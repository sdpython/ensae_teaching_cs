"""
@brief      test log(time=3s)
"""
import os
import unittest
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from ensae_teaching_cs.data import load_irep


class TestDataIrep(ExtTestCase):

    def test_irep(self):
        temp = get_temp_folder(__file__, "temp_irep")
        found = load_irep(cache=temp)
        self.assertIsInstance(found, list)
        self.assertGreater(len(found), 20)
        for year in range(2003, 2018):
            self.assertExists(os.path.join(temp, str(year), 'emissions.csv'))


if __name__ == "__main__":
    unittest.main()
