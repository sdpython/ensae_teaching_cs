"""
@brief      test log(time=10s)

"""
import os
import unittest
from ensae_teaching_cs.helpers import enumerate_inspect_source_code


class TestCodeHelper(unittest.TestCase):

    def test_size_object_in_folder(self):
        folder = os.path.abspath(os.path.dirname(__file__))
        patterns = "from ensae_teaching_cs[._a-zA-Z0-9]* import ([a-zA-Z0-9_]+)"
        res = []
        nb = 0
        for obs in enumerate_inspect_source_code(folder, line_patterns=patterns):
            res.append(obs)
            if obs['group'] == "enumerate_inspect_source_code":
                nb += 1
        self.assertGreater(len(res), 0)
        self.assertEqual(nb, 1)


if __name__ == "__main__":
    unittest.main()
