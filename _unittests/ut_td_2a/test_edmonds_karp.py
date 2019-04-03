"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.td_2a import EdmondsKarpGraph


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
