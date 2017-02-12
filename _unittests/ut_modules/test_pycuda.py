"""
@brief      test log(time=6s)
"""


import sys
import os
import unittest
import warnings


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
from pyquickhelper.pycode import is_travis_or_appveyor


class TestModulesCuda(unittest.TestCase):

    def test_cuda(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            dll = os.path.join("c:\\Windows\\System32", "NVCUDA.DLL")
            if not os.path.exists(dll):
                warnings.warn("Missing DLL: " + dll)
                return

        if is_travis_or_appveyor():
            # skipping on automated build
            return

        import pycuda.driver as drv
        import numpy

        from pycuda.compiler import SourceModule
        mod = SourceModule("""
        __global__ void multiply_them(float *dest, float *a, float *b)
        {
          const int i = threadIdx.x;
          dest[i] = a[i] * b[i];
        }
        """)

        multiply_them = mod.get_function("multiply_them")

        a = numpy.random.randn(400).astype(numpy.float32)
        b = numpy.random.randn(400).astype(numpy.float32)

        dest = numpy.zeros_like(a)
        multiply_them(
            drv.Out(dest), drv.In(a), drv.In(b),
            block=(400, 1, 1), grid=(1, 1))

        fLOG(dest - a * b)


if __name__ == "__main__":
    unittest.main()
