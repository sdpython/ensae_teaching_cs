"""
@brief      test log(time=10s)

"""
import os
import sys
import unittest


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


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.helpers.image_helper import collate_images, convert_image


class TestImageHelper(unittest.TestCase):

    def test_collate_image(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_collate_image")
        img = os.path.join(temp, "..", "data")
        imgs = os.listdir(img)
        png = [os.path.join(img, _)
               for _ in imgs if os.path.splitext(_)[-1] == ".png" and "00" not in _]
        self.assertTrue(len(png) > 0)
        out = os.path.join(temp, "out_collate.png")
        im = collate_images(png, out)
        self.assertTrue(os.path.exists(out))
        self.assertTrue(im is not None)

    def test_convert_imgae(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_convert_image")
        img = os.path.join(temp, "..", "data", "snippet.png")
        res = convert_image(img, "jpg", temp)
        self.assertEqual(len(res), 1)
        self.assertTrue(os.path.exists(res[0]))
        s1 = os.stat(img).st_size
        s2 = os.stat(res[0]).st_size
        self.assertTrue(s1 > s2)
        self.assertTrue(s2 > 0)


if __name__ == "__main__":
    unittest.main()
