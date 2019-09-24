"""
@brief      test log(time=93s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.helpgen import rst2html
import ensae_teaching_cs


class TestRst2HtmlLatex(unittest.TestCase):

    def test_rst2html_png_bug(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(ensae_teaching_cs is not None)

        links = {
            'Python': 'https://www.python.org/',
            'git': 'https://fr.wikipedia.org/wiki/Git',
            'numpy': 'http://www.numpy.org/',
            'pandas': 'https://pandas.pydata.org/',
            'matplotlib': 'https://matplotlib.org/',
            'bokeh': 'https://bokeh.pydata.org/en/latest/',
            'pyecharts': 'https://github.com/pyecharts/pyecharts',
            'cartopy': 'https://scitools.org.uk/cartopy/docs/latest/',
            'flask': 'http://flask.pocoo.org/',
            'numba': 'https://numba.pydata.org/',
            'Cython': 'http://cython.org/',
            'pybind11': 'https://github.com/pybind/pybind11',
        }

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
        doc_folders = [os.path.join(temp, "..", "..", "..", "_doc",
                                    "sphinxdoc", "source", "questions"),
                       os.path.join(temp, "..", "..", "..", "_doc",
                                    "sphinxdoc", "source", "specials")]

        fulls = []
        for doc in doc_folders:
            fulls.extend(os.path.join(doc, _) for _ in os.listdir(doc))

        # filter
        fulls = [_ for _ in fulls if "route_1A_2018" in _]

        # second filter
        fLOG("number of files", len(fulls))
        if len(fulls) > 10:
            fulls = fulls[:10]

        # process
        for full in fulls:
            if os.path.splitext(full)[-1] != ".rst":
                continue
            if "index_expose" in full or "index.rst" in full:
                continue
            rem = []
            if "hermionne" in full:
                p = os.path.abspath(os.path.join(
                    os.path.dirname(ensae_teaching_cs.__file__), ".."))
                fLOG("add", p)
                sys.path.append(p)
                rem.append(p)
            last = os.path.split(full)[-1]
            fLOG("process", last)
            with open(full, "r", encoding="utf-8") as f:
                content = f.read()
            try:
                text = rst2html(content, outdir=temp, layout="sphinx",
                                imgmath_latex_preamble=preamble,
                                epkg_dictionary=links,
                                extlinks=dict(issue=('https://link/%s',
                                                     'issue {0} on GitHub')))
            except NotImplementedError as e:
                if "Unknown node: todoext_node" in str(e):
                    warnings.warn("todoext has no outputs in latex")
                    continue
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
