"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase, is_travis_or_appveyor

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


class TestCodeStyle(ExtTestCase):
    """Test style."""

    def test_src(self):
        "skip pylint"
        self.assertFalse(src is None)

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))

        skip = ["do not assign a lambda expression, use a def",
                "too many leading '#' for block comment",
                "line too long (480 > 143",
                "Redefining name 'fLOG' from outer scope",
                "Unable to import 'System",
                "parallel_thread.py:39: R1710",
                "dice.py:51: W0612",
                "dice.py:47: W0612",
                "Redefining built-in 'format'",
                "Unused variable 'variance_a_eviter'",
                "Attribute 'objets' defined outside __init__",
                "Attribute 'sources' defined outside __init__",
                "Redefining built-in 'round'",
                "Redefining built-in 'iter'",
                "Unable to import 'ENSAE.",
                "Instance of '_TableFormulaStat' has no ",
                "Line too long (480/143)",
                "Unable to import 'MagicJupyter' (pylint)",
                "Unused variable 'n'",
                "Unused variable 'i'",
                "bad operand type for unary -: matrix",
                "No name 'AddReference' in module 'clr'",
                "Instance of 'TableFormula' has no 'table' member",
                "Unexpected keyword argument 'sheet' in function call",
                "Redefining built-in 'filter'",
                "Unused variable 'a'",
                "No name 'resize' in module 'cv2'",
                "No name 'imread' in module 'cv2'",
                "No name 'VideoWriter_fourcc' in module 'cv2'",
                "No name 'VideoWriter' in module 'cv2'",
                "'pygame' has no 'error' member",
                "'pygame' has no 'init' member",
                "Module 'matplotlib.cm' has no 'rainbow' member",
                "Redefining built-in 'input'",
                "Unused variable 'vt'",
                "Value 'lastrow' is unsubscriptable",
                "tsp_bresenham.py:9: R1710",
                "Redefining built-in 'next'",
                "Attribute '__dict__' defined outside __init__",
                "Instance of 'Rule' has no 'clauses' member",
                "Instance of 'LatexCode' has no 'replace' member",
                "filename_helper.py:68: E1136",
                "coding_party1_velib.py:331: W0612",
                "send_feedback.py:287: W0640",
                "send_feedback.py:286: W0640",
                "send_feedback.py:135: W0640",
                "send_feedback.py:135: W0631",
                "send_feedback.py:26",
                "projects_helper.py:16: W0102",
                "mail_helper.py:79: W0102",
                "jenkins_helper.py:142: W0102",
                "ftp_publish_helper.py:197: W0102",
                "pandas_helper.py:8: W0611",
                "coding_party1_velib.py:239: W0612",
                "ftp_publish_helper.py:196: W0102",
                "pandas_helper.py:7: W0611",
                "table_formula.py:2702: W0612",
                "ftp_publish_helper.py:246: E0401",
                "ftp_publish_helper.py:138: E0401",
                "Unable to import 'pycuda",
                "Unable to import 'pyopencl'",
                "Unable to import 'selenium",
                "Unable to import 'splinter'",
                "Unable to import 'ensae_teaching_cs.td_1a.flask_helper'",
                "Unused import clr",
                "Module 'clr' has no 'AddReference' member",
                "Unable to import 'clr'",
                "send_feedback.py:292: E0602",
                "send_feedback.py:137: W0631",
                "send_feedback.py:137: W0640",
                ]

        if is_travis_or_appveyor() == "appveyor":
            skip.extend(["Unable to import 'fairtest'"])

        check_pep8(src_, fLOG=fLOG, skip=skip,
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'R1702', 'C0200', 'W0703', 'W0223',
                                  'W020', 'W0212', 'C0123', 'C0302', 'W0221',
                                  'R0912', 'E0203', 'W0201', 'R1710', 'W0603',
                                  'R1711', 'R1714'))

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        skip = ["src' imported but unused",
                "skip_' imported but unused",
                "skip__' imported but unused",
                "skip___' imported but unused",
                "Unused variable 'skip_'",
                "imported as skip_",
                "Unused import src",
                "Module 'pygame' has no 'init' member",
                "Module 'pygame' has no 'NOFRAME' member",
                "Class 'mem_flags' has no ",
                "Module 'torch' has no ",
                "Module 'numpy.random' has no 'RandomState' ",
                "Unable to import 'onemod' ",
                "Redefining built-in 'filter' ",
                "Redefining built-in 'input'",
                "Unused variable 'n'",
                "Redefining name 'path' from outer scope",
                "Unused variable 'i'",
                "Unable to import 'System",
                "Module 'src.ensae_teaching_cs.pythonnet.",
                "Unused variable 'skip___'",
                "Module 'pygame' has no 'quit'",
                "Unable to import 'primes'",
                "Parameters differ from overridden 'forward' method",
                "test_data_competition.py:3",
                "test_data_competition.py:1",
                "Redefining name 'src' from outer scope",
                "Unable to import 'pycuda.",
                "Unable to import 'pyopencl'",
                "Unused import clr",
                "Unused variable 'clr'",
                "Unable to import 'clr'",
                "Module 'clr' has no 'AddReference' member",
                "test_SKIP_torch.py:67: E1123",
                "test_SKIP_torch.py:102: E1101",
                "test_SKIP_torch.py:104: E1101",
                ]

        if is_travis_or_appveyor() == "appveyor":
            skip.extend(["Unable to import 'fairtest'"])

        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*", skip=skip,
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'C0200', 'C0122', "W0123", 'W0703',
                                  'W0212', 'W0201', 'R1711', 'R1714'))


if __name__ == "__main__":
    unittest.main()
