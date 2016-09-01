"""
@brief      test log(time=10s)

"""
import os
import sys
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


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, is_virtual_environment, run_base_script
from src.ensae_teaching_cs.helpers.video_helper import make_video


class TestVideoHelper(unittest.TestCase):

    def test_make_video(self):
        """
        This test does not work under a virtual environment.
        """
        fLOG(__file__, self._testMethodName, OutputPrint=True)

        if is_travis_or_appveyor() == "travis":
            warnings.warn("cv2 is not available")
            return

        if not is_virtual_environment():
            fLOG("running in base environment", sys.prefix)
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
        else:
            # we run it with the original interpreter
            fLOG("switch from virtual environment", sys.base_prefix)
            this = os.path.abspath(__file__)
            if sys.version_info[0] == 2:
                this = this.replace(".pyc", ".py")
            out = run_base_script(this, file=True, fLOG=fLOG)
            fLOG(out)


if __name__ == "__main__":
    unittest.main()
