"""
@brief      test log(time=6s)
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


class TestModulesTheano(unittest.TestCase):

    def test_theano(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        if not is_travis_or_appveyor():
            fLOG("import theano")
            this = os.path.abspath(os.path.join(os.path.dirname(
                sys.executable), "Library", "mingw-w64", "bin"))
            if os.path.exists(this) and this not in os.environ["PATH"]:
                # Should not be needed unless the location is different.
                # os.environ["PATH"] += ";" + this
                pass
            else:
                fLOG("[warning] '{0}' does not exist".format(loc))

            import theano
            # if you see the following warning
            # WARNING (theano.configdefaults): g++ not detected !
            # Theano will be unable to execute optimized C-implementations
            # (for both CPU and GPU) and will default to Python implementations.
            # Performance will be severely degraded. To remove this warning,
            # set Theano flags cxx to an empty string.
            # you should install TDM-GCC or
            # http://mingw-w64.org/doku.php/start (more recent updates)
            # https://sourceforge.net/projects/mingw-w64/files/?source=navbar
            # choose x86_64 + posix + seh
            #
            # With Anaconda: conda install m2w64-toolchain
            # See http://deeplearning.net/software/theano/install_windows.html#install-requirements-and-optional-packages
            #
            # If not present, you should copy g++ into
            # mingw_w64_gcc = os.path.join(os.path.dirname(sys.executable), "Library", "mingw-w64", "bin", "g++")
            # And you add the path to the compiler into PATH
            #
            # error with hypot
            # https://stackoverflow.com/questions/38536788/g-error-on-import-of-theano-on-windows-7
            self.assertTrue(theano is not None)

            dirgcc = os.path.dirname(theano.configdefaults.mingw_w64_gcc)
            if not os.path.exists(dirgcc):
                fLOG("[warning] '{0}' does not exist".format(dirgcc))

            if False:
                rows = []
                for k in sorted(dir(theano.configdefaults)):
                    if hasattr(theano.configdefaults, k):
                        rows.append("{0}={1}".format(
                            k, getattr(theano.configdefaults, k)))
                fLOG("\n" + "\n".join(rows))


if __name__ == "__main__":
    unittest.main()
