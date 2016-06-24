"""
@brief      test log(time=10s)

"""
import os
import sys
import unittest
import warnings


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
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from src.ensae_teaching_cs.special.corde import pygame_simulation
from src.ensae_teaching_cs.helpers.video_helper import make_video


class TestCorde(unittest.TestCase):

    def test_image_video_corde(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_image_video_corde")

        if is_travis_or_appveyor() == "travis":
            warnings.warn("pygame is not available")
            return

        import pygame
        pygame_simulation(pygame, fLOG=fLOG,
                          iter=2000 if __name__ == "__main__" else 100,
                          folder=temp)
        files = os.listdir(temp)
        assert len(files) > 9
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        assert len(png) > 0
        out = os.path.join(temp, "corde.avi")

        v = make_video(png, out, size=(400, 300), format="XVID", fps=24)
        assert v is not None


if __name__ == "__main__":
    unittest.main()
