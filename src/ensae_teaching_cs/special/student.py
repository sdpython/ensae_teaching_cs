"""
@file
@brief
"""
import numpy


class Student:
    """
    Class Student, it has:

    * `qna`: dictionary {question: answer}

    `answer` is a float in [0, 1], 0 means the student
    failed to answer, 1 means the student is right,
    in ]0, 1[, we don't know for sure. (We are human!)

    .. runpython::
        :showcode:

        from ensae_teaching_cs.special.student import Student

        st = Student({'q1': 0.6, 'q2': 0.7, 'q3': 0.1})
        print(st)

    """

    def __init__(self, qna):
        self.qna = qna

    def __repr__(self):
        "usual"
        return "%s(%r)" % (self.__class__.__name__, self.qna)

    def count_anwers(self, threshold=0.5, counter=None):
        """
        Returns a dictionary `{ ('q1', 'q2'): { (True, False): 1 } }`.
        That means the student was True at question q1 and False at question q2.
        If counter is not None, this dictionary is added to the same
        dictionary computed with an other students.

        `{ ('q1', 'q2'): { (True, False): 1, (False, False): 2 } }`

        This means there were 3 students, 1 was right at q1 and wrong at q2,
        2 were wrong at both questions.

        :param threshold: threshold above which the answer is valid
        :param counter: existing counter, added to these counts
        :return: new or updated counter

        .. runpython::
            :showcode:

            from ensae_teaching_cs.special.student import Student
            from pprint import pprint

            st1 = Student({'q1': 0.6, 'q2': 0.7, 'q3': 0.1})
            st2 = Student({'q1': 0.6, 'q2': 0.2, 'q3': 0.1})
            mat = st1.count_anwers()

            pprint(mat)
        """
        if counter is None:
            res = {}
        else:
            res = counter
        for q1, a1 in self.qna.items():
            b1 = a1 >= 0.5
            for q2, a2 in self.qna.items():
                b2 = a2 >= 0.5
                if q1 == q2:
                    continue

                key = q1, q2
                if key not in res:
                    res[key] = {}
                key2 = b1, b2
                if key2 not in res[key]:
                    res[key][key2] = 0
                res[key][key2] += 1

        return res

    def to_matrix(self, names=None):
        """
        Returns a names, vect.

        * names is dictionary `{'q1': row_index}`
        * vect is a vector: mat[row_index] is the answer to question q1

        :param names: mapping between rows and questions
        :return: names or names, new or updated counter

        .. runpython::
            :showcode:

            from ensae_teaching_cs.special.student import Student

            st = Student({'q1': 0.6, 'q2': 0.7, 'q3': 0.1})
            names, mat = st.to_matrix()

            print(names)
            print(mat)
        """
        if names is None:
            sorted_names = list(sorted(self.qna))
            names = {}
            for i, name in enumerate(sorted_names):
                names[name] = i

        mat = numpy.zeros(len(names), dtype=numpy.float64)
        for q, a in self.qna.items():
            mat[names[q]] = a
        return names, mat

    def count_anwers_matrix(self, threshold=0.5, counter=None, names=None):
        """
        Returns a names, mat.

        * names is dictionary `{'q1': row_index}`
        * mat is a matrix:
            * mat[0, q1_index, q2_index] is the number of times
              students were right at questions q1, q2
            * mat[1, q1_index, q2_index] is the number of times
              students were right at question q1 and wrong at question q2
            * mat[2, q1_index, q2_index] is the number of times
              students were wrong at question q1 and right at question q2
            * mat[3, q1_index, q2_index] is the number of times
              students were wring at both questions

        :param threshold: threshold above which the answer is valid
        :param counter: existing counter, added to these counts
        :param names: mapping between rows and questions
        :return: names or names, new or updated counter

        .. runpython::
            :showcode:

            from ensae_teaching_cs.special.student import Student

            st1 = Student({'q1': 0.6, 'q2': 0.7, 'q3': 0.1})
            st2 = Student({'q1': 0.6, 'q2': 0.2, 'q3': 0.1})
            names, mat = st1.count_anwers_matrix()

            print(names)
            print(mat)

        The following code compares this method to the previous one.

        .. runpython::
            :showcode:

            from pyinstrument import Profiler
            from ensae_teaching_cs.special.student import Student


            students = [Student.random_student(80) for i in range(50)]

            profiler = Profiler()
            profiler.start()

            for n in range(10):
                mat2 = {}
                for st in students:
                    st.count_anwers(counter=mat2)

            for n in range(10):
                mat3 = None
                names = None
                for st in students:
                    names, mat3 = st.count_anwers_matrix(counter=mat3, names=names)

            profiler.stop()
            print(profiler.output_text())
        """
        names, mat = self.to_matrix(names)
        mat = (mat >= threshold).reshape(-1, 1).astype(numpy.int64)

        if counter is None:
            res = numpy.zeros((4, len(names), len(names)), dtype=numpy.float64)
        else:
            res = counter

        neg_mat = 1 - mat
        tmat = mat.T
        tneg_mat = neg_mat.T
        res[0, :, :] += mat @ tmat   # numpy.dot(mat, tmat)
        res[1, :, :] += mat @ tneg_mat
        res[2, :, :] += neg_mat @ tmat
        res[3, :, :] += neg_mat @ tneg_mat
        return names, res

    @staticmethod
    def random_student(n=100):
        """
        Returns a student with random answers.

        :param n: number of questions
        :return: *Student*
        """
        rnd = numpy.random.rand(n)
        qna = {}
        for i in range(n):
            qna[i] = rnd[i]
        return Student(qna)
