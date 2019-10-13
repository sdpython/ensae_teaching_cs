"""
@brief      test log(time=3s)
"""
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from ensae_teaching_cs.data import (
    besancon_df, added,
    deal_flow_espace_vert_2018_2019
)


class TestDataZip(ExtTestCase):

    def test_besancon_df(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from pyensae.datasource import DownloadDataException
        temp = get_temp_folder(__file__, "temp_besancon")
        text = besancon_df(local=True, fLOG=fLOG)
        self.assertNotEmpty(text)
        self.assertIsInstance(text, str)

        try:
            text2 = besancon_df(local=False, cache_folder=temp, fLOG=fLOG)
            assert text2
            self.assertIsInstance(text2, str)
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
        text = added(local=True, fLOG=fLOG)
        self.assertNotEmpty(text)
        self.assertIsInstance(text, str)

        try:
            text2 = added(local=False, cache_folder=temp, fLOG=fLOG)
            assert text2
            self.assertIsInstance(text2, str)
        except (ConnectionResetError, DownloadDataException) as e:
            warnings.warn("Cannot check remote added.txt.\n" + str(e))
            return

    def test_deal_flow_espace_vert_2018_2019(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from pyensae.datasource import DownloadDataException
        temp = get_temp_folder(
            __file__, "temp_deal_flow_espace_vert_2018_2019")
        text = deal_flow_espace_vert_2018_2019(local=True, fLOG=fLOG)
        self.assertNotEmpty(text)
        self.assertIsInstance(text, list)

        try:
            text2 = deal_flow_espace_vert_2018_2019(
                local=False, cache_folder=temp, fLOG=fLOG)
            self.assertNotEmpty(text2)
            self.assertIsInstance(text2, list)
        except (ConnectionResetError, DownloadDataException) as e:
            warnings.warn(
                "Cannot check remote deal_flow_espace_vert_2018_2019.zip.\n" + str(e))
            return


if __name__ == "__main__":
    unittest.main()
