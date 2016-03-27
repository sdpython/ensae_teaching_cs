"""
@brief      test log(time=4s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import requests
import time


try:
    import src
    import pyquickhelper as skip_
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
    import src
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG, get_url_content
from src.ensae_teaching_cs.td_1a.simple_flask_site import app
from src.ensae_teaching_cs.td_1a.flask_helper import FlaskInThread


class TestSimpleFlask (unittest.TestCase):

    def test_flask(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            # skip travis and Flask
            return

        th = FlaskInThread(app, host="localhost", port=8025)
        th.start()

        site = "http://localhost:8025/"

        # main page
        c = get_url_content(site)
        assert "Simple Flask Site"

        # exception
        c = get_url_content(site + "help/exception")
        assert "STACK:" in c

        # help for
        c = get_url_content(site + "help/ask/for/help")
        fLOG(c)
        assert "help for command: ask/for/help" in c

        # shutdown
        c = requests.post(site + "shutdown/")
        fLOG(c.text)
        assert "Server shutting down..." in c.text

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
