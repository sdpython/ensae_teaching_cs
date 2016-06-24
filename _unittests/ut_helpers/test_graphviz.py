"""
@brief      test log(time=2s)

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
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from src.ensae_teaching_cs.helpers.graphviz_helper import draw_graph_graphviz


class TestGraphviz(unittest.TestCase):

    def test_make_video(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            warnings.warn("graphviz is not available")
            return

        temp = get_temp_folder(__file__, "temp_graphviz")
        fout = os.path.join(temp, "image.png")

        out = draw_graph_graphviz([(1, "eee", "red")],
                                  [(1, 2, "blue"), (3, 4), (1, 3)], fout)

        fLOG(out)
        assert os.path.exists(fout)
        assert os.path.exists(fout + ".gv")


if __name__ == "__main__":
    unittest.main()
