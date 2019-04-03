"""
@brief      test log(time=3s)
"""
import sys
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from ensae_teaching_cs.faq import graph_with_label


class TestGraphWithLabel(unittest.TestCase):

    def test_graph_with_label(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        x = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43]
        y = [
            1,
            3,
            10,
            6,
            3,
            5,
            3,
            6,
            4,
            2,
            3,
            2,
            11,
            10,
            4,
            5,
            2,
            5,
            4,
            1,
            1,
            1,
            3,
            15,
            5,
            2,
            1,
            5,
            3,
            1,
            3,
            2,
            4,
            5,
            2,
            12,
            12,
            5,
            11,
            2,
            19,
            21,
            5,
            2]
        xl = [
            '2014-w04',
            '2014-w05',
            '2014-w06',
            '2014-w07',
            '2014-w08',
            '2014-w09',
            '2014-w10',
            '2014-w11',
            '2014-w12',
            '2014-w13',
            '2014-w14',
            '2014-w15',
            '2014-w16',
            '2014-w17',
            '2014-w18',
            '2014-w19',
            '2014-w20',
            '2014-w21',
            '2014-w22',
            '2014-w23',
            '2014-w24',
            '2014-w25',
            '2014-w27',
            '2014-w29',
            '2014-w30',
            '2014-w31',
            '2014-w32',
            '2014-w34',
            '2014-w35',
            '2014-w36',
            '2014-w38',
            '2014-w39',
            '2014-w41',
            '2014-w42',
            '2014-w43',
            '2014-w44',
            '2014-w45',
            '2014-w46',
            '2014-w47',
            '2014-w48',
            '2014-w49',
            '2014-w50',
            '2014-w51',
            '2014-w52']
        if sys.version_info[:2] <= (3, 4):
            warnings.warn(
                "Issue with Python 3.4, bug probably related to wrong pointers")
            return
        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        import matplotlib.pyplot as plt
        _, ax = plt.subplots(figsize=(8, 3))
        graph_with_label(x, y, xl, ax=ax)
        if __name__ == "__main__":
            plt.show()
        plt.close('all')
        fLOG("end")


if __name__ == "__main__":
    unittest.main()
