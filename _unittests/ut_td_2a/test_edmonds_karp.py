"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
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
from pyquickhelper.pycode import ExtTestCase
from src.ensae_teaching_cs.td_2a import EdmondsKarpGraph


class TestEdmondsKarp(ExtTestCase):

    def test_simple_graph(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        graph = EdmondsKarpGraph([(1, 2, 1), (2, 3, 1)])
        res = graph.edmonds_karp(1, 3)
        self.assertEqual(res, 1)

        graph = EdmondsKarpGraph([(1, 2, 2), (2, 3, 1), (3, 4, 1), (1, 4, 1)])
        res = graph.edmonds_karp(1, 4)
        self.assertEqual(res, 2)

        graph = EdmondsKarpGraph([(1, 2, 2), (2, 3, 1), (1, 4, 1)])
        res = graph.edmonds_karp(1, 4)
        self.assertEqual(res, 1)

        graph = EdmondsKarpGraph([(1, 2, 2), (3, 4, 1)])
        self.assertRaise(lambda: graph.edmonds_karp(1, 4), ValueError)


if __name__ == "__main__":
    unittest.main()
