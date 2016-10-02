"""
@brief      test log(time=2s)
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
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.ml.competitions import AUC, private_codalab_wrapper


class TestCompetitions(unittest.TestCase):

    def test_auc(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        ans = [1, 1, 1, 1, 1, 0, 0, 0, 0]
        score = [i * 0.8 + 0.1 for i in ans]
        a = AUC(ans, score)
        self.assertEqual(a, 1)
        score = [-i * 0.8 - 0.1 for i in ans]
        a = AUC(ans, score)
        self.assertEqual(a, 0)
        score = [i * 0.8 + 0.1 for i in ans]
        score[0] = 0.4
        score[-1] = 0.6
        a = AUC(ans, score)
        self.assertEqual(a, 0.95)

    def test_auc_file(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        ans = [1, 1, 1, 1, 1, 0, 0, 0, 0]
        score = [i * 0.8 + 0.1 for i in ans]
        score[0] = 0.4
        score[-1] = 0.6
        fLOG(score)
        t1 = get_temp_folder(__file__, "temp_answers")
        t2 = get_temp_folder(__file__, "temp_scores")
        f1 = "answer.txt"
        f2 = "answer.txt"
        fu1 = os.path.join(t1, f1)
        fu2 = os.path.join(t2, f2)
        out = os.path.join(t2, "scores.txt")
        with open(fu1, "w") as f:
            f.write("\n".join(str(_) for _ in ans))
        with open(fu2, "w") as f:
            f.write("\n".join(str(_) for _ in score))
        private_codalab_wrapper(AUC, "AUC", t1, t2, output=out)
        assert os.path.exists(out)
        with open(out, "r") as f:
            code = f.read()
        fLOG("**", code)
        self.assertEqual(code, "AUC:0.95")


if __name__ == "__main__":
    unittest.main()
