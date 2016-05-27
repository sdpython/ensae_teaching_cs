"""
@brief      test log(time=4s)

"""
import os
import sys
import unittest
import random


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
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from src.ensae_teaching_cs.helpers.matplotlib_helper_xyz import scatter_xy_id, scatter_xyc, scatter_xyz
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams


class TestMatplotlibHelperVizScatterPlots (unittest.TestCase):

    backend = rcParams["backend"]

    def generate_gauss(self, x, y, sigma, N=1000):
        res = []
        for i in range(N):
            u = random.gauss(0, 1)
            a = sigma * u + x
            b = sigma * random.gauss(0, 1) + y + u
            res.append((a, b))
        return res

    def test_viz_scatter_scatter_xyid(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv()
        if __name__ == "__main__":
            rcParams["backend"] = "TkAgg"
        fold = os.path.abspath(os.path.split(__file__)[0])
        fold = os.path.join(fold, "temp_graph_xyz")
        im = os.path.join(fold, self._testMethodName + ".png")
        if not os.path.exists(fold):
            os.mkdir(fold)
        for img in [im]:
            if os.path.exists(img):
                os.remove(img)

        nuage1 = self.generate_gauss(0, 0, 3)
        nuage2 = self.generate_gauss(3, 4, 2)
        nuage = [(a, b, 0) for a, b in nuage1] + [(a, b, 1) for a, b in nuage2]

        matplotlib.use(matplotlib.get_backend(), warn=False, force=True)

        fig, ax = scatter_xy_id(
            nuage, title=self._testMethodName, legend={0: "c0", 1: "c1"})
        fig.savefig(im)
        assert os.path.exists(im)
        if __name__ == "__main__":
            rcParams["backend"] = TestMatplotlibHelperVizScatterPlots.backend
        plt.close('all')
        fLOG(plt.style.available)
        # ['seaborn-bright', 'ggplot', 'seaborn-paper', 'seaborn-dark-palette', 'seaborn-dark',
        # 'seaborn-ticks', 'seaborn-notebook', 'seaborn-white', 'seaborn-poster', 'classic',
        # 'bmh', 'seaborn-talk', 'seaborn-pastel', 'seaborn-whitegrid', 'dark_background',
        # 'seaborn-deep', 'grayscale', 'seaborn-muted', 'fivethirtyeight', 'seaborn-darkgrid', 'seaborn-colorblind']

    def test_viz_scatter_scatter_xyc(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv()
        if __name__ == "__main__":
            rcParams["backend"] = "TkAgg"
        fold = os.path.abspath(os.path.split(__file__)[0])
        fold = os.path.join(fold, "temp_graph_xyz")
        im = os.path.join(fold, self._testMethodName + ".png")
        if not os.path.exists(fold):
            os.mkdir(fold)
        for img in [im]:
            if os.path.exists(img):
                os.remove(img)

        def f(a, b):
            return (a ** 2 + b ** 2) ** 0.5

        nuage1 = self.generate_gauss(0, 0, 3)
        nuage2 = self.generate_gauss(3, 4, 2)
        nuage = [(a, b, f(a, b)) for a, b in nuage1] + \
            [(a, b, f(a, b)) for a, b in nuage2]

        matplotlib.use(matplotlib.get_backend(), warn=False, force=True)

        fig, ax = scatter_xyc(nuage, title=self._testMethodName)
        fig.savefig(im)
        assert os.path.exists(im)

        fig, ax = scatter_xyc(
            nuage, smooth=1, title=self._testMethodName + " - smooth 10")
        fig.savefig(im.replace(".png", ".s10.png"))
        assert os.path.exists(im)
        if __name__ == "__main__":
            rcParams["backend"] = TestMatplotlibHelperVizScatterPlots.backend
        plt.close('all')

    def test_viz_scatter_scatter_xyz(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv()
        if __name__ == "__main__":
            rcParams["backend"] = "TkAgg"
        fold = os.path.abspath(os.path.split(__file__)[0])
        fold = os.path.join(fold, "temp_graph_xyz")
        im = os.path.join(fold, self._testMethodName + ".png")
        if not os.path.exists(fold):
            os.mkdir(fold)
        for img in [im]:
            if os.path.exists(img):
                os.remove(img)

        def f(a, b):
            return (a ** 2 + b ** 2) ** 0.5

        nuage1 = self.generate_gauss(0, 0, 3)
        nuage2 = self.generate_gauss(3, 4, 2)
        nuage = [(a, b, f(a, b)) for a, b in nuage1] + \
            [(a, b, f(a, b)) for a, b in nuage2]

        matplotlib.use(matplotlib.get_backend(), warn=False, force=True)

        fig, ax = scatter_xyz(nuage, title=self._testMethodName)
        fig.savefig(im)
        assert os.path.exists(im)

        fig, ax = scatter_xyz(
            nuage, smooth=2, title=self._testMethodName + " - smooth 10")
        fig.savefig(im.replace(".png", ".s10.png"))
        assert os.path.exists(im)
        if __name__ == "__main__":
            rcParams["backend"] = TestMatplotlibHelperVizScatterPlots.backend
        plt.close('all')


if __name__ == "__main__":
    unittest.main()
