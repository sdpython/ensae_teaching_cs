# -*- coding: utf-8 -*-
"""
@brief      test log(time=2s)
"""
import os
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from ensae_teaching_cs.automation_students import enumerate_feedback, enumerate_send_email


class TestFeedback(ExtTestCase):

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
        df = pandas.read_excel(xls, sheet_name=0, engine='openpyxl')
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
                    raise Exception(f"EXP\n{exp[i]}\nRES\n{m[1]}")

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
        df = pandas.read_excel(xls, sheet_name=0, engine='openpyxl')
        try:
            mails = list(enumerate_send_email(mailbox, fr="me", col_name="Nom", cols=["Pitch", "Code"],
                                              df1=df, exc=False, fLOG=fLOG, delay_sending=True,
                                              begin="BEGIN", end="END", subject="SUBJECT"))
            self.assertNotEmpty(mails)
        except ValueError as e:
            if "mailbox is None" in str(e):
                pass
            else:
                raise e


if __name__ == "__main__":
    unittest.main()
