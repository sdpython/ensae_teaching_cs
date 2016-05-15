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
from pyquickhelper.loghelper import unzip
from src.ensae_teaching_cs.helpers.sound_helper import convert_music_file


class TestSoundHelper(unittest.TestCase):

    def test_convert_music_file(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_convert_music_file")
        data = os.path.join(temp, "..", "data")
        ffmpeg = os.path.join(data, "ffmpeg.zip")
        assert os.path.exists(ffmpeg)
        ff = unzip(ffmpeg, temp)
        mp3 = os.path.join(data, "podcasts_example.mp3")
        wav = os.path.join(temp, "podcasts_example.wav")

        convert_music_file(mp3, wav, ffmpeg=ff)
        assert os.path.exists(wav)
        assert os.stat(wav).st_size > 90000


if __name__ == "__main__":
    unittest.main()
