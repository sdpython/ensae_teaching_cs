"""
@file
@brief Defines a custom class to define a learner which follows the same API
than any scikit-learn learner.
"""

from .sklearn_parameters import SkLearnParameters


class SkBaseLearner:

    """
    Defines a custom class to define a learner which follows the same API
    than any `scikit-learn <http://scikit-learn.org/stable/>`_ learner.
    """

    def __init__(self, **kwargs):
        """
        empty constructor, just fills the parameters
        """

        #: *P* is an instance of :class:`SkLearnParameters <ensae_teaching_cs.ml.sklearn_parameters.SkLearnParameters>`,
        #: it keeps a copy of the parameters sent to the class and it makes it easier
        #: to implements meth *get_params* used to clone a model
        self.P = SkLearnParameters(**kwargs)

    ###################
    # API scikit-learn
    ###################

    def fit(self, X, y=None, sample_weight=None):
        """
        Fit a model

        @param      X               Training data, numpy array or sparse matrix of shape [n_samples,n_features]
        @param      y               Target values, numpy array of shape [n_samples, n_targets] (optional)
        @param      sample_weight   Weight values, numpy array of shape [n_samples, n_targets] (optional)
        @return                     self : returns an instance of self.
        """
        raise NotImplementedError()

    def predict(self, X):
        """
        Predict, usually, it calls the decision_function method

        @param      X   Samples, {array-like, sparse matrix}, shape = (n_samples, n_features)
        @return         array, shape = (n_samples,.), Returns predicted values.
        """
        raise NotImplementedError()

    def decision_function(self, X):
        """
        Output of the model in case of a regressor, matrix with a score for each class and each sample
        for a classifier

        @param      X   Samples, {array-like, sparse matrix}, shape = (n_samples, n_features)
        @return         array, shape = (n_samples,.), Returns predicted values.
        """
        raise NotImplementedError()

    def score(self, X, y=None, sample_weight=None):
        """
        Returns the mean accuracy on the given test data and labels.

        @param      X               Training data, numpy array or sparse matrix of shape [n_samples,n_features]
        @param      y               Target values, numpy array of shape [n_samples, n_targets] (optional)
        @param      sample_weight   Weight values, numpy array of shape [n_samples, n_targets] (optional)
        @return                     score : float, Mean accuracy of self.predict(X) wrt. y.
        """
        raise NotImplementedError()

    ##############
    # cloning API
    ##############

    def get_params(self, deep=True):
        """
        returns the parameters mandatory to clone the class

        @param      deep        unused here
        @return                 dict
        """
        return self.P.to_dict()

    #################
    # common methods
    #################

    def __str__(self):
        """
        usual
        """
        return "{0}({1})".format(self.__class__.__name__, str(self.P))
