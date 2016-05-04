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
from src.ensae_teaching_cs.helpers.image_helper import collate_images


class TestImageHelper(unittest.TestCase):

    def test_collate_imgae(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_image_helper")
        img = os.path.join(temp, "..", "data")
        imgs = os.listdir(img)
        png = [os.path.join(img, _)
               for _ in imgs if os.path.splitext(_)[-1] == ".png" and "00" not in _]
        assert len(png) > 0
        out = os.path.join(temp, "out_collate.png")
        im = collate_images(png, out)
        assert os.path.exists(out)
        assert im is not None


if __name__ == "__main__":
    unittest.main()
