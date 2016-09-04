"""
@brief      test log(time=3s)
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
from src.ensae_teaching_cs.data import besancon_df, added


class TestDataZip(unittest.TestCase):

    def test_besancon_df(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from pyensae.datasource import DownloadDataException
        temp = get_temp_folder(__file__, "temp_besancon")
        text = besancon_df(local=True, fLOG=fLOG)
        assert text is not None
        assert isinstance(text, str)

        try:
            text2 = besancon_df(local=False, cache_folder=temp, fLOG=fLOG)
            assert text2
            assert isinstance(text2, str)
        except (ConnectionResetError, DownloadDataException) as e:
            warnings.warn("Cannot check remote besancon_df.txt.\n" + str(e))
            return

    def test_added(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from pyensae.datasource import DownloadDataException
        temp = get_temp_folder(__file__, "temp_added")
        text = besancon_df(local=True, fLOG=fLOG)
        assert text is not None
        assert isinstance(text, str)

        try:
            text2 = added(local=False, cache_folder=temp, fLOG=fLOG)
            assert text2
            assert isinstance(text2, str)
        except (ConnectionResetError, DownloadDataException) as e:
            warnings.warn("Cannot check remote added.txt.\n" + str(e))
            return


if __name__ == "__main__":
    unittest.main()
