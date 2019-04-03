"""
@brief      test log(time=93s)
"""
import os
import unittest
from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.filehelper import explore_folder_iterfile
from pyquickhelper.pycode import ExtTestCase


class TestPyEnsaeLinks(ExtTestCase):

    def test_pyensae_links(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        this = os.path.join(os.path.dirname(__file__),
                            '..', '..', '_doc', 'notebooks')
        checked = 0
        missed = []
        tolook = ['http://files.grouplens.org/datasets/movielens/ml-1m.zip',
                  'http://www.xavierdupre.fr/',
                  'url=\\"http',
                  '\\"Skin_NonSkin.txt\\", website=\\"https://archive.ics',
                  "website='http://telechargement.insee.fr/fichiersdetail",
                  'https://archive.ics.uci.edu/ml/machine-learning-databases']
        for note in explore_folder_iterfile(this, ".*[.]ipynb$", ".ipynb_checkpoints", fullname=True):
            with open(note, 'r', encoding='utf-8') as f:
                content = f.read()
            if "datasource import download_data" in content or "pyensae.download_data(" in content:
                checked += 1
                found = False
                for to in tolook:
                    if to in content:
                        found = True
                if not found:
                    missed.append(note)
        self.assertGreater(checked, 1)
        self.assertEmpty(missed)


if __name__ == "__main__":
    unittest.main()
