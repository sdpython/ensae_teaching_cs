"""
@brief      test log(time=6s)

"""


import sys
import os
import unittest
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

from pyquickhelper import fLOG
from pyrsslocal.helper.download_helper import get_url_content_timeout
from src.ensae_teaching_cs.automation import rss_teachings_update_run_server


class TestSimpleServerRSSTeaching (unittest.TestCase):

    def test_server_start_run(self):
        """
        if this test fails, the unit test is stuck, you need to stop the program yourself
        """
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.split(__file__)[0])
        dbfile = os.path.join(path, "temp_rss_starver", "blogs_rss.db3")

        #server = RSSServer(('localhost', 8093), dbfile)
        #thread = RSSServer.run_server(server, dbfile, thread=True)

        rss_teachings_update_run_server(dbfile=dbfile)

        fLOG("fetching first url")
        url = "http://localhost:8093/"
        cont = get_url_content_timeout(url)
        if "Traceback" in cont:
            fLOG(cont)
        assert "Traceback" not in cont
        assert len(cont) > 0
        assert "RSS" in cont
        assert "XD blog" in cont

        url = "http://localhost:8093/rss_status.html"
        cont = get_url_content_timeout(url)
        if "Traceback" in cont:
            fLOG(cont)
        assert "Traceback" not in cont
        assert len(cont) > 0
        assert "RSS" in cont
        assert "interesting" in cont

        url = "http://localhost:8093/rss_search.html?searchterm=pypi&usetag=usetag"
        cont = get_url_content_timeout(url)
        if "Traceback" in cont:
            fLOG(cont)
        assert "Traceback" not in cont
        assert len(cont) > 0
        assert "RSS" in cont
        if "PyPI" not in cont:
            fLOG(cont)
            assert False
        # if "added" not in cont:
        #    fLOG(cont)
        #    assert False
        assert "Mozilla Continues" not in cont

        fLOG("fetching first url")
        url = "http://localhost:8093/rss_search.html?searchterm=military"
        cont = get_url_content_timeout(url)
        if "Traceback" in cont:
            fLOG(cont)
        assert "Traceback" not in cont
        assert len(cont) > 0
        assert "RSS" in cont
        assert "interesting" not in cont
        assert "Military" in cont
        assert "Mozilla Continues" not in cont

        thread.shutdown()
        assert not thread.is_alive()


if __name__ == "__main__":
    unittest.main()
