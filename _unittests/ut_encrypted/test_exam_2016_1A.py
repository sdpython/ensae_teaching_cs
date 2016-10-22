"""
@brief      test log(time=3s)
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

try:
    import pyensae as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae as skip__

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.filehelper import get_url_content_timeout
from pyquickhelper.filehelper import encrypt_stream, decrypt_stream
from src.ensae_teaching_cs import __file__ as module_file


class TestExam20161A(unittest.TestCase):

    def test_hash(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def get_code(mail):
            import hashlib
            m = hashlib.md5()
            m.update(mail)
            b = m.digest()
            return int(b[0])

        for bbb in [b"a", b"a@a", b"any@ensae.fr", b"ensae.frs"]:
            code = get_code(bbb)
            url = "http://www.xavierdupre.fr/enseignement/examens/1A_2016/enonce_%d.txt" % code
            content = get_url_content_timeout(url)
            assert 0 <= code <= 255
            assert len(content) > 0

    def test_crypt_file(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no password
            return

        import keyring
        this = os.path.abspath(os.path.dirname(module_file))
        dst = os.path.join(this, "encrypted", "cryptcode_exam_2016.crypted")
        if not os.path.exists(dst) or os.stat(dst).st_size < 10:
            fLOG("crypt")
            pwd = keyring.get_password(
                "exam", os.environ["COMPUTERNAME"] + "key")
            pwd += "*" * (16 - len(pwd))
            pwd = pwd.encode("ascii")
            fLOG(type(pwd))
            this = os.path.join(this, "cryptcode.py")
            assert os.path.exists(this)
            encrypt_stream(pwd, this, dst)
            fLOG(os.stat(dst).st_size)

    def test_import_exam(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no password
            return

        import keyring
        temp = get_temp_folder(__file__, "temp_import_exam")
        pwd = keyring.get_password("exam", os.environ["COMPUTERNAME"] + "key")
        pwd += "*" * (16 - len(pwd))
        pwd = pwd.encode("ascii")
        this = os.path.abspath(os.path.dirname(module_file))
        dst = os.path.join(this, "encrypted", "cryptcode_exam_2016.crypted")
        assert os.path.exists(dst)
        decr = os.path.join(temp, "onemod.py")
        decrypt_stream(pwd, dst, decr)
        assert os.path.exists(decr)
        fLOG("importing")
        sys.path.append(temp)
        import onemod as temp_module
        del sys.path[-1]
        answer = temp_module.build(120)
        exp = """***      H
                H ***    H
                ***      H
                ***      H
                H ***    H
                ***      H
                ***      H
                H ***    H
                ***      H
                ***      H
                H ***    H
                ***      H""".replace("                ", "")
        self.assertEqual(answer, exp)

    def test_crypt_file_vigenere(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no password
            return

        from src.ensae_teaching_cs.td_1a.vigenere import code_vigenere

        import keyring
        this = os.path.abspath(os.path.dirname(module_file))
        dst = os.path.join(this, "encrypted", "cryptcode_exam_2016.vigenere")
        if not os.path.exists(dst) or os.stat(dst).st_size < 10:
            fLOG("crypt")
            pwd = keyring.get_password(
                "exam", os.environ["COMPUTERNAME"] + "key")
            pwd = pwd.encode("ascii")
            this = os.path.join(this, "cryptcode.py")
            assert os.path.exists(this)
            with open(this, "rb") as f:
                content = f.read()
            code = code_vigenere(content, pwd, binary=True)
            with open(dst, "wb") as f:
                f.write(code)

    def test_import_exam_vigenere(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no password
            return

        from src.ensae_teaching_cs.td_1a.vigenere import code_vigenere

        import keyring
        temp = get_temp_folder(__file__, "temp_import_exam_vigenere")
        pwd = keyring.get_password("exam", os.environ["COMPUTERNAME"] + "key")
        pwd = pwd.encode("ascii")
        this = os.path.abspath(os.path.dirname(module_file))
        dst = os.path.join(this, "encrypted", "cryptcode_exam_2016.vigenere")
        assert os.path.exists(dst)
        with open(dst, "rb") as f:
            content = f.read()
        content = code_vigenere(content, pwd, binary=True, decode=True)
        decr = os.path.join(temp, "onemod_vigenere.py")
        with open(decr, "wb") as f:
            f.write(content)
        assert os.path.exists(decr)
        fLOG("importing")
        sys.path.append(temp)
        import onemod as temp_module
        del sys.path[-1]
        answer = temp_module.build(120)
        exp = """***      H
                H ***    H
                ***      H
                ***      H
                H ***    H
                ***      H
                ***      H
                H ***    H
                ***      H
                ***      H
                H ***    H
                ***      H""".replace("                ", "")
        self.assertEqual(answer, exp)


if __name__ == "__main__":
    unittest.main()
