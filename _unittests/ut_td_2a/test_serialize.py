"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
import io
import pandas
from pyquickhelper.loghelper import fLOG


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


from src.ensae_teaching_cs.td_2a import load_object, dump_object


class TestSerialization(unittest.TestCase):

    def test_serialize(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

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
        fLOG(df2)
        fLOG(df2.values.tolist())
        assert df.values.tolist() == df2.values.tolist()

        s = io.BytesIO()
        dump_object(df, s)
        s.seek(0)
        df3 = load_object(s)
        assert df.values.tolist() == df3.values.tolist()


if __name__ == "__main__":
    unittest.main()
