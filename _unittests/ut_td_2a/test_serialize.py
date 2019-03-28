"""
@brief      test log(time=1s)
"""
import os
import unittest
import io
import pandas
from ensae_teaching_cs.td_2a import load_object, dump_object


class TestSerialization(unittest.TestCase):

    def test_serialize(self):
        temp = os.path.abspath(os.path.dirname(__file__))
        temp = os.path.join(temp, "temp_serialization")
        if not os.path.exists(temp):
            os.mkdir(temp)

        df = pandas.DataFrame([{"name": "xavier", "school": "ENSAE"},
                               {"name": "antoine", "school": "ENSAE"}])

        outfile = os.path.join(temp, "out_df.bin")
        if os.path.exists(outfile):
            os.remove(outfile)

        dump_object(df, outfile)
        assert os.path.exists(outfile)

        df2 = load_object(outfile)
        assert df.values.tolist() == df2.values.tolist()

        s = io.BytesIO()
        dump_object(df, s)
        s.seek(0)
        df3 = load_object(s)
        assert df.values.tolist() == df3.values.tolist()


if __name__ == "__main__":
    unittest.main()
