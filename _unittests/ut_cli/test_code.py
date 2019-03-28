"""
@brief      test tree node (time=7s)
"""
import os
import unittest
from io import StringIO
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.__main__ import main


class TempBuffer:
    "simple buffer"

    def __init__(self):
        "constructor"
        self.buffer = StringIO()

    def fprint(self, *args, **kwargs):  # pylint: disable=W0613
        "print function"
        mes = " ".join(str(_) for _ in args)
        self.buffer.write(mes)
        self.buffer.write("\n")

    def __str__(self):
        "usual"
        return self.buffer.getvalue()


class TestCodeCli(ExtTestCase):

    def test_inspect(self):
        st = TempBuffer()
        main(args=[], fLOG=st.fprint)
        res = str(st)
        self.assertIn("python -m ensae_teaching_cs <command>", res)
        self.assertIn("Counts groups extracted", res)

    def test_inspect_help(self):
        st = TempBuffer()
        main(args="inspect_source_code --help".split(), fLOG=st.fprint)
        res = str(st)
        self.assertIn("Counts groups extracted", res)

    def test_inspect_code(self):
        fold = os.path.abspath(os.path.dirname(__file__))
        exp = 'import ([a-zA-Z0-9_]+)'
        st = TempBuffer()
        main(args=['inspect_source_code', '-f',
                   fold, '-l', exp], fLOG=st.fprint)
        res = str(st)
        self.assertStartsWith("group,line,name,patid", res)


if __name__ == "__main__":
    unittest.main()
