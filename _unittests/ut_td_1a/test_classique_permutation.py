"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import itertools


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
from src.ensae_teaching_cs.td_1a.construction_classique import enumerate_permutations_recursive, enumerate_permutations


class TestClassiquesPermutation (unittest.TestCase):

    def test_permutation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.maxDiff = None
        ens = list(range(5))
        lt = list(tuple(p) for p in enumerate_permutations_recursive(ens))
        self.assertEqual(len(lt), 120)
        res = list(tuple(p) for p in itertools.permutations(ens))
        self.assertEqual(len(res), 120)
        self.assertEqual(set(res), set(lt))
        res = list(tuple(p) for p in enumerate_permutations(ens))
        self.assertEqual(len(res), 120)
        self.assertEqual(set(res), set(lt))


if __name__ == "__main__":
    unittest.main()
