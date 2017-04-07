"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest


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


class TestPythonnetVoiceListen(unittest.TestCase):

    def test_voice_listen(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no keys
            return

        if sys.platform.startswith("win") and __name__ == "__main__":
            from src.ensae_teaching_cs.pythonnet import vocal_recognition_listening

            try:
                for i, text in enumerate(vocal_recognition_listening()):
                    fLOG("listented", text)
                    if i >= 2:
                        break
            except Exception as e:
                if "Audio device error encountered" in str(e):
                    # maybe the script is running on a virtual machine (no
                    # Audia device)
                    if os.environ["USERNAME"] == "ensaestudent" or \
                       os.environ["USERNAME"] == "vsxavierdupre" or \
                       os.environ["USERNAME"] == "vsxavierdupre" or \
                       "DOUZE2016" in os.environ["COMPUTERNAME"] or \
                       os.environ["USERNAME"] == "appveyor" or \
                       "paris" in os.environ["COMPUTERNAME"].lower() or \
                       os.environ["USERNAME"].endswith("$"):  # anonymous Jenkins configuration
                        # I would prefer to catch a proper exception
                        # it just exclude one user only used on remotre
                        # machines
                        return
                raise Exception("USERNAME: " + os.environ.get("USERNAME", "-"))


if __name__ == "__main__":
    unittest.main()
