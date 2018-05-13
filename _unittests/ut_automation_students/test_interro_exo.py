"""
@brief      test log(time=2s)
"""
import os
import sys
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version

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


class TestInterroExo(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    def test_interro_motif(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.ensae_teaching_cs.automation_students.interro_motif import execute_python_scripts, _get_code
        code = _get_code(b"aa.bb@ensae-paristech.fr")
        self.assertEqual(code, 51)

        temp = get_temp_folder(__file__, "temp_interro_motif")
        data = os.path.join(temp, "..", "projects", "exo_1A_2016.xlsx")
        root = os.path.join(temp, "..", "projects")
        input = pandas.read_excel(data)
        url = "http://www.xavierdupre.fr/enseignement/examens/1A_2016/enonce_{0}.txt"
        col_names = dict(folder="nom_prenom", mail="nom_prenom")
        df = execute_python_scripts(
            root, input, col_names=col_names, url=url, fLOG=fLOG, eol="/")
        out = os.path.join(temp, "results.xlsx")
        df.to_excel(out)
        assert os.path.exists(out)


if __name__ == "__main__":
    unittest.main()
