"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
import warnings


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
                "src",)))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8
from pyquickhelper.pycode.utils_tests import _extended_refectoring


class TestFlake8(unittest.TestCase):

    def test_flake8_src(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2 or "Anaconda" in sys.executable \
                or "condavir" in sys.executable:
            warnings.warn(
                "skipping test_flake8 because of Python 2 or " + sys.executable)
            return

        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG, extended=[("fLOG", _extended_refectoring)],
                   neg_filter="((.*pandas_helper.*)|(.*faq_python.*))")

    def test_flake8_test(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2 or "Anaconda" in sys.executable \
                or "condavir" in sys.executable:
            warnings.warn(
                "skipping test_flake8 because of Python 2 or " + sys.executable)
            return

        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_filter="temp_.*",
                   skip=["'src' imported but unused",
                         "'skip_' imported but unused",
                         "'skip__' imported but unused",
                         "'skip___' imported but unused",
                         "'skip____' imported but unused",
                         "'skip_____' imported but unused",
                         "'skip______' imported but unused",
                         ],
                   extended=[("fLOG", _extended_refectoring)],
                   max_line_length=320)


if __name__ == "__main__":
    unittest.main()
