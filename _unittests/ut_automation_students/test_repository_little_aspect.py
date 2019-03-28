"""
@brief      test log(time=2s)
"""
import unittest
from ensae_teaching_cs.automation_students import ProjectsRepository


class TestRepositoryLittleAspect(unittest.TestCase):

    def test_regular_expression(self):
        text = """<br /></div>
                    <div><div dir="ltr">Pourriez-vous vous ajouter sur le doodle suivant ?<div><br></div><div>
                    <p style="margin:0in;font-family:Calibri;font-size:11pt" lang="fr">
                    <a href="http://doodle.com/poll/xxxxxxxxc9w8">http://doodle.com/poll/xxxxxxsyz7c9w8</a></p></div></div><div class
                    """
        f = ProjectsRepository._link_regex.findall(text)
        self.assertEqual(len(f), 2)
        self.assertEqual(f[0], "http://doodle.com/poll/xxxxxxxxc9w8")


if __name__ == "__main__":
    unittest.main()
