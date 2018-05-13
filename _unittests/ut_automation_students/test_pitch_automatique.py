# -*- coding: utf-8 -*-
"""
@brief      test log(time=2s)
"""
import sys
import os
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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

from src.ensae_teaching_cs.automation_students import enumerate_feedback, enumerate_send_email


class TestFeedback(unittest.TestCase):

    def test_enumerate_feedback(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        exp = [
            "<p>ok</p>",
        ]

        temp = get_temp_folder(__file__, "temp_enumerate_feedback")
        data = os.path.abspath(os.path.dirname(__file__))
        data = os.path.join(data, "data")
        xls = os.path.join(data, "groupes_eleves_pitch.xlsx")
        df = pandas.read_excel(xls, sheetname=0, index=False)
        mails = list(enumerate_feedback(df, exc=False, fLOG=fLOG,
                                        begin="BEGIN", end="END", subject="SUBJECT",
                                        col_name="Nom", cols=["Pitch", "Code"]))
        for i, m in enumerate(mails):
            fLOG("------------", i)
            name = os.path.join(temp, "m%d.html" % i)
            with open(name, "w", encoding="utf-8") as f:
                f.write(m[1])
            if i < len(exp):
                if exp[i] not in m[1]:
                    raise Exception("EXP\n{0}\nRES\n{1}".format(exp[i], m[1]))

    def test_enumerate_send_email(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.dirname(__file__))
        data = os.path.join(data, "data")
        xls = os.path.join(data, "groupes_eleves_pitch.xlsx")
        # pymmails.sender.create_smtp_server("gmail", login, pwd)
        mailbox = None
        df = pandas.read_excel(xls, sheetname=0, index=False)
        try:
            mails = list(enumerate_send_email(mailbox, fr="me", col_name="Nom", cols=["Pitch", "Code"],
                                              df1=df, exc=False, fLOG=fLOG, delay_sending=True,
                                              begin="BEGIN", end="END", subject="SUBJECT"))
            assert mails is not None
        except ValueError as e:
            if "mailbox is None" in str(e):
                pass
            else:
                raise e


if __name__ == "__main__":
    unittest.main()
