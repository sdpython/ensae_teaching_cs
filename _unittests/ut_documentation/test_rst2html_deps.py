"""
@brief      test log(time=93s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, add_missing_development_version
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


class TestRst2HtmlDeps(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "jyquickhelper"],
                                        __file__, hide=True)

    def test_rst2html_deps(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() in ("travis", "appveyor"):
            # it requires latex
            return

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

        temp = get_temp_folder(__file__, "temp_rst2html_deps")
        doc = os.path.join(temp, "..", "..", "..", "_doc",
                           "sphinxdoc", "source", "ci_status.rst")
        fulls = [doc]

        links = dict(jyquickhelper="http", pyquickhelper="http",
                     pymyinstall="http", Jenkins="http", docutils="http",
                     Jupyter="http", lightmlboard="zoo", lightmlrestapi="mll",
                     mlinsights="mli", mlprodict="mlp", sparkouille="spko",
                     spark='spk', manydataapi="mda", csharpy='cspy',
                     csharpyml='cspyml', Python='Python')
        links.update({'ML.net': 'mlnet', 'C#': 'C#'})

        for full in fulls:
            last = os.path.split(full)[-1]
            fLOG("process", last)
            with open(full, "r", encoding="utf-8") as f:
                content = f.read()
            writer = "rst"
            content = content.replace(
                "from ensae_teaching", "from src.ensae_teaching")
            text = rst2html(content, outdir=temp, writer=writer,
                            imgmath_latex_preamble=preamble, layout="sphinx",
                            extlinks=dict(issue=('https://link/%s',
                                                 'issue {0} on GitHub')),
                            epkg_dictionary=links)
            ji = os.path.join(temp, last + "." + writer)
            with open(ji, "w", encoding="utf-8") as f:
                f.write(text)
            if "ERROR/" in text:
                raise Exception(text)
            if "git clone" not in text:
                raise Exception(text)


if __name__ == "__main__":
    unittest.main()
