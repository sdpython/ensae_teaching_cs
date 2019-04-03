"""
@brief      test log(time=1s)
"""
import unittest
from ensae_teaching_cs.doc import regex_cases


class TestDocRegex(unittest.TestCase):

    def test_regex(self):
        df = regex_cases()
        self.assertEqual(df.shape, (26, 2))


if __name__ == "__main__":
    unittest.main()
