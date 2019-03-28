"""
@brief      test log(time=3s)
"""
import unittest
from ensae_teaching_cs.data import simple_database


class TestDataWeb(unittest.TestCase):

    def test_simple_database(self):
        name = simple_database(local=True)
        assert name.endswith(".db3")


if __name__ == "__main__":
    unittest.main()
