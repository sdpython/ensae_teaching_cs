"""
@brief      test log(time=8s)
"""

import sys
import os
import unittest
import pandas
from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.helpgen.stat_helper import enumerate_notebooks_link
from pyquickhelper.pycode import ExtTestCase


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


class TestHelpGenStatHelper(ExtTestCase):

    def test_format_history(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        this = os.path.abspath(os.path.dirname(__file__))
        nb_folder = os.path.join(this, "..", "..", "_doc", "notebooks")
        self.assertTrue(os.path.exists(nb_folder))
        nb_doc = os.path.join(this, "..", "..", "_doc", "sphinxdoc", "source")
        self.assertTrue(os.path.exists(nb_doc))
        nb = 0
        counts = {'title': 0}
        nbfound = set()
        rows = []
        for ind, r in enumerate(enumerate_notebooks_link(nb_folder, nb_doc)):
            rl = list(r)
            rl[0] = None if r[0] is None else os.path.split(r[0])[-1]
            rl[1] = os.path.split(r[1])[-1]
            nb += 1
            m = rl[2]
            counts[m] = counts.get(m, 0) + 1
            self.assertTrue(r[-2] is None or isinstance(r[-2], str))
            self.assertTrue(r[-1] is None or isinstance(r[-1], str))
            if r[-1] is not None:
                counts["title"] += 1
            nbfound.add(rl[1])
            rows.append(rl[:2] + rl[-2:] + [r[1].split("_doc")[-1]])
            if __name__ != "__main__" and ind > 30:
                break
        self.assertGreater(counts.get("ref", 0), 0)
        # self.assertTrue(counts.get(None, 0) > 0)
        self.assertNotEmpty(counts["title"])
        self.assertGreater(len(nbfound), 5)
        # self.assertIn("graph4exos.ipynb", nbfound)
        # self.assertTrue(counts.get("refn", 0) > 0)
        # self.assertTrue(counts.get("toctree", 0) > 0)

        df = pandas.DataFrame(data=rows, columns=[
                              "rst", "ipynb", "link", "title", "path"])
        name = os.path.join(os.path.dirname(__file__), "temp_notebook_rst.txt")
        df = df[df.rst != "all_notebooks.rst"]
        df.sort_values("ipynb").to_csv(name, sep="\t", index=False)
        self.assertTrue(name)


if __name__ == "__main__":
    unittest.main()
