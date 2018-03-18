
.. |pyecopng| image:: ../_static/pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: ../_static/pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

|pyecopng| |pystatpng|

.. _l-td2a-ml-extensions:

De la théorie à la pratique
+++++++++++++++++++++++++++

Tous les modèles proposées répondent à un problème d'optimisation
et convergent avec un algorithme donnée et avec des hypothèses
précises sur les données. Dans la plupart des cas, ces hypothèses
ne sont jamais vérifiées. Malgré tout, on continue à utiliser
le machine learning parce qu'il marche plutôt bien même si les
hypothèses initiales ne sont pas vérifiées mais connaître la
façon dont sont construits ces modèles aide à construire
une liste de recettes qui améliorent leur performances et qui
accélèrent le moment où le problème devient vraiment intéressant.
Deux ou trois petits à garder à l'esprit.

Les réseaux de neurones s'apprennent avec des méthodes de d'optimisation
basées sur le **gradient**. Elles n'aiment pas les **échelles logarithmiques**.
Les variables de type fréquences (nombre de clics sur une page, nombre d'occurence
d'un mot, ...) ont des queues épaisses et quelques valeurs extrêmes,
il est conseillé de normaliser et de passer à une échelle logarithmique.
Elles n'aiment pas les **gradients élevés** : le gradient peut avoir une valeur très élevée
dan un voisinage localisée (un regression proche d'une fonction en escalier),
l'optimisation à base de gradient mettra beaucoup de temps à converger.
Elles n'aiment pas les **variables discrètes** : le calcul du gradient fonctionne beaucoup
mieux sur des variables continues plutôt que des variables discrètes
car cela limite le nombre de valeurs que peut prendre le gradient.

Les forêts aléatoires  et les arbres de décision sont des méthodes ensemblistes.
Elles n'utilisent pas de gradient. Elles ne sont pas sensibles à la
**normalisation**, comme ces modèles sont des assemblages de décisions basées sur
des seuils, ils ne sont pas sensibles aux changements d'échelle. En revanche, elles
n'aiment pas trop pas **décisions obliques**, comme un seuil s'applique sur une variable,
il ne peut approcher une droite *x + y = 1* qu'avec une fonction en escalier
(lire `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_).
Ces algorithms n'aiment pas non plus les problèmes **multi-classe**.
Pour un assemblage de fonction binaire (au dessus ou en dessous du seuil),
il est plus facile d'avoir seulement deux choix.
On compense cette lacune avec deux stratégies
`one versus rest <https://en.wikipedia.org/wiki/Multiclass_classification#One-vs.-rest>`_
ou `one versus one <https://en.wikipedia.org/wiki/Multiclass_classification#One-vs.-one>`_
(stratégie dite aussi `pair-wise <https://en.wikipedia.org/wiki/Learning_to_rank#Pairwise_approach>`_).

Le `boosting <https://en.wikipedia.org/wiki/Boosting_(machine_learning)>`_
est une technique de machine learning qui consiste à sur-pondérer
les erreurs. Pour un algorithme d'apprentissage itératif, cela consiste à donner
plus de poids à l'itération *n* aux erreurs produites par l'itération *n-1*.
L'algorithme le plus connu est `AdaBoost <https://en.wikipedia.org/wiki/AdaBoost>`_.
Le `gradient boosting <https://en.wikipedia.org/wiki/Gradient_boosting>`_ est
l'application de ce concept à un modèle et une fonction d'erreur dérivable.
A ce sujet : `The Boosting Approach to Machine Learning An Overview <https://www.cs.princeton.edu/picasso/mats/schapire02boosting_schapire.pdf>`_,
`A Theory of Multiclass Boosting <http://rob.schapire.net/papers/multiboost-journal.pdf>`_,
`weak learner <https://stats.stackexchange.com/questions/82049/what-is-meant-by-weak-learner>`_.

`XGBoost <http://xgboost.readthedocs.io/>`_
est un librairie qui a bénéficié de nombreux apports au fur et à
mesure des compétitions `Kaggle <https://www.kaggle.com/>`_
qu'elle a permis de gagner. Certains paramètres qui pilotent l'apprentissage
du modèle ne sont pas issus de la théorie mais de la pratique
et permettent de contourner un problème de données qui ferait
échouer l'apprentissage :
`paramètres de XGBoost <https://github.com/dmlc/xgboost/blob/master/doc/parameter.md>`_.
C'est le cas du paramètre *scale_pos_weight* qui permet de forcer une distribution
des labels de sortie dans le cas d'un problème de classification binaire.
C'est utile dans le cas d'un problème
de :ref:`l-imbalanced-classification`.

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_ml

*Lectures*

* :ref:`Travailleur les features ou changer de modèle <mlfeaturesmodelrst>`
* :ref:`Bien démarrer un projet de machine learning <l-debutermlprojet>`
* :ref:`question_projet_2014`
* `MA 2823 Foundations of Machine Learning (Fall 2016) <http://cazencott.info/index.php/pages/MA-2823-Foundations-of-Machine-Learning-%28Fall-2016%29>`_
* `A Random Forest Guided Tour <http://www.lsta.upmc.fr/BIAU/bs.pdf>`_, Gérard Biau, Erwan Scornet
* `Courbe ROC <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html>`_
* `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_
* `A Unified Approach to Learning Task-Specific Bit Vector Representations for Fast Nearest Neighbor Search <http://www.cs.toronto.edu/~vnair/www12.pdf>`_
* `On the Mutual Nearest Neighbors Estimate in Regression <http://www.jmlr.org/papers/volume14/guyader13a/guyader13a.pdf>`_
* `The Boosting Approach to Machine Learning An Overview <https://www.cs.princeton.edu/picasso/mats/schapire02boosting_schapire.pdf>`_,
* `A Theory of Multiclass Boosting <http://rob.schapire.net/papers/multiboost-journal.pdf>`_

`JMLR <http://www.jmlr.org/>`_
poste régulièrement des articles sur des librairies de machine learning open source telles que
`fastFM: A Library for Factorization Machines <fastFM: A Library for Factorization Machines>`_.

*Recherche*

* `XGBoost: A Scalable Tree Boosting System <https://arxiv.org/pdf/1603.02754.pdf>`_
* `On the Influence of Momentum Acceleration on OnlineLearning <http://www.jmlr.org/papers/volume17/16-157/16-157.pdf>`_

*Digressions*

* `A Network That Learns Strassen Multiplication <http://www.jmlr.org/papers/volume17/16-074/16-074.pdf>`_
* `Learning Theory for Distribution Regression <http://www.jmlr.org/papers/volume17/14-510/14-510.pdf>`_

*Métriques*

* `Optimization of AMS using Weighted AUC optimized models <http://jmlr.org/proceedings/papers/v42/diaz14.pdf>`_

*Modules*

* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `xgboost <https://xgboost.readthedocs.io/en/latest/>`_
* `mlxtend <https://github.com/rasbt/mlxtend>`_
