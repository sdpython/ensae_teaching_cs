"""
@brief      test log(time=1s)
"""

import os
import unittest
import folium
from pyquickhelper.pycode import get_temp_folder


class TestModulesImport(unittest.TestCase):

    def test_folium(self):
        temp = get_temp_folder(__file__, "temp_folium")
        outfile = os.path.join(temp, "osm.map")

        map_osm = folium.Map(location=[48.85, 2.34])
        map_osm.save(outfile=outfile)
        self.assertTrue(os.path.exists(outfile))


if __name__ == "__main__":
    unittest.main()
