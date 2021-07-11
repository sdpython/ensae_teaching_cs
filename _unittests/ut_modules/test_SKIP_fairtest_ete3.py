"""
@brief      test log(time=6s)
"""
import os
import unittest
import warnings
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, get_temp_folder
import pyensae.datasource as ds


class TestModulesFairTest(unittest.TestCase):

    def test_fairtest(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no fair test
            return

        # ete3 is needed by fairtest.
        try:
            import ete3  # pylint: disable=W0611
        except ImportError:
            warnings.warn("ete3 not installed.")
            return

        try:
            import fairtest  # pylint: disable=W0611
        except ImportError:
            warnings.warn("fairtest not installed.")
            return

        from fairtest import DataSource, Testing, train, test, report  # pylint: disable=E0401
        temp = get_temp_folder(__file__, "temp_fairtest")
        data = ds.download_data("adult.data",
                                url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/",
                                whereTo=os.path.join(temp, ".."))
        names = ("age,Workclass,fnlwgt,education,education-num,marital-status,occupation,relationship," +
                 "race,sex,capital-gain,capital-loss,hours-per-week,native-country,income").split(",")
        df = pandas.read_csv(data, names=names)
        if df.shape[0] > 100:
            fLOG(df.shape)  # pylint: disable=E1101
            df = df[:100]  # pylint: disable=E1136
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
