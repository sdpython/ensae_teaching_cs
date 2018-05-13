"""
@brief      test log(time=4s)
"""


import sys
import os
import unittest
import time
import requests
from pyquickhelper.loghelper import fLOG, get_url_content
from pyquickhelper.pycode import is_travis_or_appveyor


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

from src.ensae_teaching_cs.td_1a.simple_flask_site import app
from src.ensae_teaching_cs.td_1a.flask_helper import FlaskInThread


class TestSimpleFlask (unittest.TestCase):

    def test_flask(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() in ('travis', 'circleci'):
            # Get an error: urllib.error.URLError: <urlopen error [Errno 99] Cannot assign requested address>.
            return

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
        c = requests.post(site + "shutdown/")
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
