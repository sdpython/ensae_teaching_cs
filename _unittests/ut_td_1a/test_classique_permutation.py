"""
@brief      test log(time=1s)
"""
import unittest
import itertools
from ensae_teaching_cs.td_1a.construction_classique import enumerate_permutations_recursive, enumerate_permutations


class TestClassiquesPermutation(unittest.TestCase):

    def test_permutation(self):
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
