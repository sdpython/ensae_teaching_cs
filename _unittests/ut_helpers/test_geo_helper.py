"""
@brief      test log(time=10s)
"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG


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


from src.ensae_teaching_cs.helpers.geo_helper import lambert93_to_WGPS


class TestGeoHelper(unittest.TestCase):

    def test_lambert93_to_longlat(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        x1, y1 = lambert93_to_WGPS(99217.1, 6049646.300000001)
        x2, y2 = lambert93_to_WGPS(1242417.2, 7110480.100000001)
        d1 = abs(x1 - (-4.1615802638173065)) + abs(y1 - 41.303505287589545)
        d2 = abs(x2 - 10.699505053975292) + abs(y2 - 50.85243395553585)
        assert d1 + d2 < 1e-8


if __name__ == "__main__":
    unittest.main()
