"""
@brief      test log(time=6s)

"""


import sys
import os
import unittest
import warnings
import shutil
import warnings

try:
    import src
    import pyquickhelper
    import pyensae
    import pyrsslocal
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
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
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyrsslocal",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper
    import pyensae
    import pyrsslocal

from pyquickhelper import fLOG, get_temp_folder
from pyrsslocal.helper.download_helper import get_url_content_timeout
from pyrsslocal import RSSServer
from src.ensae_teaching_cs.automation import __file__ as location
from src.ensae_teaching_cs.automation.rss_teachings_blog import rss_teachings_update_run_server


class TestSimpleServerRSSTeaching (unittest.TestCase):

    def test_server_start_run(self):
        """
        if this test fails, the unit test is stuck, you need to stop the program yourself
        """
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            # skip travis and Flask
            warnings.warn(
                "travis, unable to test TestSimpleServerRSSTeaching.test_server_start_run")
            return

        temp = get_temp_folder(__file__, "temp_rss_starter")
        dirn = os.path.abspath(os.path.dirname(location))
        xmlb = None

        data = os.path.join(temp, "..", "data", "ensae_teaching_cs_blogs.db3")
        shutil.copy(data, temp)
        dbfile = os.path.join(temp, "ensae_teaching_cs_blogs.db3")

        server = RSSServer(('localhost', 8093), dbfile)

        thread = rss_teachings_update_run_server(dbfile=dbfile, xml_blogs=xmlb,
                                                 browser="none",
                                                 server=server, thread=True)

        fLOG(thread)
        fLOG("fetching first url")
        url = "http://localhost:8093/"
        cont = get_url_content_timeout(url)
        if "Traceback" in cont and not "l''exception ::      Traceback" in cont:
            raise Exception(cont)
        assert len(cont) > 0
        assert "RSS" in cont
        assert "XD blog" in cont

        fLOG("fetching first url")
        url = "http://localhost:8093/rss_search.html?searchterm=command"
        cont = get_url_content_timeout(url)
        if "Traceback" in cont:
            fLOG(cont)
        if "Traceback" in cont and not "l''exception ::      Traceback" in cont:
            raise Exception(cont)
        assert len(cont) > 0
        assert "RSS" in cont
        assert "interesting" not in cont
        assert "command" in cont

        thread.shutdown()
        assert not thread.is_alive()


if __name__ == "__main__":
    unittest.main()
