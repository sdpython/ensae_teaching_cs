"""
@brief      test log(time=8s)
@author     Xavier Dupre
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


try:
    import pyquickhelper as skip____
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip____


from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.helpgen import rst2html


class TestRst2HtmlLatex(unittest.TestCase):

    def test_rst2html_png_bug(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # it requires latex
            return

        assert src is not None

        preamble = """
                    \\newcommand{\\acc}[1]{\\left\\{#1\\right\\}}
                    \\newcommand{\\cro}[1]{\\left[#1\\right]}
                    \\newcommand{\\pa}[1]{\\left(#1\\right)}
                    \\newcommand{\\girafedec}[3]{ \\begin{array}{ccccc} #1 &=& #2 &+& #3 \\\\ a' &=& a &-& o  \\end{array}}
                    \\newcommand{\\vecteur}[2]{\\pa{#1,\\dots,#2}}
                    \\newcommand{\\R}[0]{\\mathbb{R}}
                    \\newcommand{\\N}[0]{\\mathbb{N}}
                    \\newcommand{\\indicatrice}[1]{\\mathbf{1\\!\\!1}_{\\acc{#1}}}
                    \\usepackage[all]{xy}
                    """

        temp = get_temp_folder(__file__, "temp_rst2html_png_latex")
        doc = os.path.join(temp, "..", "..", "..", "_doc",
                           "sphinxdoc", "source", "specials")
        files = os.listdir(doc)
        fulls = [os.path.join(doc, _) for _ in files]

        for full in fulls:
            if os.path.splitext(full)[-1] != ".rst":
                continue
            if "index_expose" in full:
                continue
            rem = []
            if "hermionne" in full:
                p = os.path.abspath(os.path.dirname(src.__file__))
                fLOG("add", p)
                sys.path.append(p)
                rem.append(p)
            last = os.path.split(full)[-1]
            fLOG("process", last)
            with open(full, "r", encoding="utf-8") as f:
                content = f.read()
            text = rst2html(content, outdir=temp,
                            imgmath_latex_preamble=preamble)

            for r in rem:
                find = sys.path.index(r)
                del sys.path[find]

            # fLOG(text)
            ji = os.path.join(temp, last + ".html")
            with open(ji, "w", encoding="utf-8") as f:
                f.write(text)


if __name__ == "__main__":
    unittest.main()
