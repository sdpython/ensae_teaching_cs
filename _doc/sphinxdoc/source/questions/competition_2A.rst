
.. index:: compétition

.. _l-competition:

Compétitions
============

.. contents::
    :local:

.. _l-competition-2017-2a:

2017
++++

Le site `OpenFoodFacts <https://world.openfoodfacts.org/>`_
recense la composition de milliers de produits. La base de données
peut être téléchargée (`data <https://world.openfoodfacts.org/data>`_).
On veut savoir si les additifs ajoutés apparaissent plus fréquemment
avec certains produits ou certaines compositions. Une façon est
de prédire la présence d'additifs en fonction de toutes les autres variables.
Si un modèle de prédiction fait mieux que le hasard, cela signifie que certaines
corrélations existent. Le notebook :ref:`preparedata2017rst`
explique comment les données ont été préparées et montre un premier résultat.
C'est un problème de classification binaire.

* La colonne ``hasE`` précise si le produit contient des additifs.
* Toutes les autres colonnes peuvent être utilisées pour prédire.

Les données divisées en trois :

* `off_train_all.zip <http://www.xavierdupre.fr/enseignement/complements/off_train_all_.zip>`_ :
  pour apprendre un modèle ou tout autre chose.
* `off_test_all.zip <http://www.xavierdupre.fr/enseignement/complements/off_test_all_.zip>`_ :
  pour évaluer votre modèle.
* `off_eval_all_X.zip <http://www.xavierdupre.fr/enseignement/complements/off_eval_all_.zip>`_ :
  ce fichier ne contient pas la cible à prédire, chacun devra calculer ses prédictions,
  et une tierce partie calculera le score.
* ``off_eval_all_Y.zip`` : les réponses attendues sur la base d'évaluation,
  elles seront disponibles à la fin de la compétition.

De manière évidente, il est possible de tricher puisque la construction de ces trois
jeux est mise à disposition et qu'il serait très facile de retrouver les réponses
de la base d'évalution. J'ai quelques idées pour freiner vos ardeurs
si jamais la tentation se trouvait être trop forte.

Une fois que le modèle de prédiction est construit, il fera nécessairement
des erreurs, peut-être même avec une confiance assez forte. Peut-on affirmer
avec certitude que ces erreurs en sont vraiment ou serait-ce une erreur de saisie
des données voire un oubli volontaire sur l'étiquette du produit ? Cela nécessiterait
sans doute de récupérer quelques produits similaire à celui qui mène à une
prédiction erronnée.

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
