# -*- coding: utf-8 -*-
"""
@brief      test log(time=13s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.data import generate_sells


class TestDataTs(ExtTestCase):

    def test_generate_sells(self):
        df = generate_sells()
        self.assertEqual(len(df), 731)


if __name__ == "__main__":
    unittest.main()
