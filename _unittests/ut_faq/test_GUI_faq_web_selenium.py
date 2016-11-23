"""
@brief      test log(time=50s)
"""

import sys
import os
import unittest
import warnings


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
    import pyquickhelper as skip_
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
    import pyquickhelper as skip_

try:
    import pyensae as skip__
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
    import pyensae as skip__

try:
    import pymyinstall as skip____
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
    import pymyinstall as skip____


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from src.ensae_teaching_cs.faq.faq_web import webshot, webhtml


class TestLONGFaqWeb(unittest.TestCase):

    def test_selenium_html(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            return

        url = "http://www.xavierdupre.fr"
        navigator = "chrome"
        html = webhtml(url, navigator=navigator, fLOG=fLOG)
        assert len(html) > 0
        self.assertEqual(len(html[0]), 2)
        if "href" not in html[0][1]:
            raise Exception(html)

        # module='splinter')
        html = webhtml(url, navigator=navigator, fLOG=fLOG)
        assert len(html) > 0
        self.assertEqual(len(html[0]), 2)
        if "href" not in html[0][1]:
            raise Exception(html)

    def test_selenium_image(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            return

        temp = get_temp_folder(__file__, "temp_selenium_image")
        img = os.path.join(temp, "image_selenium.png")
        url = "http://www.xavierdupre.fr/"
        navigator = "chrome"
        # download_chromedriver(dest=temp)
        # os.environ["PATH"] += ";" + temp
        res = webshot(img, url, navigator=navigator, fLOG=fLOG)
        assert os.path.exists(img)
        fLOG(res)
        self.assertEqual(len(res), 1)
        self.assertEqual(len(res[0]), 2)

        if navigator != "opera":
            # not available on splinter
            img = os.path.join(temp, "image_splinter.png")
            res = webshot(img, url, module='splinter',
                          navigator=navigator, fLOG=fLOG)
            img = res[0][1]
            assert os.path.exists(img)
            fLOG(res)
            self.assertEqual(len(res), 1)
            self.assertEqual(len(res[0]), 2)
        else:
            warnings.warn("opera not available on splinter")


if __name__ == "__main__":
    unittest.main()
