"""
@file
@brief Implements *LassoRandomForestRegressor*.
"""
import numpy
from sklearn.base import BaseEstimator, RegressorMixin, clone
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso


class LassoRandomForestRegressor(BaseEstimator, RegressorMixin):
    """
    Fits a random forest and then selects trees by using a
    Lasso regression. The traning produces the following
    attributes:

    * `rf_estimator_`: trained random forest
    * `lasso_estimator_`: trained Lasso
    * `estimators_`: trained estimators mapped to a not null coefficients
    * `intercept_`: bias
    * `coef_`: estimators weights
    """

    def __init__(self, rf_estimator=None, lasso_estimator=None):
        """
        @param  rf_estimator    random forest estimator,
                                :epkg:`sklearn:ensemble:RandomForestRegressor`
                                by default
        @param  lass_estimator  Lasso estimator,
                                :epkg:`sklearn:linear_model:LassoRegression`
                                by default
        """
        BaseEstimator.__init__(self)
        RegressorMixin.__init__(self)
        if rf_estimator is None:
            rf_estimator = RandomForestRegressor()
        if lasso_estimator is None:
            lasso_estimator = Lasso()
        self.rf_estimator = rf_estimator
        self.lasso_estimator = lasso_estimator

    def fit(self, X, y, sample_weight=None):
        """
        Fits the random forest first, then applies a lasso
        and finally removes all trees mapped to a null coefficient.

        @param      X               training features
        @param      y               training labels
        @param      sample_weight   sample weights
        """
        self.rf_estimator_ = clone(self.rf_estimator)
        self.rf_estimator_.fit(X, y, sample_weight)

        estims = self.rf_estimator_.estimators_
        estimators = numpy.array(estims).ravel()
        X2 = numpy.zeros((X.shape[0], len(estimators)))
        for i, est in enumerate(estimators):
            pred = est.predict(X)
            X2[:, i] = pred

        self.lasso_estimator_ = clone(self.lasso_estimator)
        self.lasso_estimator_.fit(X2, y)

        not_null = self.lasso_estimator_.coef_ != 0
        self.intercept_ = self.lasso_estimator_.intercept_
        self.estimators_ = estimators[not_null]
        self.coef_ = self.lasso_estimator_.coef_[not_null]
        return self

    def decision_function(self, X):
        """
        Computes the predictions.
        """
        prediction = None
        for i, est in enumerate(self.estimators_):
            pred = est.predict(X)
            if prediction is None:
                prediction = pred * self.coef_[i]
            else:
                prediction += pred * self.coef_[i]
        return prediction + self.intercept_

    def predict(self, X):
        """
        Computes the predictions.
        """
        return self.decision_function(X)
