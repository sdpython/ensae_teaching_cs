"""
@brief      test log(time=1000s)
"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder

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

from src.ensae_teaching_cs.special.rues_paris import get_data
from src.ensae_teaching_cs.special.rues_paris import eulerien_extension, distance_paris


class TestSKIPRueParis(unittest.TestCase):

    def test_get_data(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_rues")
        if not os.path.exists(folder):
            os.mkdir(folder)
        for ext in [".txt", ".zip"]:
            f = os.path.join(folder, "paris_54000" + ext)
            if os.path.exists(f):
                os.remove(f)
        try:
            data = get_data(whereTo=folder, fLOG=fLOG, timeout=60)
        except Exception as e:
            if "unable to retrieve data" in str(e):
                return
            else:
                raise Exception("*****" + str(e) + "*****") from e

        fLOG(len(data))
        assert len(data) > 0
        total = sum(_[-1] for _ in data)
        fLOG("total length", total)

    def test_algo3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        folder = get_temp_folder(__file__, "temp_algo3")
        edges = get_data(whereTo=folder, fLOG=fLOG)
        fLOG("start")
        added = eulerien_extension(edges, fLOG=fLOG, distance=distance_paris)
        assert len(added) > 0
        fLOG("nb added", len(added))
        with open(os.path.join(folder, "added.txt"), "w") as f:
            f.write(str(added))


if __name__ == "__main__":
    unittest.main()
