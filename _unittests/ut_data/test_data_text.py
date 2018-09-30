# -*- coding: utf-8 -*-
"""
@brief      test log(time=13s)
"""

import sys
import os
import unittest
from pyquickhelper.pycode import ExtTestCase


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

from src.ensae_teaching_cs.data import load_sentiment_dataset


class TestDataText(ExtTestCase):

    def test_sentiment_download(self):
        df = load_sentiment_dataset()
        self.assertEqual(list(df.columns), ['sentance', 'sentiment', 'source'])
        self.assertEqual(df.shape, (3000, 3))


if __name__ == "__main__":
    unittest.main()
