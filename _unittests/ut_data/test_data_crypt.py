"""
@brief      test log(time=3s)
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

try:
    import pyensae as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae as skip__

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.data import encrypt_data, decrypt_data


class TestCryptHelper(unittest.TestCase):

    def test_crypt_helper(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_crypt")

        input = os.path.abspath(__file__.replace(".pyc", ".py"))
        output = os.path.join(temp, "crypted.bin")
        output2 = os.path.join(temp, "decrypted.txt")
        key = "01" * 8
        encrypt_data(key, input, output)
        decrypt_data(key, output, output2)
        with open(input, "r") as f:
            t1 = f.read()
        with open(output2, "r") as f:
            t2 = f.read()
        self.assertEqual(t1, t2)
        assert len(t1) > 0
        encrypt_data("xdamerat" * 2, r"C:\xadupre\__home_\_data\GitHub\ensae_teaching_cs\_doc\competitions\2016\answer.txt",
                     "answers.bin")

if __name__ == "__main__":
    unittest.main()
