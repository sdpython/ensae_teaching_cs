"""
@brief      test log(time=10s)

"""
import os
import sys
import warnings
import unittest
import pyquickhelper
from pyquickhelper.pycode import get_temp_folder, skipif_travis, is_virtual_environment, run_base_script, ExtTestCase
from ensae_teaching_cs.helpers.video_helper import make_video


context = {}


class TestVideoHelper(ExtTestCase):

    @skipif_travis("cv2 is not available")
    def test_make_video(self):
        """
        This test does not work under a virtual environment.
        """
        temp = get_temp_folder(__file__, "temp_make_video")
        img = os.path.join(temp, "..", "data")
        imgs = os.listdir(img)
        png = [os.path.join(img, _)
               for _ in imgs if os.path.splitext(_)[-1] == ".png" and "00" in _]
        assert len(png) > 0
        out = os.path.join(temp, "out_video.avi")

        v = make_video(png, out, size=(1000, 300))
        assert os.path.exists(out)
        assert os.stat(out).st_size > 90000
        assert v is not None


if __name__ == "__main__":
    unittest.main()
