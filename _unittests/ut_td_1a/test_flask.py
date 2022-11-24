"""
@brief      test log(time=4s)
"""
import sys
import unittest
import time
import requests
from pyquickhelper.loghelper import fLOG, get_url_content
from pyquickhelper.pycode import skipif_travis, skipif_circleci
from ensae_teaching_cs.td_1a.simple_flask_site import create_application
from ensae_teaching_cs.td_1a.flask_helper import FlaskInThread


class TestSimpleFlask(unittest.TestCase):

    def test_flask_recommended(self):
        app = create_application()
        with app.test_client() as cl:
            # main page
            c = cl.get("/")
            c = c.data.decode("utf-8")
            self.assertIn("Simple Flask Site", c)

            # exception
            c = cl.get("/help/exception")
            c = c.data.decode("utf-8")
            self.assertIn("STACK:", c)

            # help for
            c = cl.get("/help/ask/for/help")
            c = c.data.decode("utf-8")
            self.assertIn("help for command: ask/for/help", c)

    @skipif_travis("urllib.error.URLError: <urlopen error [Errno 99] Cannot assign requested address")
    @skipif_circleci("urllib.error.URLError: <urlopen error [Errno 99] Cannot assign requested address")
    @unittest.skipIf(not sys.platform.startswith("win"), reason="did not find the right settings to make it work.")
    def test_flask_thread(self):
        """
        On Linux, this test fails unless the firewall
        is told to allow port 8025:

        ::

            sudo ufw allow 5000
            sudo ufw enable
        """
        app = create_application()
        th = FlaskInThread(app, host="localhost", port=8025)
        th.start()

        site = "http://localhost:8025/"

        # main page
        c = get_url_content(site)
        self.assertIn("Simple Flask Site", c)

        # exception
        c = get_url_content(site + "help/exception")
        self.assertIn("STACK:", c)

        # help for
        c = get_url_content(site + "help/ask/for/help")
        fLOG(c)
        self.assertIn("help for command: ask/for/help", c)

        # shutdown
        c = requests.post(site + "shutdown/")  # pylint: disable=W3101
        fLOG(c.text)
        self.assertIn("Server shutting down...", c.text)

        nb = 0
        while th.is_alive() and nb < 5:
            fLOG("waiting...", nb)
            time.sleep(1)
            nb += 1

        if th.is_alive():
            fLOG("thread is still alive (1)?", th.is_alive())
            assert False


if __name__ == "__main__":
    unittest.main()
