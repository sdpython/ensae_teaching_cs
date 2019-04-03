"""
@brief      test log(time=50s)
"""
import os
import unittest
import warnings
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, ExtTestCase
from ensae_teaching_cs.faq.faq_web import webshot, webhtml


class TestLONGFaqWeb(ExtTestCase):

    def test_selenium_html(self):
        if is_travis_or_appveyor():
            return

        url = "http://www.xavierdupre.fr"
        navigator = "chrome"
        html = webhtml(url, navigator=navigator)
        self.assertNotEmpty(html)
        self.assertEqual(len(html[0]), 2)
        if "href" not in html[0][1]:
            raise Exception(html)

        # module='splinter')
        html = webhtml(url, navigator=navigator)
        self.assertNotEmpty(html)
        self.assertEqual(len(html[0]), 2)
        if "href" not in html[0][1]:
            raise Exception(html)

    def test_selenium_image(self):
        if is_travis_or_appveyor():
            return

        temp = get_temp_folder(__file__, "temp_selenium_image")
        img = os.path.join(temp, "image_selenium.png")
        url = "http://www.xavierdupre.fr/"
        navigator = "chrome"
        # download_chromedriver(dest=temp)
        # os.environ["PATH"] += ";" + temp
        res = webshot(img, url, navigator=navigator)
        self.assertExists(img)
        self.assertEqual(len(res), 1)
        self.assertEqual(len(res[0]), 2)

        if navigator != "opera":
            # not available on splinter
            img = os.path.join(temp, "image_splinter.png")
            res = webshot(img, url, module='splinter', navigator=navigator)
            img = res[0][1]
            self.assertExists(img)
            self.assertEqual(len(res), 1)
            self.assertEqual(len(res[0]), 2)
        else:
            warnings.warn("opera not available on splinter")


if __name__ == "__main__":
    unittest.main()
