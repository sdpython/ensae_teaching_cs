# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.jenkinshelper import JenkinsExt


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


from src.ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, default_jenkins_jobs


class TestJenkins(unittest.TestCase):

    def test_jenkins_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        engines = dict(anaconda2="C:\\Anaconda2", anaconda3="C:\\Anaconda3",
                       winpython="C:\\WinPython-64bit-3.4.2.3\\python-3.4.2.amd64",
                       default="c:\\PythonXX_x64", py27="c:\\Python27", py35="c:\\Python35_x64",
                       py36="c:\\Python36_x64", Python34="py34", Python35="py35",
                       Python36="py36", Anaconda3="apy35", Anaconda2="apy27",
                       Python27="py27", WinPython35="wpy35", WinPython36="wpy36",
                       Python35pyq="DDD", Python37="py37")
        vers = "%d%d" % sys.version_info[:2]
        engines["Python" + vers] = "py" + vers

        js = JenkinsExt('http://machine:8080/', "user",
                        "password", mock=True, engines=engines, fLOG=fLOG)

        if sys.platform.startswith("win"):
            res = setup_jenkins_server(js,
                                       overwrite=True,
                                       location=r"c:\\jenkins\\pymy",
                                       prefix="_node_")
            self.assertGreater(len(res), 0)

            job = "pyrsslocal [py35] <-- pyquickhelper, pyensae"
            cmd = "\n".join(js.get_jenkins_script(job))
            if "PythonXX" in cmd:
                raise Exception(cmd)

    def test_jenkins_local27(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        modules = default_jenkins_jobs(".*yml.*", ".*update.*")
        self.assertEqual(len(modules), 34)
        modules = default_jenkins_jobs(".*27.*", ".*update.*")
        self.assertEqual(len(modules), 0)


if __name__ == "__main__":
    unittest.main()
