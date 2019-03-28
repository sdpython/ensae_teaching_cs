"""
@brief      test log(time=3s)
"""
import os
import unittest
import warnings
import pandas
with warnings.catch_warnings():
    warnings.simplefilter('ignore', DeprecationWarning)
    import keyring
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.filehelper import zip_files
from ensae_teaching_cs.data.crypt_helper import encrypt_data, decrypt_data
from ensae_teaching_cs.data.datacpt import data_cpt_ENSAE_2016_11, data_cpt_ENSAE_2016_11_blind_set
from ensae_teaching_cs.ml.competitions import AUC


class TestCompetition(unittest.TestCase):

    def test_crypt_helper(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_crypt")

        input = os.path.abspath(__file__.replace(".pyc", ".py"))
        output = os.path.join(temp, "crypted.bin")
        output2 = os.path.join(temp, "decrypted.txt")
        key = "01" * 8
        encrypt_data(key, input, output)
        decrypt_data(key, output, output2)
        with open(input, "r") as f:
            t1 = f.read()
        with open(output2, "r") as f:
            t2 = f.read()
        self.assertEqual(t1, t2)
        assert len(t1) > 0

    def test_ensae_2016(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_cpt_ensae_2016")
        r = data_cpt_ENSAE_2016_11(folder=temp, fLOG=fLOG)
        self.assertEqual(len(r), 2)
        assert isinstance(r[0], pandas.DataFrame)
        assert isinstance(r[1], pandas.DataFrame)
        self.assertEqual(r[0].shape, (22500, 24))
        self.assertEqual(r[1].shape, (7500, 23))

    def test_ensae_2016_answers(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no stored password
            return
        password = keyring.get_password(
            "cpt", "ensae_teaching_cs,pwd")
        r = data_cpt_ENSAE_2016_11_blind_set(password)
        self.assertEqual(len(r), 7500)
        truth = r

        r = data_cpt_ENSAE_2016_11_blind_set("dummy")
        self.assertEqual(len(r), 7500)
        s = sum(r)
        assert 0 <= s <= len(r)
        auc = AUC(truth, r)
        fLOG(auc)
        assert 0 <= auc <= 1

        temp = get_temp_folder(__file__, "temp_cpt_ensae_2016_answers")
        out = os.path.join(temp, "answer.txt")
        with open(out, "w") as f:
            f.write("\n".join(str(_) for _ in r))
        zip_files(os.path.join("submission.zip"), [out])


if __name__ == "__main__":
    unittest.main()
