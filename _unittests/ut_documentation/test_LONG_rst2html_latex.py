"""
@brief      test log(time=93s)
"""

import sys
import os
import warnings
import unittest
from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.helpgen import rst2html


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


class TestRst2HtmlLatex(unittest.TestCase):

    def test_rst2html_png_bug(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # it requires latex
            return

        if sys.version_info[0:2] <= (3, 4):
            # unpexpected failure
            return

        self.assertTrue(src is not None)

        preamble = """
                    \\newcommand{\\acc}[1]{\\left\\{#1\\right\\}}
                    \\newcommand{\\abs}[1]{\\left\\{#1\\right\\}}
                    \\newcommand{\\cro}[1]{\\left[#1\\right]}
                    \\newcommand{\\pa}[1]{\\left(#1\\right)}
                    \\newcommand{\\girafedec}[3]{ \\begin{array}{ccccc} #1 &=& #2 &+& #3 \\\\ a' &=& a &-& o  \\end{array}}
                    \\newcommand{\\vecteur}[2]{\\pa{#1,\\dots,#2}}
                    \\newcommand{\\R}[0]{\\mathbb{R}}
                    \\newcommand{\\N}[0]{\\mathbb{N}}
                    \\newcommand{\\indicatrice}[1]{\\mathbf{1\\!\\!1}_{\\acc{#1}}}
                    \\usepackage[all]{xy}
                    \\newcommand{\\infegal}[0]{\\leqslant}
                    \\newcommand{\\supegal}[0]{\\geqslant}
                    \\newcommand{\\ensemble}[2]{\\acc{#1,\\dots,#2}}
                    \\newcommand{\\fleche}[1]{\\overrightarrow{ #1 }}
                    \\newcommand{\\esp}{\\mathbb{E}}
                    """

        temp = get_temp_folder(__file__, "temp_rst2html_png_latex")
        doc = os.path.join(temp, "..", "..", "..", "_doc",
                           "sphinxdoc", "source", "specials")
        files = os.listdir(doc)
        fulls = [os.path.join(doc, _) for _ in files]
        fLOG("number of files", len(fulls))
        if len(fulls) > 10:
            fulls = fulls[:10]

        for full in fulls:
            if os.path.splitext(full)[-1] != ".rst":
                continue
            if "index_expose" in full or "index.rst" in full:
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
            try:
                text = rst2html(content, outdir=temp,
                                imgmath_latex_preamble=preamble,
                                extlinks=dict(issue=('https://link/%s',
                                                     'issue {0} on GitHub')))
            except NotImplementedError as e:
                if "Unknown node: todoext_node" in str(e):
                    warnings.warn("todoext has no outputs in latex")
                    continue
                else:
                    raise e

            for r in rem:
                find = sys.path.index(r)
                del sys.path[find]

            # fLOG(text)
            ji = os.path.join(temp, last + ".html")
            with open(ji, "w", encoding="utf-8") as f:
                f.write(text)


if __name__ == "__main__":
    unittest.main()
