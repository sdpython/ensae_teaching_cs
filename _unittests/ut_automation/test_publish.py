# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import noLOG
from pyquickhelper.pycode import ExtTestCase

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


from src.ensae_teaching_cs.automation import publish_teachings_to_web


class TestPublish(ExtTestCase):

    def test_publish(self):
        if sys.platform.startswith("win"):
            letter = "d" if os.path.exists("d:") else "c"
            location = letter + ":\\jenkins\\pymy\\%s\\%s%s\\dist\\%s"
        else:
            location = "/var/lib/jenkins/workspace/%s/%s%s/dist/%s"

        rootw = "/www/htdocs/app/%s/%s"
        rootw2 = "/lesenfantscodaient.fr"
        google_id = "NOGOODID"
        suffix = ("_UT_%d%d_std" % sys.version_info[:2],)

        projects = publish_teachings_to_web("nologin", location=location, exc=False,
                                            suffix=suffix, transfer=False,
                                            fLOG=noLOG, google_id=google_id,
                                            rootw=rootw, rootw2=rootw2)
        n = 0
        for _ in projects:
            if "ensae_teaching_cs" not in _["local"]:
                continue
            self.assertIn("/helpsphinx", _["root_web"])
            n += 1
        self.assertGreater(n, 1)


if __name__ == "__main__":
    unittest.main()
