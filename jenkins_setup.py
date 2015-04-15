"""
copy the documentation to the website
"""
import sys, os
sys.path.append (r"../github/pyquickhelper/src")
sys.path.append (r"../github/pyensae/src")
sys.path.append (r"../github/ensae_teaching_cs/src")

from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, JenkinsExt

js = JenkinsExt('http://localhost:8080/', None, None)

if True:
    setup_jenkins_server(   js,
                        fLOG=print,
                        overwrite = True,
                        location = r"c:\\jenkins\\pymy")

if True:
    setup_jenkins_server(js,
                        fLOG=print,
                        overwrite = True,
                        location = r"c:\\jenkins\\pymy_nodep",
                        no_dep=True,
                        prefix = "_nodep_")

