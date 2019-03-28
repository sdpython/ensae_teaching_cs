"""
@brief      test log(time=2s)
"""
import unittest
from ensae_teaching_cs.automation_students.quick_tasks import build_mailing_list


class TestQuickTasks(unittest.TestCase):

    def test_mail_build(self):
        names = ["DUPRE Xavier", "DU PRE Xav ier"]
        mails = build_mailing_list(names, domain="ensae.fr")
        self.assertEqual(
            mails, ['xavier.dupre@ensae.fr', 'xav.ier.du.pre@ensae.fr'])


if __name__ == "__main__":
    unittest.main()
