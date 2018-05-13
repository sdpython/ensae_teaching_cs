# -*- coding: utf-8 -*-
"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
import numpy
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


class TestPythonnet(unittest.TestCase):

    def test_pythonnet(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.platform.startswith("win"):
            from src.ensae_teaching_cs.pythonnet import clr
            clr.AddReference("System")
            clr.AddReference("System.Collections")
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
                if "Audio device error encountered" in str(e) or \
                        "Erreur de périphérique audio rencontrée" in str(e):
                    # maybe the script is running on a virtual machine (no
                    # Audia device)
                    if os.environ["USERNAME"] == "ensaestudent" or \
                       os.environ["USERNAME"] == "vsxavierdupre" or \
                       os.environ["USERNAME"] == "vsxavierdupre" or \
                       "DOUZE2016" in os.environ["COMPUTERNAME"] or \
                       "ENSAE" in os.environ["COMPUTERNAME"] or \
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
            from src.ensae_teaching_cs.pythonnet import clr
            clr.AddReference("System.Collections")
            from System import IntPtr, Array, Double
            from System.Runtime.InteropServices import Marshal
            assert Double is not None
            assert Array is not None
            assert IntPtr is not None

            array = numpy.ones((2, 2))
            ar = clr.IntPtr_long(array.__array_interface__['data'][0])
            ar2 = Array[int]([0, 0, 0, 0] * 2)
            fLOG(type(ar))
            fLOG(type(ar2), list(ar2))
            Marshal.Copy(ar, ar2, 0, len(ar2))
            fLOG(list(ar2))


if __name__ == "__main__":
    unittest.main()
