"""
@brief      test log(time=2s)
"""
import unittest
from io import BytesIO
import pickle
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.exceptions import ConvergenceWarning
from pyquickhelper.pycode import ExtTestCase, ignore_warnings
from ensae_teaching_cs.ml.lasso_random_forest_regressor import LassoRandomForestRegressor


class TestLassoRandomForestRegressor(ExtTestCase):

    @ignore_warnings(ConvergenceWarning)
    def test_lasso_random_forest_regressor(self):
        X, y = make_regression(1000, n_features=10)  # pylint: disable=W0632
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        rf2 = RandomForestRegressor()
        rf2.fit(X_train, y_train)
        sc2 = rf2.score(X_test, y_test)
        ls = LassoRandomForestRegressor()
        ls.fit(X_train, y_train)
        sc = ls.score(X_test, y_test)
        self.assertLesser(len(ls.estimators_), len(
            ls.rf_estimator_.estimators_))
        self.assertLesser(abs(sc - sc2) / sc2, 0.1)

        by = BytesIO()
        pickle.dump(ls, by)
        by2 = BytesIO(by.getvalue())
        mod2 = pickle.load(by2)
        p1 = ls.predict(X_test)
        p2 = mod2.predict(X_test)
        self.assertEqualArray(p1, p2)


if __name__ == "__main__":
    unittest.main()
