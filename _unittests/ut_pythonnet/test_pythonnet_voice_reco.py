"""
@brief      test log(time=1s)
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

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor


class TestPythonnetVoiceReco(unittest.TestCase):

    def test_voice_reco(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        wav = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), "data", "output.wav")

        if is_travis_or_appveyor():
            # no keys
            return

        import keyring
        subkey = keyring.get_password(
            "cogser", os.environ["COMPUTERNAME"] + "voicereco")

        if subkey is None:
            warnings.warn("No available key for access Voice Recognition.")
            return

        if sys.platform.startswith("win"):
            from src.ensae_teaching_cs.pythonnet import vocal_recognition

            with open(wav, "rb") as f:
                content = f.read()

            res = vocal_recognition(subkey, memwav=content)
            fLOG(res)
            self.assertTrue(isinstance(res, dict))

            res = vocal_recognition(subkey, filename=wav)
            fLOG(res)
            self.assertTrue(isinstance(res, dict))
            for k, v in res.items():
                fLOG(k, v)
                if "results" == k:
                    for _ in v:
                        fLOG(_)


if __name__ == "__main__":
    unittest.main()
