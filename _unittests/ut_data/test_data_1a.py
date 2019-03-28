"""
@brief      test log(time=3s)
"""
import unittest
import warnings
from pyquickhelper.pycode import get_temp_folder
from ensae_teaching_cs.data import marathon, donnees_enquete_2003_television


class TestData1a(unittest.TestCase):

    def test_marathon(self):
        temp = get_temp_folder(__file__, "temp_marathon")
        text = marathon(local=True, filename=False)
        assert text is not None

        name = marathon(local=True, filename=True)
        assert name.endswith("marathon.txt")

        try:
            text2 = marathon(local=False, cache_folder=temp, filename=False)
        except ConnectionResetError as e:
            warnings.warn("Cannot check remote marathon.txt.\n" + str(e))
            return

        assert text2 is not None
        self.assertEqual(len(text), len(text2))
        self.maxDiff = None
        self.assertEqual(text, text2)

    def test_donnees_enquete_2003_television(self):
        temp = get_temp_folder(
            __file__, "temp_donnees_enquete_2003_television")
        text = donnees_enquete_2003_television(local=True, filename=False)
        assert text is not None

        name = donnees_enquete_2003_television(local=True, filename=True)
        assert name.endswith("donnees_enquete_2003_television.txt")

        try:
            text2 = donnees_enquete_2003_television(
                local=False, cache_folder=temp, filename=False)
        except ConnectionResetError as e:
            warnings.warn(
                "Cannot check remote donnees_enquete_2003_television.txt.\n" + str(e))
            return

        assert text2 is not None
        self.assertEqual(len(text), len(text2))
        self.maxDiff = None
        self.assertEqual(text, text2)


if __name__ == "__main__":
    unittest.main()
