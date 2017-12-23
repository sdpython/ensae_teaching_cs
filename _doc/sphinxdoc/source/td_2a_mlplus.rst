
.. _l-td2a-mlplus:

=============================
Machine learning - extensions
=============================

.. contents::
    :local:

.. |pyecopng| image:: _static/pyeco.png
            :height: 20
            :alt: Economie
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: _static/pystat.png
            :height: 20
            :alt: Statistique
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

------------

Machine Learning Avancé
=======================

.. contents::
    :local:
    :depth: 1

|pyecopng| |pystatpng|

Régression quantile
+++++++++++++++++++

(*à venir*)

*Lectures*

* `La régression quantile en pratique <https://www.insee.fr/fr/statistiques/fichier/1381107/doc_regression_quantile.pdf>`_
* `Extensions of the Markov chain marginal bootstrap <https://www.researchgate.net/publication/23635751_Extensions_of_the_Markov_chain_marginal_bootstrap>`_
* `Iteratively reweighted least squares <https://en.wikipedia.org/wiki/Iteratively_reweighted_least_squares>`_

*Modules*

* `statsmodels <http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.quantile_regression.QuantReg.html>`_

|pyecopng| |pystatpng|

Optimisation des hyperparamètres
++++++++++++++++++++++++++++++++

(*à venir*)

*Lectures*

* `Algorithms for Hyper-Parameter Optimization <https://papers.nips.cc/paper/4443-algorithms-for-hyper-parameter-optimization.pdf>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/>`_
* `hyperopt <https://github.com/hyperopt/hyperopt>`_

|pystatpng|

Online training
+++++++++++++++

*(à venir)*

*Lectures*

* `Fast Rates in Statistical and Online Learning <http://www.jmlr.org/papers/volume16/vanerven15a/vanerven15a.pdf>`_

|pystatpng|

Modèles avec dépendances dans le temps
++++++++++++++++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Learning Algorithms for Second-Price Auctions with Reserve <http://www.jmlr.org/papers/volume17/14-499/14-499.pdf>`_
* `Machine Learning in an Auction Environment <http://www.jmlr.org/papers/volume17/15-109/15-109.pdf>`_

|pyecopng| |pystatpng|

Timeseries - Séries temporelles
+++++++++++++++++++++++++++++++

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_timeseries

(à venir : modèles SETAR pour les séries non périodiques, modèles proies prédateurs)

*Lectures*

* `Time series analysis with pandas <http://earthpy.org/pandas-basics.html>`_
* `Consistent Algorithms for Clustering Time Series <http://www.jmlr.org/papers/volume17/khaleghi16a/khaleghi16a.pdf>`_
* `Learning Time Series Detection Models from Temporally Imprecise Labels <https://arxiv.org/abs/1611.02258>`_
* `Time Series Prediction With Deep Learning in Keras <http://machinelearningmastery.com/time-series-prediction-with-deep-learning-in-python-with-keras/>`_
* `Sequence Classification with LSTM Recurrent Neural Networks in Python with Keras <http://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/>`_
  (voir `LSTM <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>`_)
* `Time Series Classification and Clustering with Python <http://alexminnaar.com/time-series-classification-and-clustering-with-python.html>`_
* `Dynamic Time Warping <https://en.wikipedia.org/wiki/Dynamic_time_warping>`_
* `Functional responses, functional covariates and the concurrent model <http://www.ece.uvic.ca/~bctill/papers/mocap/Ramsay_Silverman_2005ao.pdf>`_
* `Fast and Accurate Time Series Classification with WEASEL <https://arxiv.org/pdf/1701.07681.pdf>`_ (text and timeseries)
* `Forecasting at Scale <https://facebookincubator.github.io/prophet/static/prophet_paper_20170113.pdf>`_ (Facebook)
* `SETAR <https://en.wikipedia.org/wiki/SETAR_(model)>`_ : prédiction sur des modèles
  en apparence cycliques mais non périodiques (type proies-prédateurs, chaotiques),
  SETAR = Self-Exciting Threshold AutoRegressive
* `Using predator-prey models on the Canadian lynx series <http://andrewgelman.com/2012/01/28/the-last-word-on-the-canadian-lynx-series/>`_,
  `Inference for nonlinear dynamical systems <http://www.pnas.org/content/103/49/18438.full.pdf>`_
* `Milestones of Deep Learning <http://www.codesofinterest.com/2017/07/milestones-of-deep-learning.html#more>`_
* `Engineering Extreme Event Forecasting at Uber with Recurrent Neural Networks <https://eng.uber.com/neural-networks/>`_
* `Holt-Winters seasonal method <https://www.otexts.org/fpp/7/5>`_,
  `Initializing the Holt-Winters method <https://robjhyndman.com/hyndsight/hw-initialization/>`_

*Compétitions*

* Kaggle Web Traffic Time Series Forecasting `code <https://github.com/Arturus/kaggle-web-traffic>`_,
  `modèle <https://github.com/Arturus/kaggle-web-traffic/blob/master/how_it_works.md>`_

*Modules*

* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `pyflux <http://pyflux.readthedocs.io/en/latest/>`_ (la documentation est plutôt bien faite)
* `fbprophet <https://github.com/facebookincubator/prophet/tree/master/python>`_
  (requires `pystan <http://pystan.readthedocs.io/en/latest/index.html>`_)
* `Rob J Hyndman software <http://robjhyndman.com/publications/software/>`_
  (disponible uniquement en R)
* `influxdb <https://github.com/influxdata/influxdb>`_ (An Open-Source Time Series Database)
* `seasonal <https://github.com/welch/seasonal>`_

|pystatpng|

Timeseries - Filtre de Kalman
+++++++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `An Introduction to the Kalman Filter <http://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf>`_
* `Implementation of Kalman Filter with Python Language <https://arxiv.org/ftp/arxiv/papers/1204/1204.0375.pdf>`_
* `Derivation of Kalman Filtering and Smoothing Equations <https://users.ece.cmu.edu/~byronyu/papers/derive_ks.pdf>`_
* `Auto-Differentiating Linear Algebra <https://arxiv.org/pdf/1710.08717.pdf>`_
* `Kalman Filtering in Python for Reading Sensor Input <http://scottlobdell.me/2014/08/kalman-filtering-python-reading-sensor-input/>`_
* `kalman 2d filter in python <https://stackoverflow.com/questions/13901997/kalman-2d-filter-in-python>`_
* `Multidimensional Kalman-Filter <https://github.com/balzer82/Kalman>`_
* `Deep Kalman Filters <https://arxiv.org/abs/1511.05121>`_

*Modules*

* `pykalman <https://pykalman.github.io/>`_
* `filterpy <https://github.com/rlabbe/filterpy>`_
* `scipy <http://scipy-cookbook.readthedocs.io/items/KalmanFiltering.html>`_

Timeseries - Similarités
++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Faster Retrieval with a Two-Pass Dynamic-Time-Warping Lower Bound <https://arxiv.org/abs/0811.3301>`_
* `Soft-DTW: a Differentiable Loss Function for Time-Series <https://arxiv.org/abs/1703.01541>`_

*Modules*

* `LBImproved C++ Library <https://github.com/lemire/lbimproved>`_,
  `LBImproved C++ Library and Python <https://github.com/felixr/dtw_lbimproved>`_
* `soft-dtw <https://github.com/mblondel/soft-dtw/>`_

|pystatpng|

Finance
+++++++

 (*à venir*)

*Modules*

* `pyalgotrade <http://gbeced.github.io/pyalgotrade/>`_
* `zipline <https://pypi.python.org/pypi/zipline>`_
* `alphalens <https://github.com/quantopian/alphalens>`_
* `pyfolio <https://github.com/quantopian/pyfolio>`_
* `empyrical <https://github.com/quantopian/empyrical>`_
* `quantlib <https://github.com/lballabio/quantlib>`_
* `prophet <http://prophet.michaelsu.io/en/latest/>`_ (not updated anymore)
* `bloomberg API <https://www.bloomberglabs.com/api/libraries/>`_
* `ta-lib <https://github.com/mrjbq7/ta-lib>`_

*Modules data*

* `forex-python <https://github.com/MicroPyramid/forex-python>`_
* `python-currencies <https://github.com/Alir3z4/python-currencies>`_

|pystatpng|

Auto-Learning
+++++++++++++

*(à venir)*

* `Angluin Algorithm <https://web.archive.org/web/20131202232143/http://www.cse.iitk.ac.in/users/chitti/thesis/references/learningRegSetsFromQueriesAndCounterExamples.pdf>`_

*Article de blog*

* `Automating Development and Optimization of Machine Learning Models <https://www.datanami.com/2017/06/12/automating-development-optimization-machine-learning-models/>`_

*Lectures*

* `ATM: A distributed, collaborative, scalable system for automated machine learning <https://cyphe.rs/static/atm.pdf>`_
  (site web: `ATM <https://hdi-dai.lids.mit.edu/projects/atm/>`_)
* `FeatureHub: Towards collaborative data science <https://www.micahsmith.com/files/featurehub-smith.pdf>`_
* `Learning to learn by gradient descent by gradient descent <https://papers.nips.cc/paper/6461-learning-to-learn-by-gradient-descent-by-gradient-descent.pdf>`_
* `Matching Networks for One Shot Learning <https://papers.nips.cc/paper/6385-matching-networks-for-one-shot-learning.pdf>`_
* `Efficient and Robust Automated Machine Learning <http://papers.nips.cc/paper/5872-efficient-and-robust-automated-machine-learning.pdf>`_
* `Learning Regular Sets from Queries and Counterexamples <https://web.archive.org/web/20131202232143/http://www.cse.iitk.ac.in/users/chitti/thesis/references/learningRegSetsFromQueriesAndCounterExamples.pdf>`_
* `Neural Architecture Search With Reinforcement Learning <https://openreview.net/forum?id=r1Ue8Hcxg&noteId=r1Ue8Hcxg>`_ (`pdf <https://openreview.net/pdf?id=r1Ue8Hcxg>`_
* `ASlib: A Benchmark Library for Algorithm Selection <https://arxiv.org/abs/1506.02465>`_
* `MacroBase: Prioritizing Attention in Fast Data <https://arxiv.org/pdf/1603.00567.pdf>`_
* `A Bayesian criterion for evaluating the robustness of classification rules in binary data sets <http://www.marc-boulle.fr/publications/GayEtAlAKDM12.pdf>`_
* `Bayesian instance selection for the nearest neighbor rule <http://www.marc-boulle.fr/publications/FerrandizEtAlML10.pdf>`_
* `One Model To Learn Them All <https://arxiv.org/abs/1706.05137>`_
* `DLPaper2Code: Auto-generation of Code from Deep Learning Research Papers <https://arxiv.org/pdf/1711.03543.pdf>`_

*Sites*

* `Machine Learning for Automated Algorithm Design <http://www.ml4aad.org/>`_

*Modules*

* `ATM <https://github.com/HDI-Project/ATM>`_
* `FeatureHub <https://github.com/HDI-Project/FeatureHub>`_
* `REP <https://github.com/yandex/rep>`_
* `TPOT <https://github.com/rhiever/tpot>`_
* `auto-sklearn <https://github.com/automl/auto-sklearn/>`_
* `RoBO <https://github.com/automl/RoBO>`_ (bayésien)

|pystatpng|

Prédire une distribution
++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Learning with a Wasserstein Loss <https://arxiv.org/pdf/1506.05439.pdf>`_

|pystatpng|

Sequence Learning
+++++++++++++++++

*(à venir)*

*Lectures*

* `A Credit Assignment Compiler for Joint Prediction <https://arxiv.org/pdf/1406.1837.pdf>`_

|pystatpng|

Clustering hors espace vectoriel de dimension finie
+++++++++++++++++++++++++++++++++++++++++++++++++++

(à venir)

*Clustering de trajectoires*

Le problème est qu'on cherche plutôt à clusteriser de bouts de trajectoires sinon il suffirait
de clusteriser le point de départ d'arrivée. Que ferait-on alors de deux trajectoires
qui passent par le même chemin ?

* `Discovering Patterns in Time-Varying Graphs: A Tri`_clustering Approach <http://www.marc-boulle.fr/publications/GuigouresEtAlADAC15.pdf>`_
* `Co-Clustering Network-Constrained Trajectory Data <http://www.marc-boulle.fr/publications/ElMahrsiEtAlAKDM15.pdf>`_

|pystatpng|

Algorithmes génétiques et autres variantes
++++++++++++++++++++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Natural Evolution Strategies <http://people.idsia.ch/~tom/publications/nes.pdf>`_

*Modules*

* `pyevolve <http://pyevolve.sourceforge.net/>`_

---------------

Interprétation, Anonymisation, Cryptage, Privacy
================================================

On sait beaucoup de choses avec les données et comme elles concernent
des personnes la plupart du temps, les chercheurs réfléchissent
à d'autres façons de les exploiter.

.. contents::
    :local:
    :depth: 1

|pyecopng| |pystatpng|

Machine Learning éthique
++++++++++++++++++++++++

Toutes les entreprises ont des données. Ce qui a changé récemment est
ce ne sont plus seulement des données à caractère personnel, l'ensemble
de vos commandes, le montant, mais aussi des
données de déplacements. Le téléphone portable et les applications
permet à beaucoup plus d'acteurs de collecter ces mêmes données.
La législation n'est pas toujours très claire quant à ce qu'on le droit
d'en faire et les pays ne partagent pas tous les mêmes règles.
De plus, c'est une chose que de fixer une limite, c'est autre chose
que de vérifier qu'elle n'a pas été franchie.
Des modèles construits avec des données si précises peuvent
de retrouver des informations que vous n'avez pourtant pas divulgué.
Comment déterminer si un modèle ne produit pas des résultats biaisés
envers une partie de la population même avec des données anonymes ?
Les articles sont encore peu nombreux à
ce sujet et plutôt récents. Il est probable qu'il y en ait un peu plus
à l'avenir. Il n'existe pas de certitude quant au caractère éthique
d'un modèle. Quelques idées ont néanmoins émergé :

* La collecte des données est parfois biaisée, les échantillons aléatoires
  sont rares sur Internet, la collecte est incitative (échange service contre
  données). Certaines sous-population sont sur-représentées, d'autres sous-représentées.
  Il faut en tenir compte.
* Construire un modèle interprétable et de cette façon vérifier son côté éthique :
  `Ideas on interpreting machine learning <https://www.oreilly.com/ideas/ideas-on-interpreting-machine-learning>`_.
* Fabriquer de fausses observations pour vérifier que le modèle ne change
  pas de prédictions quand il ne le devrait pas :
  `Equality of Opportunity in Supervised Learning <http://ttic.uchicago.edu/~nati/Publications/HardtPriceSrebro2016.pdf>`_.
* Construire deux modèles pour éviter les interactions entre :math:`X_1` et :math:`X_2`,
  le premier modèle ne voit que :math:`X_1`, le second ne voit que :math:`X_2`,
  puis on combine les prédictions :
  `When Recommendations Systems Go Bad <https://www.youtube.com/watch?v=MqoRzNhrTnQ>`_.
* Construire une partition de la population à étudier pour vérifier
  que l'appartenance à un sous-groupe n'est pas corrélée à la prédiction
  ou à l'erreur de prédiction :
  `FairTest: Discovering Unwarranted Associations in Data-Driven Applications <https://arxiv.org/pdf/1510.02377.pdf>`_.

L'article `Equality of Opportunity in Supervised Learning <http://ttic.uchicago.edu/~nati/Publications/HardtPriceSrebro2016.pdf>`_
définit l'aspect éthique comme l'invariance d'une loi marginale. On suppose que *S*
est un attribut protégé binaire (exemple : le genre). *I* sont les entrées du modèle
de machine learning, *O* les sorties. Le modèle est éthique si :

.. math::

    \pr{ O | I, S=0} = \pr{ O | I, S=1}

La connaissance de *S* ne change pas la prédiction. Cela pose deux problèmes.
Le premier est que parfois cette distribution change car cet attribut est corrélé avec
un autre qui lui n'est pas protégé. Que décide-t-on dans ce cas ? Le second est
l'égalité n'est jamais vérifié sur de vraies données, les deux distributions
doivent être proches. Elles peuvent l'être sur l'ensemble de la population
tout en ne l'étant pas du tout sur une petite partie de la population.
L'article `FairTest: Discovering Unwarranted Associations in Data-Driven Applications <https://arxiv.org/pdf/1510.02377.pdf>`_
propose une réponse à ces deux problèmes.

*Notebooks*

.. toctree::

    notebooks/_gs2a_ethics

*Lectures*

* `Comment permettre à l'homme de garder la main ? <https://www.cnil.fr/sites/default/files/atoms/files/cnil_rapport_garder_la_main_web.pdf#page=58>`_,
  Les enjeux éthiques des algorithmes et de l’intelligence artificielle,
  Synthèse du débat public animé par la :epkg:`CNIL` dans le cadre de la mission
  de réflexion éthique confiée par la loi pour une république numérique.
* `FairTest: Discovering Unwarranted Associations in Data-Driven Applications <https://arxiv.org/pdf/1510.02377.pdf>`_
* `Equality of Opportunity in Supervised Learning <http://ttic.uchicago.edu/~nati/Publications/HardtPriceSrebro2016.pdf>`_
* `O21 : La transparence des algorithmes relève des droits civiques <http://www.lemonde.fr/campus/article/2017/05/02/o21-la-transparence-des-algorithmes-releve-des-droits-civiques_5121201_4401467.html>`_
* `TransAlgo : évaluer la responsabilité et la transparence des systèmes algorithmiques <https://www.inria.fr/actualite/actualites-inria/transalgo>`_
* `Réguler les algorithmes : remise d'un rapport à Axelle Lemaire <https://www.economie.gouv.fr/reguler-algorithmes-rapport-axelle-lemaire-cge>`_
* `Enquête : comment les apps Figaro, L'Equipe ou Closer participent au pistage de 10 millions de Français <https://www-numerama-com.cdn.ampproject.org/c/www.numerama.com/politique/282934-enquete-comment-les-apps-figaro-lequipe-ou-closer-participent-au-pistage-de-10-millions-de-francais.html/amp>`_
* `Accountable Algorithms <https://www.jkroll.com/papers/dissertation.pdf>`_ (PhD thesis)
* `Improving the Transparency of the Sharing Economy <http://mathias.lecuyer.me/assets/assets/www2017airbnb.pdf>`_
* `Sunlight: Fine-grained Targeting Detection at Scale with Statistical Confidence <http://www.cs.columbia.edu/~djhsu/papers/sunlight.pdf>`_
* `Justice actuarielle, algorithmes... et données <http://freakonometrics.hypotheses.org/51783>`_
* `Surveiller et prévenir, l'ère de la pénalité prédictive <https://bourgoinblog.wordpress.com/2017/11/10/surveiller-et-prevenir-lere-de-la-penalite-predictive/>`_

*Conférences*

* `Katharine Jarmul | Keynote: Ethical Machine Learning: Creating Fair Models in an Unjust World <https://www.youtube.com/watch?v=hDgXIUM3Rmw>`_
* `When Recommendations Systems Go Bad <https://www.youtube.com/watch?v=MqoRzNhrTnQ>`_

*Sites*

* `Data Transparency Lab <http://datatransparencylab.org/>`_
* `OPAL <http://www.data4sdgs.org/dc-opal/>`_

*Modules*

* `fairtest <https://github.com/columbia/fairtest>`_

|pyecopng| |pystatpng|

.. _l-interpretabilite-ml:

Interprétabilité des modèles
++++++++++++++++++++++++++++

.. index:: transparence, protection des données, loi européenne

Le machine learning tend à déléguer une partie de la modélisation pour
fabriquer des modèles opaques, avec beaucoup de coefficients
là où les statistiques privilégient la simplicité.
On gagne en rapidité lors de la mise en oeuvre et on perd
en interprétabilité. Il est de plus en plus important de comprendre pourquoi un
modèle se trompe, pourquoi il donne telle ou telle réponse pour une plus grande
transparence. La loi sur le
`Règlement général sur la protection des données <https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es>`_
(voir aussi
`Règlement européen sur la protection des données : ce qui change pour les professionnels <https://www.cnil.fr/fr/reglement-europeen-sur-la-protection-des-donnees-ce-qui-change-pour-les-professionnels>`_),
va dans le sens d'une plus grande transparence.
Elle doit rentrer en application à partir du 25 mai 2018.
La compréhension des décisions d'un modèle est parfois
une nécessité. Quelques idées de recherche :

* **Déléguer la complexité sur les variables** : on utilise un modèle simple
  (linéaire, arbre de décision), et on construit de nouvelles variables ou features
  parfois complexes qui font du sens pour le problèmes et qu'un modèle de machine
  learning ne pourrait pas reproduire aisément
  (voir aussi `feature learning <https://en.wikipedia.org/wiki/Feature_learning>`_).
* **Sélectionner les variables** et en garder le moins possibles,
  voir `feature selection <https://en.wikipedia.org/wiki/Feature_selection>`_,
  voir aussi `Feature importances with forests of trees <http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html>`_.
* Extraire des informations sur les variables elle-même,
  une forêt d'arbre produit une décision pour une observation qui n'utilise
  qu'une petite partie du modèle, il est possible d'extraire la liste
  des variables impliquées dans cette décision et de les trier
  par ordre d'importance, on regarde les
  **parties du modèle activées lors de la prédiction**,
  voir `treeinterpreter <https://pypi.python.org/pypi/treeinterpreter>`_.
* Poser des contraintes sur le modèle comme la **monotonie de la décision**
  par rapport aux variables, voir `Isotonic Regression <https://en.wikipedia.org/wiki/Isotonic_regression>`_.
* Apprendre un **second modèle dédié à l'interprétation**,
  voir `Making Tree Ensembles Interpretable <https://arxiv.org/pdf/1606.05390v1.pdf>`_.
* **Contenir la complexité des modèles**,
  voir `The information bottleneck method <https://arxiv.org/pdf/physics/0004057.pdf>`_
* **Visualiser** la décision.

*Notebooks*

(*à venir*)

*Lectures : expliquer*

* `Ideas on interpreting machine learning <https://www.oreilly.com/ideas/ideas-on-interpreting-machine-learning>`_
* `Learning to learn by gradient descent by gradient descent <https://arxiv.org/pdf/1606.04474.pdf>`_
* `Importance Weighting Without Importance Weights: An Efficient Algorithm for Combinatorial Semi-Bandits <http://jmlr.org/papers/volume17/15-091/15-091.pdf>`_
* `Making Tree Ensembles Interpretable <https://arxiv.org/pdf/1606.05390v1.pdf>`_
* `Understanding variable importances in forests of randomized trees <http://papers.nips.cc/paper/4928-understanding-variable-importances-in-forests-of-randomized-trees.pdf>`_
* `Confidence Intervals for Random Forests: The Jackknife and the Infinitesimal Jackknife <http://jmlr.csail.mit.edu/papers/volume15/wager14a/wager14a.pdf>`_
* `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_
* `Wavelet decompositions of Random Forests - smoothness analysis, sparse approximation and applications <http://www.jmlr.org/papers/volume17/15-203/15-203.pdf>`_
* `"Why Should I Trust You?" Explaining the Predictions of Any Classifier <http://arxiv.org/pdf/1602.04938v1.pdf>`_
  (sans doute un des articles à lire en premier - `lime <https://github.com/marcotcr/lime>`_)
* `Edward: A library for probabilistic modeling, inference, and criticism <https://arxiv.org/pdf/1610.09787.pdf>`_
* `Strictly Proper Scoring Rules, Prediction, and Estimation <https://www.cs.duke.edu/courses/spring17/compsci590.2/Gneiting2007jasa.pdf>`_
* `Visualizing and Understanding Neural Machine Translation <http://www.aclweb.org/anthology/P/P17/P17-1106.pdf>`_
* `Multiplicative Multitask Feature Learning <http://jmlr.org/papers/v17/15-234.html>`_
* `Multi-Target Regression with Rule Ensembles <http://www.jmlr.org/papers/volume13/aho12a/aho12a.pdf>`_
* `SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability <https://arxiv.org/pdf/1706.05806.pdf>`_
* `The Myth Of Interpretability of Econometric Models <http://freakonometrics.hypotheses.org/51752>`_

*Lectures : monotonie*

* `Isotonic Regression <https://en.wikipedia.org/wiki/Isotonic_regression>`_
* `Monotonic Calibrated Interpolated Look-Up Tables <http://jmlr.org/papers/v17/15-243.html>`_
* `Lattice Regression <https://papers.nips.cc/paper/3694-lattice-regression.pdf>`_
* `Optimized Regression for Efficient Function Evaluation <http://ieeexplore.ieee.org/document/6203580/?reload=true>`_
* `Fast and Flexible Monotonic Functions with Ensembles of Lattices <https://papers.nips.cc/paper/6377-fast-and-flexible-monotonic-functions-with-ensembles-of-lattices.pdf>`_
* `Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks <https://arxiv.org/abs/1702.01135>`_
  (pas tout à fait sur la monotonie mais plutôt sur une façon de s'assurer que le modèle
  ne produit pas de valeur aberrante)
* `Multivariate Convex Regression with Adaptive Partitioning <http://www.jmlr.org/papers/volume14/hannah13a/hannah13a.pdf>`_
* `Isotone Optimization in R: Pool-Adjacent-Violators Algorithm (PAVA) and Active Set Methods <http://gifi.stat.ucla.edu/janspubs/2009/reports/deleeuw_hornik_mair_R_09.pdf>`_
* `Online Isotonic Regression <http://proceedings.mlr.press/v49/kotlowski16.pdf>`_

*Lectures : local*

* `Learning Deep Nearest Neighbor Representations Using Differentiable Boundary Trees <https://arxiv.org/abs/1702.08833>`_

*Lectures: modèle graphique*

* `Factor Graph <http://deepdive.stanford.edu/assets/factor_graph.pdf>`_
* `An Introduction to Conditional Random Fields for Relational Learning <http://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf>`_
* `Factor Graphs and the Sum-Product Algorithm <http://www.comm.utoronto.ca/~frank/papers/KFL01.pdf>`_

*Lectures : erreurs, outliers*

* `BoostClean: Automated Error Detection and Repair for Machine Learning <https://arxiv.org/abs/1711.01299>`_
* `Scorpion: Explaining Away Outliers in Aggregate Queries <http://sirrice.github.io/files/papers/scorpion-vldb13.pdf>`_
* `Outlier Detection Techniques <https://www.siam.org/meetings/sdm10/tutorial3.pdf>`_,
  `abod.py <https://github.com/MarinYoung4596/OutlierDetection/tree/master/OutlierDetection/Python%20Implementation>`_

*Lectures : information bottleneck

* `Information bottleneck method <https://en.wikipedia.org/wiki/Information_bottleneck_method>`_ (wikipédia)
* `The information bottleneck method <https://arxiv.org/pdf/physics/0004057.pdf>`_
* `Deep Learning and the Information Bottleneck Principle <https://arxiv.org/pdf/1503.02406.pdf>`_
* `Opening the black box of Deep Neural Networks via Information <https://arxiv.org/pdf/1703.00810.pdf>`_

*Modules*

* `edward <http://edwardlib.org/>`_
* `deepdive <http://deepdive.stanford.edu/>`_: ce n'est pas un module python,
  cet outil a été développé pour étudier les relations dans les données et plus
  particulièrement les `dark data <https://en.wikipedia.org/wiki/Dark_data>`_
* `treeinterpreter <https://pypi.python.org/pypi/treeinterpreter>`_
* `lime <https://github.com/marcotcr/lime>`_ (`notebooks <https://github.com/marcotcr/lime/tree/master/doc/notebooks>`_)
* `ml-insights <https://ml-insights.readthedocs.io/en/latest/>`_ :
  méthode empiriques pour observer les prédictions en fonctions
  de variations des features

|pyecopng| |pystatpng|

Sélection de variables
++++++++++++++++++++++

La sélection de features peut paraître de moindre importance
dans un contexte où la puissance de calcul ne cesse d'augmenter mais
cette puissance est de plus en plus accessible via la parallélisation
qui nécessite quelques ajustements algorithmiques. L'ajout de features
complique également l'interprétation des résultats.

*à vénir*

*Lectures*

* `An Introduction to Variable and Feature Selection <http://www.jmlr.org/papers/volume3/guyon03a/guyon03a.pdf>`_
* `Feature Selection (wikipédia) <https://en.wikipedia.org/wiki/Feature_selection>`_
* `Feature Selection (scikit-learn) <http://scikit-learn.org/stable/modules/feature_selection.html>`_

|pyecopng| |pystatpng|

Anonymisation des données / Privacy
+++++++++++++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `A General Survey Of Privacy-Preserving Data Mining Models And Algorithms <http://charuaggarwal.net/generalsurvey.pdf>`_
* `Privacy Preserving Data Mining <http://web.stanford.edu/group/mmds/slides/mcsherry-mmds.pdf>`_, Cynthia Dwork, Frank McSherry,
  concept de :math:`\epsilon`-differential privacy
  (`version longue <https://users.soe.ucsc.edu/~abadi/CS223_F12/mcsherry.pdf>`_,
  `Privacy Preserving Data Mining <http://www.cs.jhu.edu/~fabian/courses/CS600.624/slides/privacy-preserving.pdf>`_)
* `Differentially Private Empirical Risk Minimization <http://www.jmlr.org/papers/volume12/chaudhuri11a/chaudhuri11a.pdf>`_
* `Preserving Privacy of Continuous High-dimensional Data with Minimax Filters <http://www.jmlr.org/proceedings/papers/v38/hamm15.pdf>`_
* `Privacy for Free: Posterior Sampling and Stochastic Gradient Monte Carlo <http://www.jmlr.org/proceedings/papers/v37/wangg15.pdf>`_
* `Privatics (INRIA) <https://team.inria.fr/privatics/>`_
* `Differential Privacy for Bayesian Inference through Posterior Sampling∗ <http://www.jmlr.org/papers/volume18/15-257/15-257.pdf>`_

*Lectures - autodestruction*

* `New Directions for Self-Destructing Data Systems <https://vanish.cs.washington.edu/pubs/vanish-extensions-techreport11.pdf>`_
* `Keypad: An Auditing File System for Theft-Prone Devices <http://eurosys2011.cs.uni-salzburg.at/pdf/eurosys2011-geambasu.pdf>`_
* `Self Destructing Data System Based On Session Keys <http://www.ijstr.org/final-print/feb2014/Self-Destructing-Data-System-Based-On-Session-Keys.pdf>`_
* `Vanish: Increasing Data Privacy with Self-Destructing Data <http://www.usenix.net/legacy/events/sec09/tech/full_papers/geambasu.pdf>`_

*Algorithmes*

* `k-anonymité <https://en.wikipedia.org/wiki/K-anonymity>`_
* `L-diversité <https://en.wikipedia.org/wiki/L-diversity>`_

*Modules*

* `AGD Tools <https://github.com/SGMAP-AGD/anonymisation>`_ : ce module s'accompagne d'un wiki et de notebooks.

|pystatpng|

Machine Learning sur des données cryptées
+++++++++++++++++++++++++++++++++++++++++

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_crypt

*Lectures*

* `Fully Homomorphic Encryption over the Integers <https://eprint.iacr.org/2009/616.pdf>`_
* `Homomorphic Encryption from Learning with Errors: Conceptually-Simpler, Asymptotically-Faster, Attribute-Based <https://eprint.iacr.org/2013/340.pdf>`_
* `Differentially Private Online Learning <http://www.jmlr.org/proceedings/papers/v23/jain12/jain12.pdf>`_
* `A Differentially Private Stochastic Gradient Descent Algorithm for Multiparty Classification <http://www.jmlr.org/proceedings/papers/v22/rajkumar12/rajkumar12.pdf>`_
* `Machine Learning Classification over Encrypted Data <https://eprint.iacr.org/2014/331.pdf>`_
* `CryptoNets: Applying Neural Networks to Encrypted Data with High Throughput and Accuracy <http://jmlr.org/proceedings/papers/v48/gilad-bachrach16.pdf>`_
* `Compressed Sensing <https://en.wikipedia.org/wiki/Compressed_sensing>`_
* `ML Confidential: Machine Learning on Encrypted Data <https://www.microsoft.com/en-us/research/publication/ml-confidential-machine-learning-on-encrypted-data-2/>`_
* `Encrypted statistical machine learning: new privacy preserving methods <https://arxiv.org/abs/1508.06845>`_
* `Fast and Secure Linear Regression and Biometric Authentication with Security Update <https://pdfs.semanticscholar.org/73f0/aa4e1b47b55f0f3d8464f61750e559067c56.pdf>`_
* `NuCypher KMS: Decentralized key management system <https://arxiv.org/abs/1707.06140>`_
* `Hawk: The Blockchain Model of Cryptography and Privacy-Preserving Smart Contracts <https://eprint.iacr.org/2015/675.pdf>`_
* `Privacy-Preserving Classification on Deep Neural Network <https://eprint.iacr.org/2017/035.pdf>`_

*Lectures - alternatives*

* `Semi-supervised Knowledge Transfer for Deep Learning from Private Training Data <https://arxiv.org/abs/1610.05755>`_
* `Practical Black-Box Attacks against Machine Learning <https://arxiv.org/abs/1602.02697>`_

*Modules*

* `ciphermed <https://github.com/rbost/ciphermed>`_, pas maintenu par l'auteur mais un peu
  plus par d'autres `ciphermed-forests <https://github.com/paberr/ciphermed-forests>`_
* `PySyft <https://github.com/OpenMined/PySyft>`_ : encrypted deep learning library
* `python-paillier (phe) <https://github.com/n1analytics/python-paillier>`_ : a library for partially homomorphic encryption in python,
  cette librairie fait du machine learning en clair une fois les données et le modèle décryptées,
  elle promet de faire `mieux <https://github.com/OpenMined/PySyft/blob/master/syft/nn/linear.py#L92>`_

------------------

Graphes - Réseaux
=================

|pyecopng| |pystatpng|

Clustering de Graphes
+++++++++++++++++++++

*(à venir)*

*Lectures*

* `Basic models and questions in statistical network analysis <https://arxiv.org/abs/1609.03511>`_
* `Trinity: A Distributed Graph Engine on a Memory Cloud <https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Trinity-1.pdf>`_
* `Dimensionality Reduction for Spectral Clustering <http://www.jmlr.org/proceedings/papers/v15/niu11a/niu11a.pdf>`_
* `Compressive Spectral Clustering <http://jmlr.org/proceedings/papers/v48/tremblay16.pdf>`_
* `Spectral Clustering on a Budget <http://www.jmlr.org/proceedings/papers/v15/shamir11a/shamir11a.pdf>`_
* `Partitioning Well-Clustered Graphs: Spectral Clustering Works! <http://www.jmlr.org/proceedings/papers/v40/Peng15.pdf>`_
* `Bipartite Correlation Clustering: Maximizing Agreements <http://www.jmlr.org/proceedings/papers/v51/asteris16.pdf>`_
* `Correlation Clustering and Biclustering with Locally Bounded Errors <http://jmlr.org/proceedings/papers/v48/puleo16.pdf>`_
* `A Unified Framework for Model-based Clustering <http://www.jmlr.org/papers/volume4/zhong03a/zhong03a.pdf>`_
* `A Tensor Approach to Learning Mixed Membership Community Models <http://jmlr.org/papers/volume15/anandkumar14a/anandkumar14a.pdf>`_

*Lectures - métriques*

* `Social Clicks: What and Who Gets Read on Twitter? <https://hal.inria.fr/hal-01281190/document>`_

*Lectures Ranking*

* `CoSimRank <http://anthology.aclweb.org/P/P14/P14-1131.pdf>`_
* `PageRank <https://en.wikipedia.org/wiki/PageRank>`_
* `A Local Spectral Method for Graphs: With Applications to Improving Graph Partitions and Exploring Data Graphs Locally <http://www.jmlr.org/papers/v13/mahoney12a.html>`_

*Modules*

* `networkx <https://networkx.github.io/>`_
* `neo4j <https://neo4j.com/developer/python/>`_,
  `py2neo <http://py2neo.org/v3/>`_,
  `neo4j-python-driver <https://github.com/neo4j/neo4j-python-driver>`_
* `snap.py <https://snap.stanford.edu/snappy/index.html#docs>`_

|pyecopng| |pystatpng|

Communautés
+++++++++++

Déterminer les communautés est un problème assez semblable au problème
de clustering mais on cherche aussi à en déterminer le centre ou encore
à catégoriser chaque individu autrement que par son appartenance à un cluster.

*(à venir)*

*Lectures*

* `Katz centrality <https://en.wikipedia.org/wiki/Katz_centrality>`_
* `Fast unfolding of communities in large networks <https://arxiv.org/pdf/0803.0476v2.pdf>`_ (Louvain)
* `Modularity and community structure in networks <https://arxiv.org/abs/physics/0602124>`_
* `Computing communities in large networks using random walks (long version) <https://arxiv.org/abs/physics/0512106>`_
* `Finding and evaluating community structure in networks <https://arxiv.org/abs/cond-mat/0308217>`_
* `Mixing patterns in networks <http://www.leonidzhukov.net/hse/2015/sna/papers/mixing_patterns.pdf>`_
* `Networks in Their Surrounding Contexts <https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch04.pdf>`_
* `Local Network Community Detection with Continuous Optimization of Conductance and Weighted Kernel K-Means <http://jmlr.org/papers/volume17/16-043/16-043.pdf>`_
* `Learning Communities in the Presence of Errors <http://www.jmlr.org/proceedings/papers/v49/makarychev16.pdf>`_

--------------------

.. _l-deep-learning:

Deep Learning
=============

.. contents::
    :local:
    :depth: 1

Le deep learning signifie aussi des calculs intensifs et des modules qui
utilisent un compilateur C++ pour optimiser les calculs
et le GPU si vous en avez.
Vous pouvez tester votre installation avec le notebook
:ref:`mldeeppythonrst` ou encore
`Keras-TensorFlow-GPU-Windows-Installation <https://github.com/antoniosehk/keras-tensorflow-windows-installation>`_.

|pystatpng|

Réseaux de neurones et Deep Learning
++++++++++++++++++++++++++++++++++++

Les premiers modèles de *deep learning* sont des réseaux de neurones.
Il n'est pas inutile de coder le sien au moins une fois
même s'il n'utilise pas de GPU, même s'il sera probablement
beaucoup plus lent. :epkg:`TensorFlow` est sans doute
le framework le plus utilisé, :epkg:`pytorch` est le plus
didactique. Il n'est pas facile de passer de l'un à l'autre
ou de convertir ses modèles d'un à l'autre même s'il
y a quelques avancées sur le sujet :
`Deep Learning Model Convertors <https://github.com/ysh329/deep-learning-model-convertor>`_.

* `Introduction au Deep Learning <https://github.com/sdpython/ensae_teaching_cs/blob/master/_doc/sphinxdoc/source/specials/DEEP%20LEARNING%20FOR%20ENSAE.pdf>`_

*Notebooks*

* :ref:`100LogisticIRISrst`
* :ref:`110PerceptronIrisrst`
* :ref:`200PerceptronMNISTrst`
* :ref:`210ConvolutionMNISTrst`
* :ref:`300ConvolutionCIFAR10rst`

*Tutorials et anti-sèches*

* `Companion Jupyter notebooks for the book "Deep Learning with Python" <https://github.com/fchollet/deep-learning-with-python-notebooks>`_
  (avec :epkg:`keras`)
* `Keras Tutorial <https://github.com/tgjeon/Keras-Tutorials>`_
* `Keras Cheat Sheet <https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Keras_Cheat_Sheet_Python.pdf>`_
* `pytorch tutorials <http://pytorch.org/tutorials/>`_ (officiel)
* `pytorch tutorials <https://github.com/yunjey/pytorch-tutorial>`_ (tout en moins de 30 lignes),
  l'exemple `pytorch basics <https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py>`_
* `PyTorch Cheat Sheet <https://github.com/bfortuner/pytorch-cheatsheet/blob/master/pytorch-cheatsheet.ipynb>`_

*Code*

* `Implementing a Neural Network from Scratch in Python - An Introduction <http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/>`_,
  `notebook <https://github.com/dennybritz/nn-from-scratch>`_
* `A Neural Network in 11 lines of Python (Part 1) <http://iamtrask.github.io/2015/07/12/basic-python-network/>`_,
  `A Neural Network in 13 lines of Python (Part 2 - Gradient Descent) <http://iamtrask.github.io/2015/07/27/python-network-part2/>`_
* `nimblenet <https://github.com/jorgenkg/python-neural-network>`_ : implémentation de différents algorithmes de back propagation
  avec `numpy <http://www.numpy.org/>`_)

*Lectures*

* `Réseau de neurones en maths <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn.html>`_
* `Artificial Intelligence, Revealed (1) <https://code.facebook.com/pages/1902086376686983>`_ : article de blog et vidéos
  expliquant les différents concepts du deep learning
* `Artificial Intelligence, Revealed (2) <https://code.facebook.com/posts/384869298519962/artificial-intelligence,-revealed/>`_ :
  quelques reprises de l'article précédent et une idée du future (en 2016)
* `DeepMind Publications <https://deepmind.com/research/publications/>`_
* `Sequential Neural Models with Stochastic Layers <https://arxiv.org/abs/1605.07571>`_
* `Interaction Networks for Learning about Objects, Relations and Physics <https://arxiv.org/abs/1612.00222>`_
* `Scaling Memory-Augmented Neural Networks with Sparse Reads and Writes <https://arxiv.org/abs/1610.09027>`_
* `Tutoriel pour CNTK <https://www.cntk.ai/pythondocs/>`_
* `Adversarially Learned Inference <https://arxiv.org/abs/1606.00704>`_
  et l'implémentation de la méthode présentée dans l'article avec :epkg:`pytorch` :
  `ali-pytorch <https://github.com/edgarriba/ali-pytorch>`_.
* `The Keras Blog <https://blog.keras.io/index.html>`_

*Vidéos*

* `PyTorch in 5 Minutes <https://www.youtube.com/watch?v=nbJ-2G2GXL0>`_
* `PyTorch Demystified, Why Did I Switch <https://www.youtube.com/watch?v=VMcRWYEKmhw>`_

*Vocabulaire*

* `deep learning
  glossary <http://www.wildml.com/deep-learning-glossary/>`_ : termes
  employés pour le deep learning
* `Core Layers <https://keras.io/layers/core/>`__ : différents
  traitement pour compenser les défauts des réseaux de neurones lors de
  l'apprentissage.

*MNIST*

* La base `MNIST <https://en.wikipedia.org/wiki/MNIST_database>`_ est le premier
  sujet pour lequel un réseau de neurones profond a été appris. C'est souvent le premier
  exemple utilisé lors des tutoriels.
* `MNIST benchmark <http://yann.lecun.com/exdb/mnist/>`_
* `Handwriten Digits Recognition Using Deep
  Learning <https://faisalorakzai.wordpress.com/2016/06/01/handwritten-digits-recognition-using-deep-learning/>`_

.. image:: mnist_illustration.png
    :width: 600

*Architectures*

* `Tutorial: Learning Deep Architectures <http://www.cs.toronto.edu/~rsalakhu/deeplearning/yoshua_icml2009.pdf>`_
* `Convolution (CNN) <https://en.wikipedia.org/wiki/Convolutional_neural_network>`_
* `Recurrent (RNN) <https://en.wikipedia.org/wiki/Recurrent_neural_network>`_ :
  séquence labelling, fenêtre glissante dans les
  images, la sortie du réseau pour l'observations *n-1* est
  utilisé par le réseau pour l'observation *n* si ces deux
  observations font partie de la même séquence.
* `Auto-Encoder <https://en.wikipedia.org/wiki/Autoencoder>`_ :
  débruiter, ACP non linéaire
* `Long short-term memory (LSTM) <https://en.wikipedia.org/wiki/Long_short-term_memory>`_,
  voir aussi `Understanding LSTM Networks <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>`_,
  le modèle est construit afin qu'il puisse prendre en compte un passé de longueur variable.
  Voir aussi `LSTM <http://deeplearning.net/tutorial/lstm.html>`_.

*Modules - deep learning*

* `Torch <http://torch.ch/>`_ et surtout :epkg:`pytorch`
  dont le design est plus simple que celui des autres.
* `Caffee <http://caffe.berkeleyvision.org/>`_ (Berkeley)
* :epkg:`CNTK` (Microsoft)
* `deeplearning4j <https://deeplearning4j.org/>`_
* `fastText <https://github.com/facebookresearch/fastText>`_
* `mxnet <https://github.com/dmlc/mxnet>`_
* `PaddlePaddle <https://github.com/PaddlePaddle/Paddle>`_ (Baidu)
* :epkg:`TensorFlow` (Google)

*Modules - GPU*

* `cupy <https://github.com/cupy/cupy>`_
* `pycuda <https://documen.tician.de/pycuda/>`_

A noter que `Theano <http://deeplearning.net/software/theano/>`_ n'est plus maintenu.

*Modules - Wrappers*

* `Keras <https://keras.io/>`_ ou `chainer <http://chainer.org/>`_ implémentent des interfaces
  communes pour plusieurs librairies de machine learning.
* `DeepRosetta <https://github.com/edgarriba/DeepRosetta>`_ : convertisseur (pas vraiment maintenu)

|pyecopng| |pystatpng|

Transfer Learning
+++++++++++++++++

Le `tranfer learning <https://en.wikipedia.org/wiki/Transfer_learning>`_
consiste à réutiliser un modèle de deep learning déjà appris sur une grande
base de données pour un problème aux dimensions plus modestes.
C'est la première chose à faire quand on commence le deep learning :
c'est souvent très rapide pour des résultats déjà acceptables.
Cela a aussi l'avantage d'être peu coûteux comparé à l'apprentissage
d'un réseau de neurones profond complet sur une grande bases de données.

*Notebooks*

* `Transfer Learning <https://github.com/sdpython/2017_deeplearning_demo/blob/master/Fine_Tuning_Deep_CNNs_with_GPU_rendered.ipynb>`_ (Olivier Grisel)
* `Search images with deep learning <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/notebooks/search_images.html#searchimagesrst>`_

*Lectures - introduction*

* `Building powerful image classification models using very little data <https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html>`_
* `Deep Learning : choisir son framework et entrainer ses modèles dans Azure <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2017/experience_2017.html>`_,
  présenté avec `Olivier Grisel <http://ogrisel.com/>`_

*Lectures - articles*

* `Unsupervised and Transfer Learning Challenges in Machine Learning, Volume 7 <http://www.mtome.com/Publications/CiML/CiML-v7-book.pdf>`_
* `ICML2011 Unsupervised and Transfer Learning Workshop <http://www.jmlr.org/proceedings/papers/v27/silver12a/silver12a.pdf>`_
* `Transfer Learning <ftp://ftp.cs.wisc.edu/machine-learning/shavlik-group/torrey.handbook09.pdf>`_
* `Deep Learning of Representations for Unsupervised and Transfer Learning <http://www.jmlr.org/proceedings/papers/v27/bengio12a/bengio12a.pdf>`_
* `Unsupervised and Transfer Learning Challenge: a Deep Learning Approach <http://www.jmlr.org/proceedings/papers/v27/mesnil12a/mesnil12a.pdf>`_
* `Transfer Learning by Kernel Meta-Learning <http://www.jmlr.org/proceedings/papers/v27/aiolli12a/aiolli12a.pdf>`_
* `A Survey on Transfer Learning <https://www.cse.ust.hk/~qyang/Docs/2009/tkde_transfer_learning.pdf>`_
* `Domain-Adversarial Training of Neural Networks <http://jmlr.org/papers/volume17/15-239/15-239.pdf>`_
* `Stability and Hypothesis Transfer Learning <http://jmlr.org/proceedings/papers/v28/kuzborskij13.pdf>`_
* `Transfer Learning Decision Forests for Gesture Recognition <http://jmlr.org/papers/volume15/goussies14a/goussies14a.pdf>`_
* `Learning Transferable Features with Deep Adaptation Networks <http://www.jmlr.org/proceedings/papers/v37/long15.pdf>`_
* `Asymmetric Transfer Learning with Deep Gaussian Processes <http://www.jmlr.org/proceedings/papers/v37/kandemir15.pdf>`_
* `Transfer Learning in Sequential Decision Problems: A Hierarchical Bayesian Approach <http://www.jmlr.org/proceedings/papers/v27/wilson12a/wilson12a.pdf>`_
* `Transfer Learning for Reinforcement Learning Domains: A Survey <http://www.jmlr.org/papers/volume10/taylor09a/taylor09a.pdf>`_
* `Unsupervised dimensionality reduction via gradient-based matrix factorization with two adaptive learning rates <http://www.jmlr.org/proceedings/papers/v27/nikulin12a/nikulin12a.pdf>`_
* `Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples <https://arxiv.org/abs/1605.07277>`_
* `Semi-supervised Knowledge Transfer for Deep Learning from Private Training Data <https://arxiv.org/abs/1610.05755>`_
* `Knowledge Concentration: Learning 100K Object Classifiers in a Single CNN <https://arxiv.org/pdf/1711.07607.pdf>`_

*Lectures - hors nn*

* `Transfer Learning Decision Forests for Gesture Recognition <http://jmlr.org/papers/volume15/goussies14a/goussies14a.pdf>`_

*Modèles pré-entraînés*

* `Places CNN <http://places.csail.mit.edu/downloadCNN.html>`_,
  `Pre-release of Places365-CNNs <https://github.com/metalbubble/places365>`_
  (deep learning)
* `CNTK <https://www.microsoft.com/en-us/research/product/cognitive-toolkit/model-gallery/>`_
  (sur `github <https://github.com/Microsoft/CNTK/tree/master/Examples>`_)
* `Model Zoo <https://github.com/BVLC/caffe/wiki/Model-Zoo>`_
* `Model Gallery CNTK <https://www.microsoft.com/en-us/cognitive-toolkit/features/model-gallery/>`_
* `tensorflow/models <https://github.com/tensorflow/models>`_

|pystatpng|

Deep Learning en détail
+++++++++++++++++++++++

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_deep

(à venir foolbox)

*Cours*

* `Deep Learning course: lecture slides and lab notebooks <https://m2dsupsdlclass.github.io/lectures-labs/>`_
* `Artificial Intelligence, Revealed (1) <https://code.facebook.com/pages/1902086376686983>`_ :
  article de blog et vidéos expliquant les différents concepts du deep learning
* `colah's blog <http://colah.github.io/>`_ *(2016/08)* blog/cours sur le deep learning
* `Tutoriels avec CNTK <https://cntk.ai/pythondocs/tutorials.html>`_
* `Course notes for CS224N Winter17 <https://github.com/stanfordnlp/cs224n-winter17-notes>`_ (Stanford)

*Tutoriels*

* `Building Autoencoders in Keras <https://blog.keras.io/building-autoencoders-in-keras.html>`_
* `Image Similarity Ranking using Microsoft Cognitive Toolkit (CNTK) <https://github.com/azure/ImageSimilarityUsingCntk>`_
* `Tutoriels avec CNTK <https://github.com/Microsoft/CNTK/tree/v2.0.beta12.0/Tutorials>`_ :
  ces notebooks sont bien illlustrés
  (`GAN - Generative Models <https://github.com/Microsoft/CNTK/blob/v2.0.beta12.0/Tutorials/CNTK_206_Basic_GAN.ipynb>`_).
* `Tutoriels avec TensorFlow <https://github.com/Hvass-Labs/TensorFlow-Tutorials>`_ :
  ce ne sont pas les seuls mais ils ont l'avantage d'être bien illustrés
  (`Adversarial Training <https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/11_Adversarial_Examples.ipynb>`_).
* `Machine Learning is Fun! Part 3: Deep Learning and Convolutional Neural Networks <https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721>`_
* `Machine Learning is Fun! Part 4: Modern Face Recognition with Deep Learning <https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78>`_
* `Object detection using Fast R-CNN <https://docs.microsoft.com/en-us/cognitive-toolkit/Object-Detection-using-Fast-R-CNN>`_
* `Deep Learning - The Straight Dope <http://gluon.mxnet.io/>`_ :
  séries de notebooks de difficulté graduelle

*Sites*

* `Tinker With a Neural Network Right Here in Your Browser <http://playground.tensorflow.org/>`_
* `ConvNetJS <http://cs.stanford.edu/people/karpathy/convnetjs/>`_
* `Databricks / Deep Learning <https://docs.databricks.com/applications/deep-learning/index.html>`_

*Liens*

* `Four deep learning trends from ACL 2017 (1) <http://www.abigailsee.com/2017/08/30/four-deep-learning-trends-from-acl-2017-part-1.html>`_
* `Four deep learning trends from ACL 2017 (2) <http://www.abigailsee.com/2017/08/30/four-deep-learning-trends-from-acl-2017-part-2.html>`_

*Articles scientifiques*

* `LightRNN: Memory and Computation-Efficient Recurrent Neural Networks <https://arxiv.org/abs/1610.09893>`_
* `Deep learning architecture diagrams <http://fastml.com/deep-learning-architecture-diagrams/>`_
* `Factorized Convolutional Neural Networks <https://arxiv.org/abs/1608.04337>`_
* `Deep Residual Learning for Image Recognition <https://arxiv.org/pdf/1512.03385v1.pdf>`_
* `Deep Learning <http://www-labs.iro.umontreal.ca/~bengioy/dlbook/>`_, Yoshua Bengio, Ian Goodfellow and Aaron Courville
* `LeNet5 <http://yann.lecun.com/exdb/lenet/>`_
* `mxnet <https://github.com/dmlc/mxnet>`_
* `Benchmarking State-of-the-Art Deep Learning Software Tools <http://arxiv.org/pdf/1608.07249v5.pdf>`_
* `Wide & Deep Learning: Better Together with TensorFlow <https://research.googleblog.com/2016/06/wide-deep-learning-better-together-with.html>`_,
  `Wide & Deep Learning for Recommender Systems <https://arxiv.org/pdf/1606.07792v1.pdf>`_
* `To go deep or wide in learning? <http://www.jmlr.org/proceedings/papers/v33/pandey14.pdf>`_
* `Three Classes of Deep Learning Architectures and Their Applications: A Tutorial Survey <https://www.microsoft.com/en-us/research/publication/three-classes-of-deep-learning-architectures-and-their-applications-a-tutorial-survey/>`_
* `Tutorial: Learning Deep Architectures <http://www.cs.toronto.edu/~rsalakhu/deeplearning/yoshua_icml2009.pdf>`_
* `Deep Learning <https://en.wikipedia.org/wiki/Deep_learning>`_ (wikipédia)
* `Fast R-CNN <https://arxiv.org/abs/1504.08083>`_ (voir `Object Detection using Fast R CNN <https://github.com/Microsoft/CNTK/wiki/Object-Detection-using-Fast-R-CNN>`_)
* `Evaluation of Deep Learning Toolkits <https://github.com/zer0n/deepframeworks/blob/master/README.md>`_ *(2015/12)*
* `Understanding Deep Learning Requires Rethinking Generalization <https://arxiv.org/pdf/1611.03530.pdf>`_
* `Training Deep Nets with Sublinear Memory Cost <https://arxiv.org/pdf/1604.06174.pdf>`_
* `On the importance of initialization and momentum in deep learning <http://www.cs.toronto.edu/~fritz/absps/momentum.pdf>`_
* `TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems <http://download.tensorflow.org/paper/whitepaper2015.pdf>`_
* `Foolbox v0.8.0: A Python toolbox to benchmark the robustness of machine learning models <https://arxiv.org/abs/1707.04131>`_

*Chiffres, Textes*

* `One weird trick for parallelizing convolutional neural networks <https://arxiv.org/pdf/1404.5997v2.pdf>`_
* `ImageNet Classification with Deep Convolutional Neural Networks <https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf>`_
* `Very Deep Convolutional Networks for Large-Scale Image Recognition <https://arxiv.org/pdf/1409.1556v6.pdf>`_
* `Multi-Digit Recognition Using A Space Displacement Neural Network  <https://papers.nips.cc/paper/557-multi-digit-recognition-using-a-space-displacement-neural-network.pdf>`_
* `Space Displacement Localization Neural Networks to locate origin points of handwritten text lines in historical documents <http://liris.cnrs.fr/christian.wolf/papers/icdar-hip2015.pdf>`_
* `Neural Network Architectures <https://culurciello.github.io/tech/2016/06/04/nets.html>`_,
  `Convolutional Neural Networks (CNNs / ConvNets) <http://cs231n.github.io/convolutional-networks/#conv>`_
* `Transfer Learning <http://cs231n.github.io/transfer-learning/>`_

*Benchmarks*

* `Benchmarking CNTK on Keras: is it Better at Deep Learning than TensorFlow? <http://minimaxir.com/2017/06/keras-cntk/>`_
  (`code <https://github.com/minimaxir/keras-cntk-benchmark>`_)

*Plus théoriques*

* `Why Does Unsupervized Deep Learning Work? - A perspective from group theory <https://arxiv.org/pdf/1412.6621v3.pdf>`_
* `Deep Learning of Representations: Looking Forward <https://arxiv.org/pdf/1305.0445v2.pdf>`_
* `Why Does Unsupervised Pre-training Help Deep Learning? <http://jmlr.org/papers/volume11/erhan10a/erhan10a.pdf>`_

*Lectures deep text*

* `Efficient Estimation of Word Representations in Vector Space <http://arxiv.org/abs/1301.3781>`_, Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean,
* `Distributed Representations of Words and Phrases and their Compositionality <http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf>`_, Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, Jeff Dean,
* `word2vec Parameter Learning Explained <http://arxiv.org/abs/1411.2738>`_, Xin Rong,
* `Tutorial on Auto-Encoders <http://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_, Piotr Mirowski
* `Pretrained Character Embeddings for Deep Learning and Automatic Text Generation <http://minimaxir.com/2017/04/char-embeddings/>`_

*Vus dans des conférences*

* `Fast R-CNN <Fast R-CNN>`_ *(dotAI)*
* `Mask R-CNN <https://arxiv.org/abs/1703.06870>`_ *(dotAI)*
* `Modèle Tenserflow <https://github.com/tensorflow/models>`_
  (modèle adaptés pour du transfer learning : ResNet, `Inception <http://nicolovaligi.com/history-inception-deep-learning-architecture.html>`_) *(dotAI)*
* `Domain-Adversarial Training of Neural Networks <http://jmlr.org/papers/volume17/15-239/15-239.pdf>`_ *(dotAI)*

*Deep learning embarqué*

* `TensorFlow sur Android <https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android>`_
* `TensorFlow sur RasberryPI <https://github.com/samjabrahams/tensorflow-on-raspberry-pi/blob/master/GUIDE.md>`_

*Modules - deep learning*

* `pytorch <http://pytorch.org/>`_ : design plus simple que tous les autres
* `keras <https://keras.io/>`_
* `mxnet <https://github.com/dmlc/mxnet>`_
* `caffe <http://caffe.berkeleyvision.org/>`_ (`installation <http://caffe.berkeleyvision.org/installation.html>`_)
* `climin <http://climin.readthedocs.io/en/latest/rmsprop.html>`_ (algorithme de back propagation)
* `tensorflow <https://www.tensorflow.org/>`_ (Google)
* `cntk <https://github.com/Microsoft/CNTK>`_

*Modules - à suivre*

* `chainer <https://github.com/pfnet/chainer>`_
* `platoon <https://github.com/mila-udem/platoon/>`_ :
  multi-GPU pour `theano <http://deeplearning.net/software/theano/>`_
  (à voir car *theano* n'est plus maintenu)
* `Federated Learning: Collaborative Machine Learning without Centralized Training Data <https://research.googleblog.com/2017/04/federated-learning-collaborative.html>`_
* `foolbox <https://github.com/bethgelab/foolbox>`_ :
  trouver des petites perturbations des données qui trompent les réseaux de neurones

|pystatpng|

Apprentissage sans labels
+++++++++++++++++++++++++

.. toctree::
    :maxdepth: 2

    specials/nolabel

*Notebooks*

*(à venir)*

*Lectures*

*Autoencoders - réduction de dimensionnalité*

* `Why Does Unsupervised Pre-training Help Deep Learning? <http://www.jmlr.org/papers/volume11/erhan10a/erhan10a.pdf>`_
* `Autoencoders <http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/>`_
* `Autoencoders, Unsupervised Learning, and Deep Architectures <http://www.jmlr.org/proceedings/papers/v27/baldi12a/baldi12a.pdf>`_
* `Generative Models <https://openai.com/blog/generative-models/>`_,
  `Adversarial Autoencoders <http://hjweide.github.io/adversarial-autoencoders>`_
* `Tutorial on Variational Autoencoders <https://arxiv.org/abs/1606.05908>`_,
  `Denoising Autoencoders (dA) <http://deeplearning.net/tutorial/dA.html>`_
* `Generative Adversarial Networks <https://arxiv.org/abs/1406.2661>`_,
  `NIPS 2016 Tutorial: Generative Adversarial Networks <https://arxiv.org/abs/1701.00160>`_
* `Adversarial Autoencoders <https://arxiv.org/abs/1511.05644>`_
* `Adversarial Autoencoders (with Pytorch) <https://blog.paperspace.com/adversarial-autoencoders-with-pytorch/>`_
* `Marginalizing Stacked Linear Denoising Autoencoders <http://www.jmlr.org/papers/volume16/chen15c/chen15c.pdf>`_
* `What Regularized Auto-Encoders Learn from the Data-Generating Distribution <http://jmlr.csail.mit.edu/papers/volume15/alain14a/alain14a.pdf>`_
* `Compressed sensing and single-pixel cameras <https://terrytao.wordpress.com/2007/04/13/compressed-sensing-and-single-pixel-cameras/>`_
* `Multi-Label Prediction via Compressed Sensing <Multi-Label Prediction via Compressed Sensing>`_
* `Inference in generative models using the Wasserstein distance <https://arxiv.org/abs/1701.05146>`_,
  `Coupling of Particle Filters <https://arxiv.org/abs/1606.01156>`_
* `Auto-Encoding Variational Bayes <https://arxiv.org/pdf/1312.6114.pdf>`_

*No label, weak labels*

* `Unsupervised Supervised Learning I: Estimating Classification and Regression Errors without Labels <http://www.jmlr.org/papers/volume11/donmez10a/donmez10a.pdf>`_
* `Unsupervised Supervised Learning II: Margin-Based Classification without Labels <http://www.jmlr.org/proceedings/papers/v15/balasubramanian11a/balasubramanian11a.pdf>`_,
  `Unsupervised Supervised Learning II: Margin-Based Classification Without Labels <http://www.jmlr.org/papers/volume12/balasubramanian11a/balasubramanian11a.pdf>`_ (longer version)
* `Large-scale Multi-label Learning with Missing Labels <http://jmlr.org/proceedings/papers/v32/yu14.pdf>`_
* `Reducing Label Complexity by Learning From Bags <http://www.jmlr.org/proceedings/papers/v9/sabato10a/sabato10a.pdf>`_
* `Learning from Corrupted Binary Labels via Class-Probability Estimation <http://jmlr.org/proceedings/papers/v37/menon15.pdf>`_
* `Generalized Expectation Criteria for Semi-Supervised Learning with Weakly Labeled Data <http://www.jmlr.org/papers/volume11/mann10a/mann10a.pdf>`_
* `Multitask Learning without Label Correspondences <http://users.sussex.ac.uk/~nq28/pubs/Quaetal11.pdf>`_
* `Training Highly Multiclass Classifiers <http://jmlr.org/papers/volume15/gupta14a/gupta14a.pdf>`_

*Online training*

* `Online Incremental Feature Learning with Denoising Autoencoders <http://jmlr.csail.mit.edu/proceedings/papers/v22/zhou12b/zhou12b.pdf>`_
* `Fast Kernel Classifiers with Online and Active Learning <http://www.jmlr.org/papers/volume6/bordes05a/bordes05a.pdf>`_,
  `A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data <http://www.jmlr.org/papers/volume6/ando05a/ando05a.pdf>`_
* `Multi Kernel Learning with Online-Batch Optimization <http://www.jmlr.org/papers/volume13/orabona12a/orabona12a.pdf>`_

*Improving training set*

* `Data Programming: Creating Large Training Sets, Quickly <https://papers.nips.cc/paper/6523-data-programming-creating-large-training-sets-quickly.pdf>`_
* `Foolbox is a Python toolbox to create adversarial examples that fool neural networks. <https://foolbox.readthedocs.io/en/latest/>`_

*Adversarial Examples*

* `The Limitations of Deep Learning in Adversarial Settings <https://arxiv.org/pdf/1511.07528v1.pdf>`_ :
  l'article montre des limites de l'approche deep learning en construisant des exemples
  proches des exemples initiaux mais qui font dérailler le modèle.

|pystatpng|

Generative Adversarial Network (GAN)
++++++++++++++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Generative Adversarial Networks <https://arxiv.org/abs/1406.2661>`_ :
  c'est le premier article paru sur le sujet
* `Least Squares Generative Adversarial Networks <https://arxiv.org/abs/1611.04076v2>`_
* `f-GAN: Training Generative Neural Samplers using Variational Divergence Minimization <https://arxiv.org/abs/1606.00709>`_
* `Fader Networks: Manipulating Images by Sliding Attributes <https://arxiv.org/pdf/1706.00409.pdf>`_
* `Partial Information Attacks on Real-world AI <http://www.labsix.org/partial-information-adversarial-examples/>`_
* `Synthesizing Robust Avdersarial Examples <https://arxiv.org/pdf/1707.07397.pdf>`_

*Exemples de code*

* `generative-models <https://github.com/wiseodd/generative-models>`_ :
  programme sur une grande variété de GAN (Vanilla, Conditional, f-GAN, ...)
  avec :epkg:`tensorflow` et :epkg:`pytorch`

|pystatpng|

Deep Trees
++++++++++

L'apprentissage des réseaux de neurones reposent sur des méthodes
de gradient, différent, celui des arbres permet de prendre en compte des
features non continues et ne sont pas soumis aux problèmes d'échelle.
L'association *deep learning* - *deep neural network* était jusque là implicite,
il faut maintenant compter avec les forêts d'arbres.

*Notebooks*

(à venir)

*Lectures*

* `Unsupervised Learning of Task-Specific Tree Structures with Tree-LSTMs <https://arxiv.org/abs/1707.02786>`_
* `Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks <https://arxiv.org/abs/1503.00075>`_
  (ci-dessous : lien vers une implémentation)
* `Deep Forest: Towards An Alternative to Deep Neural Networks <https://arxiv.org/pdf/1702.08835.pdf>`_

*Modules*

* `tree_rnn (python) <https://github.com/ofirnachum/tree_rnn>`_ : pas de modules encore,
  des implémentatations partagées sur GitHub
* `treelstm <https://github.com/stanfordnlp/treelstm>`_ (java + `Torch <https://github.com/torch/torch7>`_)

|pystatpng|

Deep Nearest Neighbours
+++++++++++++++++++++++

(*à venir*)

*Lectures*

* `Learning Deep Nearest Neighbor Representations Using Differentiable Boundary Trees <https://arxiv.org/abs/1702.08833>`_

------------------

.. _l-td2a-nlp:

Texte - Natural Language Processing - NLP
=========================================

Beaucoup des méthodes performantes reposent sur le
deep learning aujourd'hui, que ce soit pour le texte,
les images ou le son.

.. contents::
    :local:
    :depth: 1

|pyecopng| |pystatpng|

Traitement du langage
+++++++++++++++++++++

Cette partie regroupe principalement des techniques
relevant du `word embedding <https://en.wikipedia.org/wiki/Word_embedding>`_ qui
consiste à convertir des données textuelles en données numériques directement
exploitable par les algorithmes d'apprentissage.

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_nlp

*Lectures*

* `Système de complétion <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_nlp/completion.html>`_ :
  la complétion est utilisée par tous les sites Internet pour aider les utilisateurs
  à saisir leur recherche. N'importe quel site commercial l'utiliser
  pour guider les utilisateurs plus rapidement vers le produit qu'ils recherchent.
* `Text Understanding from Scratch <https://arxiv.org/abs/1502.01710>`_, Xiang Zhang, Yann LeCun
* `Text Generation With LSTM Recurrent Neural Networks in Python with Keras <http://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/>`_
* `Supervised Word Mover's Distance <https://papers.nips.cc/paper/6139-supervised-word-movers-distance.pdf>`_
* `Probabilistic Context-Free Grammars (PCFGs) <http://www.cs.columbia.edu/~mcollins/courses/nlp2011/notes/pcfgs.pdf>`_
* `A Roundup of Recent Text Analytics and Vis Work <http://blogger.ghostweather.com/2014/10/a-roundup-of-recent-text-analytics-and.html>`_
* `A Joint Model for Entity Analysis: Coreference, Typing, and Linking <http://www.cs.utexas.edu/~gdurrett/papers/durrett-klein-tacl2014.pdf>`_
* `Disfluency Detection with a Semi-Markov Model and Prosodic Features <http://www.cs.utexas.edu/~gdurrett/papers/ferguson-durrett-klein-naacl2015.pdf>`_
* `Capturing Semantic Similarity for Entity Linking with Convolutional Neural Networks <http://www.cs.utexas.edu/~gdurrett/papers/mfl-durrett-klein-naacl2016.pdf>`_
* `Neural CRF Parsing <http://www.cs.utexas.edu/~gdurrett/papers/durrett-klein-acl2015.pdf>`_
* `Less Grammar More Features <http://www.cs.utexas.edu/~gdurrett/papers/hall-durrett-klein-acl2014.pdf>`_
* `Learning-Based Single-Document Summarization with Compression and Anaphoricity Constraints <https://arxiv.org/pdf/1603.08887v1.pdf>`_
* `Multimodal Word Distributions <http://www.aclweb.org/anthology/P/P17/P17-1151.pdf>`_

*Lectures - revue*

* `October Edition: Text Understanding - 9 Must-Read Articles <https://towardsdatascience.com/october-edition-text-understanding-c3594faf2964>`_

*Lectures - Classification*

* `Bag of Tricks for Efficient Text Classification <https://arxiv.org/pdf/1607.01759.pdf>`_

*Lectures - word2vec*

* `The amazing power of word vectors <https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/>`_
* `Towards a continuous modeling of natural language domains <http://www.aclweb.org/anthology/W/W16/W16-6012.pdf>`_
* `Efficient Estimation of Word Representations in Vector Space <http://arxiv.org/abs/1301.3781>`_, Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean,
  `Distributed Representations of Words and Phrases and their Compositionality <http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf>`_, Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, Jeff Dean,
  `word2vec Parameter Learning Explained <http://arxiv.org/abs/1411.2738>`_, Xin Rong,
  `Tutorial on Auto-Encoders <http://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_, Piotr Mirowski
* `Mixing Dirichlet Topic Models and Word Embeddings to Make lda2vec <https://arxiv.org/abs/1605.02019>`_

*Lectures - glove*

* `GloVe: Global Vectors for Word Representation <https://nlp.stanford.edu/pubs/glove.pdf>`_ (pdf),
  `GloVe: Global Vectors for Word Representation <https://blog.acolyer.org/2016/04/22/glove-global-vectors-for-word-representation/>`_ (article de blog)
* `glove <https://nlp.stanford.edu/projects/glove/>`_
  (`Glove avec R <https://cran.r-project.org/web/packages/text2vec/vignettes/glove.html>`_,
  `Glove avec python <https://github.com/maciejkula/glove-python>`_)

*Lectures - vidéo*

* :ref:`Cours de deep learning appliqués au NLP <blog-stanford-nlp-deep>`

*Word embedding*

* `On word embeddings - Part 1 <http://sebastianruder.com/word-embeddings-1/index.html>`_
* `On word embeddings - Part 2: Approximating the Softmax <http://sebastianruder.com/word-embeddings-softmax/index.html>`_
* `On word embeddings - Part 3: The secret ingredients of word2vec <http://sebastianruder.com/secret-word2vec/index.html>`_
* `From Word Embeddings To Document Distances <http://jmlr.org/proceedings/papers/v37/kusnerb15.pdf>`_

*Interprétation*

* `Learning to Parse and Translate Improves Neural Machine Translation <http://www.aclweb.org/anthology/P/P17/P17-2012.pdf>`_
* `Skip-Gram – Zipf + Uniform = Vector Additivity <http://www.aclweb.org/anthology/P/P17/P17-1007.pdf>`_

*Résumé*

* `Beyond SumBasic: Task-Focused Summarization with Sentence Simplification and Lexical Expansion <http://www.cis.upenn.edu/~nenkova/papers/ipm.pdf>`_
* `ROUGE: A Package for Automatic Evaluation of Summaries <http://www.aclweb.org/anthology/W04-1013>`_

*Vidéos*

* `Modern NLP in Python <https://www.youtube.com/watch?v=6zm9NC9uRkk>`_

*Modules ML*

* `nltk <http://www.nltk.org/>`_
* `gensim <https://radimrehurek.com/gensim/>`_
* `fasttext <https://github.com/facebookresearch/fastText>`_ (Facebook)
* `spacy <https://spacy.io/>`_
* `thinc <https://github.com/explosion/thinc>`_
* `Stanford CoreNLP <http://stanfordnlp.github.io/CoreNLP/other-languages.html#python>`_,
  `corenlpy <https://github.com/enewe101/corenlpy>`_
* `lda2vec <https://github.com/cemoody/lda2vec>`_
* `glove-python <https://github.com/maciejkula/glove-python>`_
* `tethne <http://diging.github.io/tethne/>`_
* `torchtext <https://github.com/pytorch/text>`_
* `pycantonese <http://pycantonese.org/>`_ (texte cantonnais),
   `snownlp <https://github.com/isnowfy/snownlp>`_ (texte Chinois),
   `jieba <https://github.com/fxsjy/jieba>`_ (tokenizer pour le chinois)
* `polyglot <https://github.com/aboSamoor/polyglot>`_ : fonctionne
  pour beaucoup de langues
* `pattern <https://github.com/clips/pattern>`_ : possède une bonne base
  d'exemples, notemmant pour récupérer des données depuis internet
  `01-web <https://github.com/clips/pattern/tree/master/examples/01-web>`_

*Modules moins ML*

* `python-rake <https://pypi.python.org/pypi/python-rake/>`_ : petit module pour extraire des mot-clés
* `sumy <https://pypi.python.org/pypi/sumy>`_ : construction automatique d'un résumé d'un texte
* `pyrouge <https://github.com/pltrdy/rouge/>`_ : calcule de la métrique `ROUGE <https://en.wikipedia.org/wiki/ROUGE_(metric)>`_

|pystatpng|

Traduction automatique
++++++++++++++++++++++

(*à venir*)

Cette partie concerne les *SMT* ou
`Statistical machines translation <https://en.wikipedia.org/wiki/Statistical_machine_translation>`_
qui évoque l'apprentissage supervisé d'un modèle de traduction automatique de texte principalement.

*Lectures*

* `Machine Learning is Fun Part 5: Language Translation with Deep Learning and the Magic of Sequences <https://medium.com/@ageitgey/machine-learning-is-fun-part-5-language-translation-with-deep-learning-and-the-magic-of-sequences-2ace0acca0aa>`_
* `Dual Learning for Machine Translation <https://papers.nips.cc/paper/6469-dual-learning-for-machine-translation.pdf>`_
* `Neural Machine Translation by Jointly Learning to Align and Translate <https://arxiv.org/abs/1409.0473>`_
* `Sequence-to-Dependency Neural Machine Translation <http://www.aclweb.org/anthology/P/P17/P17-1065.pdf>`_

*Startup*

* `DeepL <https://www.deepl.com/>`_

*Modules*

|pystatpng|

Tagging
+++++++

Le tagging consiste à prédire un label pour chacun des mots d'une phrase.
C'est ce qu'on veut faire lorsqu'on considère un problème de
`Named Entity Recognition (NER) <https://en.wikipedia.org/wiki/Named-entity_recognition>`_.
On souhaite reconnaître dans une phrase s'il y a une ville, un lieu, un téléphone,
une adresse. La difficulté consiste à intégrer un contexte dans la décision,
c'est-à-dire de considérer la séquence des mots et non les mots pris séparément.
*Paris* peut aussi bien être une ville que le mot *pari* au pluriel.
Ce problème a longtemps été traité avec des outils de statistiques
classiques tels que `Hidden Marko Models (HMM) <https://en.wikipedia.org/wiki/Hidden_Markov_model>`_ ou les
`Conditional Random Fields (CRF) <https://en.wikipedia.org/wiki/Conditional_random_field>`_.
Les meilleurs modèles sont des modèles de deep learning
`LSTM <https://en.wikipedia.org/wiki/Long_short-term_memory>`_.

(*à venir*)

*Lectures*

* `Understanding LSTM Networks <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>`_

*Modules*

* `NLTK.tag <http://www.nltk.org/api/nltk.tag.html>`_
* `hmmlearn <https://github.com/hmmlearn/hmmlearn>`_
* `sklearn-crfsuite <https://sklearn-crfsuite.readthedocs.io/en/latest/>`_
* `spacy - entity recognition <https://spacy.io/docs/usage/entity-recognition>`_
* `tagger <https://github.com/glample/tagger>`_
* `MITIE <https://github.com/mit-nlp/MITIE>`_ (le module n'a pas l'air d'être vraiment maintenu)

*Modules deep learning*

* `LightRNN <https://github.com/Microsoft/CNTK/tree/master/Examples/Text/LightRNN>`_
* `pytorch - bi-LSTM CRF <http://pytorch.org/tutorials/beginner/nlp/advanced_tutorial.html>`_

*Expérimental*

* `NeuroNER <https://github.com/Franck-Dernoncourt/NeuroNER>`_

------------------

Images / Vidéos / Sons
======================

Il est difficile d'aborder cette partie sans savoir ce qu'est
le :ref:`l-deep-learning`.

|pystatpng|

Classification
++++++++++++++

(*à venir*)

*Lectures*

* `VGG Convolutional Neural Networks Practical <http://www.robots.ox.ac.uk/~vgg/practicals/cnn/>`_
* `Image-to-Image Translation with Conditional Adversarial Networks <https://arxiv.org/pdf/1611.07004.pdf>`_,
  `Image to Image demo <http://affinelayer.com/pixsrv/index.html>`_
* `Image-to-Image Translation with Conditional Adversarial Networks <https://arxiv.org/pdf/1611.07004v1.pdf>`_
* `How to Train a GAN? Tips and tricks to make GANs work <https://github.com/soumith/ganhacks?imm_mid=0ec69d&cmp=em-data-na-na-newsltr_ai_20170123>`_
* `Towards Principled Methods for Training Generative Adversarial Networks <https://arxiv.org/abs/1701.04862>`_
* `Instance Noise: A trick for stabilising GAN training <http://www.inference.vc/instance-noise-a-trick-for-stabilising-gan-training/>`_
* `Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network <https://arxiv.org/abs/1609.05158>`_
* `YOLO9000: Better, Faster, Stronger <https://arxiv.org/abs/1612.08242>`_ : détection en temps
  d'objets sur des images ou dans une vidéo, le code est sur github
  `darknet <https://github.com/pjreddie/darknet>`_, wrapper Python :
  `darknetpy <https://github.com/danielgatis/darknetpy>`_,
  `demo <https://pjreddie.com/darknet/yolo/>`_
* `SSD: Single Shot MultiBox Detector <https://arxiv.org/abs/1512.02325>`_
  (voir aussi `caffe/ssd <https://github.com/weiliu89/caffe/tree/ssd>`_)
* `HPatches: A benchmark and evaluation of handcrafted and learned local descriptors <http://www.robots.ox.ac.uk/~vgg/publications/2017/Balntas17/balntas17.pdf>`_
* `Learning Transferable Architectures for Scalable Image Recognition <https://arxiv.org/abs/1707.07012>`_

*Algorithmes*

* `Viola–Jones object detection framework <https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework>`_
* `Histograms of Oriented Gradients for Human Detection (HOG) <http://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf>`_
* `One Millisecond Face Alignment with an Ensemble of Regression Trees <http://www.csc.kth.se/~vahidk/papers/KazemiCVPR14.pdf>`_,
  `Github/AndrejMaris/facefit <https://github.com/AndrejMaris/facefit>`_
* `ageitgey/step-2a_finding-face-landmarks.py <https://gist.github.com/ageitgey/ae340db3e493530d5e1f9c15292e5c74>`_

*Outils*

* `Image Descriptors <https://en.wikipedia.org/wiki/Visual_descriptor>`_,
  `Speeded up robust features (SURF) <https://en.wikipedia.org/wiki/Speeded_up_robust_features>`_,
  `Scale-invariant feature transform (SIFT) <https://en.wikipedia.org/wiki/Scale-invariant_feature_transform>`_,

*Modules*

* `VIGRA <https://github.com/ukoethe/vigra>`_
* `opencv <http://opencv.org/>`_
* `dlib <https://github.com/davisking/dlib>`_
* `hed <https://github.com/s9xie/hed>`_ (Holistically-Nested Edge Detection)
* `bob.bio <http://pythonhosted.org/bob.bio.base/index.html>`_
* tous les modules de :ref:`l-deep-learning`
* `plat <https://github.com/dribnet/plat>`_
  (Utilities for exploring generative latent spaces as described in the
  `Sampling Generative Networks <https://arxiv.org/abs/1609.04468>`_ paper.)
* `darknetpy <https://github.com/danielgatis/darknetpy>`_

*Modèles pré-entraînés*

* `VGG16 model for Keras <https://gist.github.com/baraldilorenzo/07d7802847aaad0a35d3>`_,
  `VGG in TensorFlow <https://www.cs.toronto.edu/~frossard/post/vgg16/>`_,
  `Very Deep Convolutional Networks for Large-Scale Visual Recognition <http://www.robots.ox.ac.uk/~vgg/research/very_deep/>`_

|pystatpng|

Détection d'objets
++++++++++++++++++

(*à venir*)

*Lectures*

* `YOLO: Real-Time Object Detection <https://pjreddie.com/darknet/yolo/>`_
* `Fast R-CNN: Fast Region-based Convolutional Networks for object detection <https://github.com/rbgirshick/fast-rcnn>`_

|pystatpng|

Segmentation
++++++++++++

La segmentation d'images consiste à isoler des zones d'intérêt dans une image.
Cela peut être un visage, des silhouettes, des objets. C'est encore un domaine
où le deep learning a permis de faire des grandes avancées. L'objectif est assez similaire
à la segmentation d'images si ce n'est qu'on cherche à déterminer les zones
d'intérêt au pixel près.

(*à venir*)

*Lectures*

* `Watershed <https://en.wikipedia.org/wiki/Watershed_(image_processing)>`_
* `Semantic Segmentation using Fully Convolutional Networks over the years <https://meetshah1995.github.io/semantic-segmentation/deep-learning/pytorch/visdom/2017/06/01/semantic-segmentation-over-the-years.html>`_
* `Fully Convolutional Networks for Semantic Segmentation <https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf>`_

*Modules*

* `opencv - watershed <http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_watershed/py_watershed.html>`_
* `torch-vision <https://github.com/warmspringwinds/vision/tree/5e0a760fc847d55a4c1699410a14003452fa4581>`_
* `pytorch-semseg <https://github.com/meetshah1995/pytorch-semseg>`_

|pystatpng|

Génération d'images
+++++++++++++++++++

(*à venir*)

*Lectures*

* `Machine Learning is Fun Part 7: Abusing Generative Adversarial Networks to Make 8-bit Pixel Art <https://medium.com/@ageitgey/abusing-generative-adversarial-networks-to-make-8-bit-pixel-art-e45d9b96cee7>`_

Vidéos
++++++

(*à venir*)

*Modules*

* `scikit-video <https://github.com/aizvorski/scikit-video>`_

|pystatpng|

Reconnaissance de la parole
+++++++++++++++++++++++++++

(*à venir*)

*Lectures*

* `Machine Learning is Fun Part 6: How to do Speech Recognition with Deep Learning <https://medium.com/@ageitgey/machine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a>`_
* `Probabilistic Linear Discriminant Analysis for Inferences About Identity <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.97.6491&rep=rep1&type=pdf>`_,
  `shrinkage <http://scikit-learn.org/stable/modules/lda_qda.html#shrinkage>`_
* `Probabilistic Linear Discriminant Analysis for Acoustic Modelling <http://www.cstr.ed.ac.uk/downloads/publications/2014/plda-spl2014.pdf>`_

*Modules*

* `bob.bio <http://pythonhosted.org/bob.bio.base/index.html>`_
* `kaldi <https://github.com/kaldi-asr/kaldi>`_ (reconnaissance de la parole)

-------------------------

Galleries de problèmes résolus ou presque
=========================================

Cette rubrique étend la liste des références avec des articles
exposant des méthodes de machine learning appliquées à des problèmes
précis.

.. contents::
    :local:

Adversarial Examples
++++++++++++++++++++

* `The Limitations of Deep Learning in Adversarial Settings <https://arxiv.org/pdf/1511.07528v1.pdf>`_

Architecture de Deep Learning
+++++++++++++++++++++++++++++

* `Neural Network Zooo Prequel: Cells and Layers <http://www.asimovinstitute.org/neural-network-zoo-prequel-cells-layers/>`_ :
  revue d'architectures de réseaux de neurones

Compétitions et datasets
++++++++++++++++++++++++

* `ImageNet <http://www.image-net.org/>`_
* `SQuAD The Stanford Question Answering Dataset <https://rajpurkar.github.io/SQuAD-explorer/>`_

Fraudes
+++++++

*  `Detecting Fraudulent Personalities in Networks of Online Auctioneers <http://www.cs.cmu.edu/~dchau/papers/auction_fraud_pkdd06.pdf>`_

Deep Learning Artistique
++++++++++++++++++++++++

* `Pramit Choudhary - Learn to be a painter using Neural Style Painting <https://www.youtube.com/watch?v=WXDr5H1hVOU&list=PLGVZCDnMOq0rxoq9Nx0B4tqtr891vaCn7&index=60>`_ (vidéo)
* `Visual Attribute Transfer through Deep Image Analogy <https://arxiv.org/abs/1705.01088>`_
* `Coherent Online Video Style Transfer <https://arxiv.org/abs/1703.09211>`_
* `StyleBank: An Explicit Representation for Neural Image Style Transfer <https://arxiv.org/abs/1703.09210>`_
* `msracver/Deep-Image-Analogy <https://github.com/msracver/Deep-Image-Analogy>`_

Images
++++++

Les réseaux de neurones profonds fonctionnent très bien sur les images
car ce sont des entrées homogènes. Le traitement des images
cachent plusieurs types de problématiques :

* **classification** : reconnaître un object dans l'image sans savoir extactement où il est
* **segmentation** : reconnaître des objects dans une images, sous la forme de boîtes
  englobantes ou au pixel près
* **transformation** : déflouter, extraire le squelette, mettre en couleur,
  fusionner image et style

Ce ne sont pas les seules mais ces problématiques commencent à être
assez bien résolus. Il faut noter qu'on n'utilisent pas mêmes modèles
s'il s'agit d'images prises par un appareil photos ou d'images médicales.

* `Time-Contrastive Networks: Self-Supervised Learning from Multi-View Observation <https://arxiv.org/abs/1704.06888>`_ :
  un robot apprend à imiter les mouvements d'une personne
  (`vidéo <https://sermanet.github.io/tcn/>`_)
* `Device Placement Optimization with Reinforcement Learning <https://arxiv.org/pdf/1706.04972.pdf>`_
* `Automatic Colorization <http://tinyclouds.org/colorize/>`_
* `Image Completion <http://bamos.github.io/2016/08/09/deep-completion/>`_
* `Perceptual Losses for Real-Time Style Transfer and Super-Resolution <https://arxiv.org/pdf/1603.08155.pdf>`_,
  article : `neural-style <https://jayanthkoushik.github.io/neural_style.html>`_,
  code : `neural-style <https://github.com/jayanthkoushik/neural-style>`_.
* `Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network <https://arxiv.org/pdf/1609.04802.pdf>`_ :
  entraîner un réseau de neurones pour améliorer la netteté des images
* `YOLO9000: Better, Faster, Stronger <https://arxiv.org/abs/1612.08242>`_ : détection en temps
  d'objets sur des images ou dans une vidéo, le code est sur github
  `darknet <https://github.com/pjreddie/darknet>`_, wrapper Python :
  `darknetpy <https://github.com/danielgatis/darknetpy>`_,
  `demo <https://pjreddie.com/darknet/yolo/>`_
* `openalpr <https://github.com/openalpr/openalpr>`_ :
  reconnaissance de plaques d'immatriculation, pas vraiment du deep learning
* `Fully Convolutional Networks for Semantic Segmentation <https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf>`_
* `Deep Supervision with Shape Concepts for Occlusion-Aware 3D Object Parsing <https://arxiv.org/pdf/1612.02699.pdf>`_

Histoire
++++++++

* `Revisiting Unreasonable Effectiveness of Data in Deep Learning Era <https://arxiv.org/pdf/1707.02968.pdf>`_

Jeux
++++

* `Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm <https://arxiv.org/pdf/1712.01815.pdf>`_,
  voir quelques parties `The future is here - AlphaZero learns chess <https://en.chessbase.com/post/the-future-is-here-alphazero-learns-chess>`_.
  Avec ce type d'algorithme adapté à la finance, le trader humain a du soucis à se faire.

Portraits
+++++++++

* `Face Segmentation <https://github.com/YuvalNirkin/face_segmentation>`_ :
  il est plus facile de déterminer une boîte englobante autour d'un visage,
  le modèle référencé extrait un visage au pixel près
* `FaderNetworks <https://github.com/facebookresearch/FaderNetworks>`_ :
  vieillir un visage, rajeunir, ajouter des lunettes, ce réseaux de neurones a été
  appris pour transformer un portrait
  (données : `Large-scale CelebFaces Attributes (CelebA) Dataset <http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html>`_)

Réseaux Sociaux
+++++++++++++++

* `Social Clicks: What and Who Gets Read on Twitter? <https://hal.inria.fr/hal-01281190/document>`_

Retail
++++++

* `Data Mining Problems in Retail <https://highlyscalable.wordpress.com/2015/03/10/data-mining-problems-in-retail/>`_

Texte / Traduction
++++++++++++++++++

* `Neural Machine Translation (seq2seq) Tutorial <https://github.com/tensorflow/nmt>`_
* `Representing Sentences as Low-Rank Subspaces <https://arxiv.org/abs/1704.05358v1>`_
* `SQuAD: 100,000+ Questions for Machine Comprehension of Text <https://arxiv.org/abs/1606.05250>`_,
  cette compétition fera sans doute émerger la nouvelle version des moteurs de recherche.
* `whatthelang <https://github.com/indix/whatthelang>`_ :
  module Python pour reconnaître la langue d'un texte,
  s'appuie sur :epkg:`FastText`

Voiture autonome
++++++++++++++++

* `Computer Vision for Autonomous Vehicles: Problems, Datasets and State-of-the-Art <https://arxiv.org/abs/1704.05519>`_

Notebooks
+++++++++

*CNTK*

* `Complex Neural Network Data Modelling with CNTK <http://dacrook.com/complex-neural-network-data-modelling-with-cntk/>`_

*Keras*

* `Using a pre-trained convnet <https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.3-using-a-pretrained-convnet.ipynb>`_
