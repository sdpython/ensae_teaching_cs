"""
@brief      test log(time=1s)
"""
import os
import unittest
import pandas
from ensae_teaching_cs.pandas_helper import dfs2excel


class TestSessionPandas(unittest.TestCase):

    def test_excel(self):
        df1 = pandas.DataFrame([{"name": "xavier", "school": "ENSAE"},
                                {"name": "antoine", "school": "ENSAE"}])

        df2 = pandas.DataFrame([{"name": "xavier", "company": "Microsoft"},
                                {"name": "antoine", "company": "Alephd"}])

        ef = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "out_example.xlsx"))
        if os.path.exists(ef):
            os.remove(ef)
        dfs2excel({"ecole": df1, "boite": df2}, ef)
        assert os.path.exists(ef)


if __name__ == "__main__":
    unittest.main()
