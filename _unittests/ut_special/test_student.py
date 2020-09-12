"""
@brief      test log(time=2s)

"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.special.student import Student


class TestStudent(ExtTestCase):

    def test_student(self):
        qna = {'q1': 0.6}
        st = repr(Student(qna))
        self.assertEqual(st, "Student({'q1': 0.6})")

    def test_correlate_answers(self):
        qna = {'q1': 0.6, 'q2': 0.7, 'q3': 0.1}
        st = Student(qna)
        mat = st.count_anwers()
        self.assertEqual(mat, {('q1', 'q2'): {(True, True): 1},
                               ('q1', 'q3'): {(True, False): 1},
                               ('q2', 'q1'): {(True, True): 1},
                               ('q2', 'q3'): {(True, False): 1},
                               ('q3', 'q1'): {(False, True): 1},
                               ('q3', 'q2'): {(False, True): 1}})

    def test_correlate_answers_matrix(self):
        qna = {'q1': 0.6, 'q2': 0.7, 'q3': 0.1}
        st = Student(qna)
        names, mat = st.count_anwers_matrix()
        expected = [[[1., 1., 0.],
                     [1., 1., 0.],
                     [0., 0., 0.]],
                    [[0., 0., 1.],
                     [0., 0., 1.],
                     [0., 0., 0.]],
                    [[0., 0., 0.],
                     [0., 0., 0.],
                     [1., 1., 0.]],
                    [[0., 0., 0.],
                     [0., 0., 0.],
                     [0., 0., 1.]]]
        self.assertEqual(mat.tolist(), expected)
        self.assertEqual(names, {'q1': 0, 'q2': 1, 'q3': 2})

    def test_correlate_answers2_matrix(self):
        st1 = Student({'q1': 0.6, 'q2': 0.7, 'q3': 0.1})
        st2 = Student({'q1': 0.6, 'q2': 0.2, 'q3': 0.1})
        mat = st1.count_anwers()
        self.assertEqual(mat, {('q1', 'q2'): {(True, True): 1},
                               ('q1', 'q3'): {(True, False): 1},
                               ('q2', 'q1'): {(True, True): 1},
                               ('q2', 'q3'): {(True, False): 1},
                               ('q3', 'q1'): {(False, True): 1},
                               ('q3', 'q2'): {(False, True): 1}})
        st2.count_anwers(counter=mat)
        expected = {('q1', 'q2'): {(True, True): 1, (True, False): 1},
                    ('q1', 'q3'): {(True, False): 2},
                    ('q2', 'q1'): {(True, True): 1, (False, True): 1},
                    ('q2', 'q3'): {(True, False): 1, (False, False): 1},
                    ('q3', 'q1'): {(False, True): 2},
                    ('q3', 'q2'): {(False, True): 1, (False, False): 1}}
        self.assertEqual(mat, expected)
        mat2 = None
        for st in [st1, st2]:
            mat2 = st.count_anwers(counter=mat2)
        self.assertEqual(mat2, expected)

    def test_correlate_answers2(self):
        st1 = Student({'q1': 0.6, 'q2': 0.7, 'q3': 0.1})
        st2 = Student({'q1': 0.6, 'q2': 0.2, 'q3': 0.1})

        mat2 = None
        for st in [st1, st2]:
            names, mat2 = st.count_anwers_matrix(counter=mat2)
        expected = [[[2., 1., 0.],
                     [1., 1., 0.],
                     [0., 0., 0.]],
                    [[0., 1., 2.],
                     [0., 0., 1.],
                     [0., 0., 0.]],
                    [[0., 0., 0.],
                     [1., 0., 0.],
                     [2., 1., 0.]],
                    [[0., 0., 0.],
                     [0., 1., 1.],
                     [0., 1., 2.]]]
        self.assertEqual(names, {'q1': 0, 'q2': 1, 'q3': 2})
        self.assertEqual(mat2.tolist(), expected)

    def test_to_matrix(self):
        st = Student({'q1': 0.6, 'q2': 0.7, 'q3': 0.1})
        names, mat = st.to_matrix()
        self.assertEqual(names, {'q1': 0, 'q2': 1, 'q3': 2})
        self.assertEqual(mat.tolist(), [0.6, 0.7, 0.1])


if __name__ == "__main__":
    unittest.main()
