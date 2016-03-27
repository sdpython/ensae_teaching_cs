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

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.mypython.custom_magics import CustomMagics


class TestCustomMagic (unittest.TestCase):

    def test_voice(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        return
        if sys.platform.startswith("win"):
            cm = CustomMagics()
            cm.SPEAK("fr-FR", "hello")

    def test_cs(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.platform.startswith("win"):
            cm = CustomMagics()
            code = "public static double SquareX(double x) {return x*x ; }"
            f = cm.CS("SquareX", code)
            x = f(2.0)
            assert x == 4

    def test_cs2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.platform.startswith("win"):
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
            li = [2, 4, 5, 3, 1]
            lis = ";".join(str(i) for i in li)
            x = f(lis)
            fLOG("results", x)
            assert x != 4
            assert x is not None


if __name__ == "__main__":
    unittest.main()
