# -*- coding: utf-8 -*-
"""
@brief      test log(time=13s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.data import load_sentiment_dataset


class TestDataText(ExtTestCase):

    def test_sentiment_download(self):
        df = load_sentiment_dataset()
        self.assertEqual(list(df.columns), ['sentance', 'sentiment', 'source'])
        self.assertEqual(df.shape, (3000, 3))


if __name__ == "__main__":
    unittest.main()
