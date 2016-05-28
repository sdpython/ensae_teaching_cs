"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
import numpy


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


class TestPythonnet(unittest.TestCase):

    def test_pythonnet(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.platform.startswith("win"):
            from src.ensae_teaching_cs.pythonnet import clr as skip__
            from System import String
            s = String("example")
            x = s.Replace("e", "j")
            assert "jxamplj" == x

            from System.Collections.Generic import Dictionary
            d = Dictionary[String, String]()
            d["un"] = "1"
            assert d.Count == 1

    def test_voice(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.platform.startswith("win"):
            from src.ensae_teaching_cs.pythonnet import vocal_synthesis
            try:
                vocal_synthesis("test unitaire")
            except Exception as e:
                if "Audio device error encountered" in str(e):
                    # maybe the script is running on a virtual machine (no
                    # Audia device)
                    if os.environ["USERNAME"] == "ensaestudent" or \
                       os.environ["USERNAME"] == "vsxavierdupre" or \
                       os.environ["USERNAME"] == "appveyor" or \
                       "paris" in os.environ["COMPUTERNAME"].lower() or \
                       os.environ["USERNAME"].endswith("$"):  # anonymous Jenkins configuration
                        # I would prefer to catch a proper exception
                        # it just exclude one user only used on remotre
                        # machines
                        return
                raise Exception("USERNAME: " + os.environ.get("USERNAME", "-"))

    def test_pythonnet_array(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.platform.startswith("win"):
            from src.ensae_teaching_cs.pythonnet import clr as skip__
            from System import IntPtr, Array, Double
            from System.Runtime.InteropServices import Marshal
            assert Double is not None
            assert Array is not None
            assert IntPtr is not None

            if sys.version_info[:2] <= (3, 4):
                array = numpy.ones((2, 2))
                ar = IntPtr.__overloads__[int](
                    array.__array_interface__['data'][0])
                ar2 = Array[int]([0, 0, 0, 0] * 2)
                fLOG(type(ar))
                fLOG(type(ar2), list(ar2))
                Marshal.Copy(ar, ar2, 0, len(ar2))
                fLOG(list(ar2))
            else:
                array = numpy.ones((2, 2))
                from clr import IntPtr_long
                ar = IntPtr_long(array.__array_interface__['data'][0])
                ar2 = Array[int]([0, 0, 0, 0] * 2)
                fLOG(type(ar))
                fLOG(type(ar2), list(ar2))
                Marshal.Copy(ar, ar2, 0, len(ar2))
                fLOG(list(ar2))


if __name__ == "__main__":
    unittest.main()
