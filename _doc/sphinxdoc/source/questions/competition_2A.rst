

.. index:: compétition

.. _l-competition:


Compétitions
============

.. _l-competition-2016-2a:

2016
++++

* Liens vers la compétation sur codalab : `Python 2A ENSAE - 2016 <https://competitions.codalab.org/competitions/13431>`_.
* Source : `default of credit card clients Data Set  <https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients>`_
* Données : `ensae_competition_2016.zip <https://github.com/sdpython/ensae_teaching_cs/raw/master/_doc/competitions/2016_ENSAE_2A/ensae_competition_2016.zip>`_
* BlindSet : :func:`data_cpt_ENSAE_2016_11_blind_set <ensae_teaching_cs.data.datacpt.data_cpt_ENSAE_2016_11_blind_set>`

L'objectif est de prédire la probabilité de défaut de paiement d'utilisateurs. 
On dispose de 23 variables et la variable à prédire est binaire. 
Chaque participant est évalué avec la métrique 
`AUC <http://stats.stackexchange.com/questions/132777/what-does-auc-stand-for-and-what-is-it>`_
qui est une métrique 
standard dans un problème de classification binaire.

*Notebooks*


.. toctree::
    :maxdepth: 2
    
    ../notebooks/td2a_eco_competition_statsdesc
    ../notebooks/td2a_eco_competition_modeles_logistiques
    ../notebooks/td2a_eco_competition_comparer_classifieurs
    ../notebooks/solution_2016_credit_clement
    
La solution est proposée par Clément Giron.

*Data Set Information*

This research aimed at the case of customers’ default payments in Taiwan 
and compares the predictive accuracy of probability of default among 
six data mining methods. From the perspective of risk management, 
the result of predictive accuracy of the estimated probability of 
default will be more valuable than the binary result of classification - 
credible or not credible clients. Because the real probability of default is unknown, 
this study presented the novel "Sorting Smoothing Method" to estimate the real 
probability of default. With the real probability of default as the response 
variable (Y), and the predictive probability of default as the independent 
variable (X), the simple linear regression result (Y = A + BX) shows that the 
forecasting model produced by artificial neural network has the highest coefficient 
of determination; its regression intercept (A) is close to zero, and regression 
coefficient (B) to one. Therefore, among the six data mining techniques, artificial 
neural network is the only one that can accurately estimate the real probability of default.

*Attribute Information*

* This research employed a binary variable, default payment (Yes = 1, No = 0), as the response variable. This study reviewed the literature and used the following 23 variables as explanatory variables: 
* X1: Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit. 
* X2: Gender (1 = male; 2 = female). 
* X3: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others). 
* X4: Marital status (1 = married; 2 = single; 3 = others). 
* X5: Age (year). 
* X6 - X11: History of past payment. We tracked the past monthly payment records (from April to September, 2005) as follows: X6 = the repayment status in September, 2005; X7 = the repayment status in August, 2005; . . .;X11 = the repayment status in April, 2005. The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above. 
* X12-X17: Amount of bill statement (NT dollar). X12 = amount of bill statement in September, 2005; X13 = amount of bill statement in August, 2005; . . .; X17 = amount of bill statement in April, 2005. 
* X18-X23: Amount of previous payment (NT dollar). X18 = amount paid in September, 2005; X19 = amount paid in August, 2005; . . .;X23 = amount paid in April, 2005.
