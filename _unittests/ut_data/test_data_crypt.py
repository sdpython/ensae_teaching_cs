"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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


if __name__ == "__main__":
    unittest.main()
