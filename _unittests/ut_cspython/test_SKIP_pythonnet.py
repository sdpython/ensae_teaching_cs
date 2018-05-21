# -*- coding: utf-8 -*-
"""
@brief      test log(time=3s)
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


class TestSKIPPythonnet(unittest.TestCase):

    def test_voice(self):
        if sys.platform.startswith("win"):
            import clr
            from src.ensae_teaching_cs.cspython import vocal_synthesis
            try:
                vocal_synthesis("test unitaire")
            except Exception as e:
                if "Audio device error encountered" in str(e) or \
                        "Erreur de périphérique audio rencontrée" in str(e):
                    # maybe the script is running on a virtual machine (no
                    # Audia device)
                    if os.environ["USERNAME"] == "ensaestudent" or \
                       os.environ["USERNAME"] == "vsxavierdupre" or \
                       os.environ["USERNAME"] == "vsxavierdupre" or \
                       "DOUZE2016" in os.environ["COMPUTERNAME"] or \
                       "ENSAE" in os.environ["COMPUTERNAME"] or \
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
