"""
@brief      test log(time=21s)
"""
import os
import unittest
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.td_1a.discours_politique import enumerate_speeches_from_elysees


class TestRetrieveSpeeches(ExtTestCase):

    def test_retrieve_speeches(self):
        temp = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "temp_speeches"))
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            f = os.path.join(temp, _)
            if os.path.isfile(f):
                os.remove(f)

        i = 0
        url = "agenda-decembre-2018"
        for i, disc in enumerate(enumerate_speeches_from_elysees(url=url)):
            if i >= 2:
                break
            self.assertNotEmpty(disc)
        self.assertGreater(i, 1)


if __name__ == "__main__":
    unittest.main()
