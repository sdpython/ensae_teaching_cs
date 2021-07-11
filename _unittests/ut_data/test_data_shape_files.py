"""
@brief      test log(time=3s)
"""
import unittest
from pyquickhelper.pycode import get_temp_folder, ExtTestCase, skipif_appveyor
from ensae_teaching_cs.data import data_shape_files, load_french_departments


class TestDataZipShapeFiles(ExtTestCase):

    def test_data_shape_files_depfr_exc(self):
        self.assertRaise(lambda: data_shape_files('depfrrr2019'), ValueError)

    @skipif_appveyor("connectivity issue")
    def test_data_shape_files_depfr(self):
        temp = get_temp_folder(__file__, 'temp_data_shape_files_depfr')
        res = data_shape_files('depfr2018', cache=temp)
        self.assertEqual(res.shape, (102, 9))
        self.assertIn('code_insee', res.columns)
        self.assertIn('nom', res.columns)
        self.assertIn('DEPLAT', res.columns)

    @skipif_appveyor("connectivity issue")
    def test_load_french_departments(self):
        df = load_french_departments()
        self.assertEqual(df.shape, (102, 7))
        self.assertIn('DEPLAT', df.columns)  # pylint: disable=E1101


if __name__ == "__main__":
    unittest.main()
