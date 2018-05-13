"""
@brief      test log(time=1s)
"""

import sys
import os
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


class TestModulesImport(unittest.TestCase):

    def test_folium(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import folium
        temp = get_temp_folder(__file__, "temp_folium")
        outfile = os.path.join(temp, "osm.map")

        map_osm = folium.Map(location=[48.85, 2.34])
        map_osm.save(outfile=outfile)
        self.assertTrue(os.path.exists(outfile))


if __name__ == "__main__":
    unittest.main()
