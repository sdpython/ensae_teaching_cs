"""
@brief      test log(time=10s)

"""
import os
import sys
import warnings
import unittest
import pyquickhelper
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, is_virtual_environment, run_base_script, ExtTestCase


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


from src.ensae_teaching_cs.helpers.video_helper import make_video


context = {}


class TestVideoHelper(ExtTestCase):

    def test_make_video(self):
        """
        This test does not work under a virtual environment.
        """
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            warnings.warn("cv2 is not available")
            return

        if "--force" in context or not is_virtual_environment():
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
            if "--force" in context:
                fLOG("success")
        else:
            # We run it with the original interpreter.
            fLOG("switch from virtual environment", sys.base_prefix)
            fold = os.path.abspath(os.path.join(
                os.path.dirname(pyquickhelper.__file__), ".."))
            old_val = os.environ.get("PYTHONPATH", "")
            os.environ["PYTHONPATH"] = fold
            this = os.path.abspath(__file__)
            if sys.version_info[0] == 2:
                this = this.replace(".pyc", ".py")
            out = run_base_script(this, file=True, fLOG=fLOG, argv=["--force"])
            os.environ["PYTHONPATH"] = old_val
            if "success" not in out:
                raise Exception(
                    "CMD:\n{0}\nOUT:\n{1}\nPYTHONPATH={2}".format(os.path.split(__file__)[-1], out, fold))


if __name__ == "__main__":

    if "--force" in sys.argv:
        context["--force"] = True
        del sys.argv[sys.argv.index('--force')]

    unittest.main()
