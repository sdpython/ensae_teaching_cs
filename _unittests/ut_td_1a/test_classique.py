"""
@brief      test log(time=1s)
"""
import unittest
from datetime import datetime
from ensae_teaching_cs.td_1a.classiques import racine_carree, commentaire_accentues, dix_entiers_carre
from ensae_teaching_cs.td_1a.classiques import repetition_a_eviter, str2date


class TestClassiques(unittest.TestCase):

    def test_fonction1(self):
        a = racine_carree(2)
        self.assertEqual(a, 2 ** 0.5)

    def test_commentaire_accentues(self):
        commentaire_accentues()

    def test_dix_entiers_carre(self):
        r = dix_entiers_carre()
        self.assertEqual(r, 385)

    def test_repetition_a_eviter(self):
        r = repetition_a_eviter([0, 1, 1, 2])
        self.assertEqual(r, 0.5)

    def test_str2date(self):
        s = str2date("9/8/2017")
        self.assertEqual(s, datetime(2017, 8, 9))


if __name__ == "__main__":
    unittest.main()
