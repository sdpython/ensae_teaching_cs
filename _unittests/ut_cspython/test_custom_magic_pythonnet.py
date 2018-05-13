"""
@brief      test log(time=4s)
"""

import sys
import os
import unittest


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

from src.ensae_teaching_cs.cspython.custom_magics import CustomMagics


class TestCustomMagic (unittest.TestCase):

    def test_cs2(self):
        cm = CustomMagics()
        code = "public static double SquareX(double x) {return x*x ; }"
        code = """
                public static long[] cs_qsortl(long[] li)
                {
                    if (li.Length == 0)
                    {
                        return null;
                    }
                    else
                    {
                        var pivot = li[0];
                        var lesser = cs_qsortl(li.Skip(1).Where(x => x < pivot).ToArray());
                        var greater = cs_qsortl(li.Skip(1).Where(x => x >= pivot).ToArray());
                        long[] res = new long[li.Length];

                        if (lesser != null && lesser.Length > 0) Array.Copy(lesser, 0, res, 0, lesser.Length);
                        int nb = lesser == null ? 0 : lesser.Length;
                        res[nb] = pivot;
                        if (greater != null && greater.Length > 0) Array.Copy(greater, 0, res, nb + 1, greater.Length);

                        return res;
                    }
                }

                public static long[] cs_qsort(string lis)
                {
                    return cs_qsortl(lis.Split(';').Select(c=>long.Parse(c)).ToArray()) ;
                }
                """
        f = cm.CS("cs_qsort", code)
        if f is None:
            raise Exception(code)
        li = [2, 4, 5, 3, 1]
        lis = ";".join(str(i) for i in li)
        x = f(lis)
        self.assertNotEqual(x, 4)
        self.assertTrue(x is not None)


if __name__ == "__main__":
    unittest.main()
