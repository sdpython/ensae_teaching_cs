"""
@brief      test log(time=6s)
"""


import sys
import os
import unittest
import pandas


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
from pyquickhelper.pycode import is_travis_or_appveyor, get_temp_folder
import pyensae.datasource as ds


class TestModulesFairTest(unittest.TestCase):

    def test_fairtest(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        try:
            import fairtest as skip___
        except ImportError:
            path = os.path.normpath(
                os.path.abspath(
                    os.path.join(
                        os.path.split(__file__)[0],
                        "..",
                        "..",
                        "..",
                        "fairtest",
                        "src")))
            if path not in sys.path:
                sys.path.append(path)
            import fairtest as skip___

        if is_travis_or_appveyor():
            # no fair test
            return

        from fairtest import DataSource, Testing, train, test, report
        temp = get_temp_folder(__file__, "temp_fairtest")
        data = ds.download_data("adult.data",
                                url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/",
                                whereTo=os.path.join(temp, ".."))
        names = "age,Workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,income".split(
            ",")
        df = pandas.read_csv(data, names=names)
        if df.shape[0] > 100:
            fLOG(df.shape)
            df = df[:100]
        data = DataSource(df, budget=1, conf=0.95)
        SENS = ['sex', 'race']     # Protected features
        TARGET = 'income'             # Output
        EXPL = ''                     # Explanatory feature

        inv = Testing(data, SENS, TARGET, EXPL)
        train([inv])
        test([inv])
        report([inv], "adult", temp)


if __name__ == "__main__":
    unittest.main()
