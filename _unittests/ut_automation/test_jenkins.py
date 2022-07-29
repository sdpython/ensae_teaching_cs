# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import sys
import unittest
from pyquickhelper.loghelper import noLOG
from pyquickhelper.pycode import ExtTestCase
from pyquickhelper.jenkinshelper import JenkinsExt
from ensae_teaching_cs.automation.jenkins_helper import (
    default_jenkins_jobs)


class TestJenkins(ExtTestCase):

    def test_jenkins_local(self):
        engines = dict(anaconda2="C:\\Anaconda2", anaconda3="C:\\Anaconda3",
                       winpython="C:\\WinPython-64bit-3.4.2.3\\python-3.4.2.amd64",
                       default="c:\\PythonXX_x64", py27="c:\\Python27", py35="c:\\Python35_x64",
                       py36="c:\\Python36_x64", Python34="py34", Python35="py35",
                       Python36="py36", Anaconda3="apy35", Anaconda2="apy27",
                       Python27="py27", WinPython35="wpy35", WinPython36="wpy36",
                       Python35pyq="DDD", Python37="py37", Python38="py38", Python39="py39")
        vers = "%d%d" % sys.version_info[:2]
        engines["Python" + vers] = "py" + vers

        js = JenkinsExt('http://machine:8080/', "user",
                        "password", mock=True, engines=engines, fLOG=noLOG)
        self.assertNotEmpty(js)

    def test_jenkins_local27(self):
        modules = default_jenkins_jobs(".*yml.*", ".*update.*")
        self.assertIn(len(modules), (33, 34, 35))
        modules = default_jenkins_jobs(".*27.*", ".*update.*")
        self.assertEqual(len(modules), 0)


if __name__ == "__main__":
    unittest.main()
