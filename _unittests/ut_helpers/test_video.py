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
from src.ensae_teaching_cs.helpers.video_helper import make_video


class TestVideo(unittest.TestCase):

    def test_make_video(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_make_video")
        img = os.path.join(temp, "..", "data")
        imgs = os.listdir(img)
        png = [os.path.join(img, _)
               for _ in imgs if os.path.splitext(_)[-1] == ".png"]
        assert len(png) > 0
        out = os.path.join(temp, "out_video.avi")
        v = make_video(png, out, size=(1000, 300))
        assert os.path.exists(out)
        assert os.stat(out).st_size > 90000
        assert v is not None

if __name__ == "__main__":
    unittest.main()
