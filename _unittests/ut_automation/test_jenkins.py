#-*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest
import re

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
    import pyquickhelper
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
    import pyquickhelper

try:
    import pyensae
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
    import pyensae

try:
    import pymmails
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymmails",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymmails

try:
    import pyrsslocal
except ImportError:
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
    import pyrsslocal

try:
    import pymyinstall
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymyinstall",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymyinstall


from pyquickhelper import fLOG, get_temp_folder
from pyquickhelper.jenkinshelper import JenkinsExt
from src.ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server


class TestJenkins(unittest.TestCase):

    def test_jenkins_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        engines = dict(anaconda2="C:\\Anaconda2", anaconda3="C:\\Anaconda3",
                       winpython="C:\\WinPython-64bit-3.4.2.3\\python-3.4.2.amd64",
                       default="c:\\Python34_x64",
                       py35="c:\\Python35_x64")

        js = JenkinsExt('http://machine:8080/', "user",
                        "password", mock=True, engines=engines, fLOG=fLOG)

        if sys.platform.startswith("win"):
            res = setup_jenkins_server(js,
                                       overwrite=True,
                                       location=r"c:\\jenkins\\pymy",
                                       prefix="_node_")
            assert len(res) > 0
            
            job = "pyrsslocal [py35] <-- pyquickhelper, pyensae"
            cmd = "\n".join(js.get_jenkins_script(job))
            assert "Python34" not in cmd


if __name__ == "__main__":
    unittest.main()
