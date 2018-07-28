"""
@brief      test tree node (time=5s)
"""


import sys
import os
import unittest
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from pyquickhelper.pycode.setup_helper import write_module_scripts

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


from src.ensae_teaching_cs import __blog__


class TestWriteScript(ExtTestCase):

    def test_write_script(self):
        temp = get_temp_folder(__file__, "temp_write_script")

        res = write_module_scripts(temp, "win32", __blog__)
        self.assertGreater(len(res), 2)
        for c in res:
            self.assertExists(c)
            with open(c, "r") as f:
                content = f.read()
            if "__" in content:
                for line in content.split("\n"):
                    if "__" in line and "sys.path.append" not in line and "__file__" not in line:
                        raise Exception(content)
            if ".xml" in c:
                if '<outline text="' not in content:
                    raise Exception(content)


if __name__ == "__main__":
    unittest.main()
