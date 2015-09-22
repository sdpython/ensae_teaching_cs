"""
copy the documentation to the website
"""
import sys
import os
sys.path.append("../pyquickhelper/src")
sys.path.append("../pyensae/src")
sys.path.append("../ensae_teaching_cs/src")
sys.path.append("../pymyinstall/src")

from pyquickhelper import fLOG
from pyquickhelper.jenkinshelper import JenkinsExt
from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, engines_default

fLOG(OutputPrint=True)
fLOG("start")

js = JenkinsExt('http://localhost:8080/', None, None,
                fLOG=fLOG, engines=engines_default)
# js.delete_all_jobs()

if True:
    setup_jenkins_server(js,
                         overwrite=True,
                         location=r"c:\\jenkins\\pymy")

if False:
    setup_jenkins_server(js,
                         overwrite=True,
                         location=r"c:\\jenkins\\pymy_nodep",
                         no_dep=True,
                         prefix="_nodep_")
