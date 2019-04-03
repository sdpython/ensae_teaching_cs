"""
@brief      test log(time=10s)

"""
import unittest
from ensae_teaching_cs.helpers.size_helper import total_size, object_size


class TestSizeHelper(unittest.TestCase):

    def test_size_object(self):
        mat = [[1, 0, 0],
               [0, 4, 0],
               [1, 2, 3]]

        s1 = object_size(mat)
        s2 = total_size(mat)
        assert s1 < s2


if __name__ == "__main__":
    unittest.main()
