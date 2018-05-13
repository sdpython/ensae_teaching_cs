"""
@brief      test log(time=6s)
"""


import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor


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


class TestModulesOpenCl(unittest.TestCase):

    def test_opencl(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            dll = os.path.join("c:\\Windows\\System32", "OpenCL.DLL")
            if not os.path.exists(dll):
                warnings.warn("Missing DLL: " + dll)
                return

        if is_travis_or_appveyor():
            # skipping on automated build
            return

        import numpy as np
        import pyopencl as cl

        a_np = np.random.rand(50000).astype(np.float32)
        b_np = np.random.rand(50000).astype(np.float32)

        # execute cl.create_some_context() from a console
        # and set up the following environment variable
        os.environ["PYOPENCL_CTX"] = '0:1'
        ctx = cl.create_some_context()
        queue = cl.CommandQueue(ctx)

        mf = cl.mem_flags
        a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
        b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

        prg = cl.Program(ctx, """
        __kernel void sum(
            __global const float *a_g, __global const float *b_g, __global float *res_g)
        {
          int gid = get_global_id(0);
          res_g[gid] = a_g[gid] + b_g[gid];
        }
        """).build()

        res_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)
        prg.sum(queue, a_np.shape, None, a_g, b_g, res_g)

        res_np = np.empty_like(a_np)
        cl.enqueue_copy(queue, res_np, res_g)

        # Check on CPU with Numpy:
        fLOG(res_np - (a_np + b_np))
        fLOG(np.linalg.norm(res_np - (a_np + b_np)))


if __name__ == "__main__":
    unittest.main()
