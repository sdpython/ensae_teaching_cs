# -*- coding: utf-8 -*-
"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
import warnings
import numpy
import clr


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
        clr.AddReference("System")
        clr.AddReference("System.Collections")
        from System import String
        s = String("example")
        x = s.Replace("e", "j")
        self.assertEqual("jxamplj", x)

        from System.Collections.Generic import Dictionary
        d = Dictionary[String, String]()
        d["un"] = "1"
        self.assertEqual(d.Count, 1)

    def test_pythonnet_array(self):
        clr.AddReference("System.Collections")
        from System import IntPtr, Array, Double
        from System.Runtime.InteropServices import Marshal
        self.assertTrue(Double is not None)
        self.assertTrue(Array is not None)
        self.assertTrue(IntPtr is not None)

        array = numpy.ones((2, 2), dtype=int)
        ar = array.__array_interface__['data'][0]
        ar2 = Array[int]([0, 0, 0, 0] * 2)
        self.assertEqual(str(type(ar)), "<class 'int'>")
        self.assertEqual(str(type(ar2)), "<class 'System.Int32[]'>")
        self.assertEqual(list(ar2), [0, 0, 0, 0, 0, 0, 0, 0])
        try:
            Marshal.Copy(ar, ar2, 0, len(ar2))
        except TypeError as e:
            warnings.warn(str(e))


if __name__ == "__main__":
    unittest.main()
