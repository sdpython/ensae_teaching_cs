"""
@brief      test log(time=3s)
"""
import unittest
import warnings
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from ensae_teaching_cs.data import wines_quality


class TestData2a(ExtTestCase):

    def test_wines_quality(self):
        temp = get_temp_folder(__file__, "temp_wines_quality")
        text = wines_quality(local=True, filename=False)
        self.assertNotEmpty(text)

        name = wines_quality(local=True, filename=True)
        self.assertEndsWith("wines-quality.csv", name)

        try:
            text2 = wines_quality(
                local=False, cache_folder=temp, filename=False)
        except ConnectionResetError as e:
            warnings.warn("Cannot check remote wines-quality.csv.\n" + str(e))
            return

        self.assertNotEmpty(text2)
        self.assertEqual(len(text), len(text2))
        self.maxDiff = None
        self.assertEqual(text, text2)


if __name__ == "__main__":
    unittest.main()
