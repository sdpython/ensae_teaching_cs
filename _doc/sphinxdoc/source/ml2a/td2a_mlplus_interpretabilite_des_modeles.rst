
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-interpretabilite-ml:

Interprétabilité des modèles
++++++++++++++++++++++++++++

.. index:: transparence, protection des données, loi européenne, LIME

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

.. index:: LIME

Ces approches sont principalement macro et permettent de construire
une vue d'ensemble. Pour étudier un cas particulier, une observation,
on choisira plutôt d'explorer autour d'une observation en changeant
quelques-unes des variables par d'autres valeurs plausibles.
C'est l'idée de l'approche `LIME <https://arxiv.org/abs/1602.04938>`_.
Ces approches sont sensibles au nombre de variables, plus il y a
de dimensions, plus il est difficile de donner du sens à une variable
en particulier quand celle-ci est présente sur quelques observations
seulement.

*Notebooks*

(*à venir*) lime, shap, unified approach,
`partial_dependence <https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html>`_,
`permutation_importance <https://eli5.readthedocs.io/en/latest/blackbox/permutation_importance.html>`_ (bientôt dans scikit-learn 0.22)

* `Interpret scikit-learn machine learning models <https://github.com/glemaitre/scikit-learn-workshop-2019/blob/master/interpretation.ipynb>`_
  (from scikit-learn's consortium workshop)

*Lectures - LIME*

* `"Why Should I Trust You?" Explaining the Predictions of Any Classifier <http://arxiv.org/pdf/1602.04938v1.pdf>`_
  (sans doute un des articles à lire en premier - `lime <https://github.com/marcotcr/lime>`_)
* `Defining Locality for Surrogates in Post-hoc Interpretablity <https://128.84.21.199/abs/1806.07498v1>`_
* `A Unified Approach to Interpreting Model Predictions <http://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf>`_

*Lectures : expliquer*

* `Ideas on interpreting machine learning <https://www.oreilly.com/ideas/ideas-on-interpreting-machine-learning>`_
* `Learning to learn by gradient descent by gradient descent <https://arxiv.org/pdf/1606.04474.pdf>`_
* `Importance Weighting Without Importance Weights: An Efficient Algorithm for Combinatorial Semi-Bandits <http://jmlr.org/papers/volume17/15-091/15-091.pdf>`_
* `Making Tree Ensembles Interpretable <https://arxiv.org/pdf/1606.05390v1.pdf>`_
* `Understanding variable importances in forests of randomized trees <http://papers.nips.cc/paper/4928-understanding-variable-importances-in-forests-of-randomized-trees.pdf>`_
* `Confidence Intervals for Random Forests: The Jackknife and the Infinitesimal Jackknife <http://jmlr.csail.mit.edu/papers/volume15/wager14a/wager14a.pdf>`_
* `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_
* `Wavelet decompositions of Random Forests - smoothness analysis, sparse approximation and applications <http://www.jmlr.org/papers/volume17/15-203/15-203.pdf>`_
* `Edward: A library for probabilistic modeling, inference, and criticism <https://arxiv.org/pdf/1610.09787.pdf>`_
* `Strictly Proper Scoring Rules, Prediction, and Estimation <https://www.cs.duke.edu/courses/spring17/compsci590.2/Gneiting2007jasa.pdf>`_
* `Visualizing and Understanding Neural Machine Translation <http://www.aclweb.org/anthology/P/P17/P17-1106.pdf>`_
* `Multiplicative Multitask Feature Learning <http://jmlr.org/papers/v17/15-234.html>`_
* `Multi-Target Regression with Rule Ensembles <http://www.jmlr.org/papers/volume13/aho12a/aho12a.pdf>`_
* `SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability <https://arxiv.org/pdf/1706.05806.pdf>`_
* `The Myth Of Interpretability of Econometric Models <http://freakonometrics.hypotheses.org/51752>`_
* `Interpretable Policies for Reinforcement Learning by Genetic Programming <https://arxiv.org/abs/1712.04170>`_
* `An Efficient Explanation of Individual Classifications using Game Theory <http://lkm.fri.uni-lj.si/xaigor/slo/pedagosko/dr-ui/jmlr-strumbelj-kononenko.pdf>`_ **
* `How to Explain Individual Classification Decisions <http://www.jmlr.org/papers/volume11/baehrens10a/baehrens10a.pdf>`_
* `Interpretable Machine Learning with XGBoost <https://towardsdatascience.com/interpretable-machine-learning-with-xgboost-9ec80d148d27>`_
* `Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV) <https://arxiv.org/abs/1711.11279>`_,
  `tutorial <https://beenkim.github.io/papers/BeenK_FinaleDV_ICML2017_tutorial.pdf>`_)
* `To Trust Or Not To Trust A Classifier <https://arxiv.org/abs/1805.11783>`_,
  `Mind the Gap: A Generative Approach to Interpretable Feature Selection and Extraction <https://beenkim.github.io/papers/BKim2015NIPS.pdf>`_
* `Interpretation of Neural Networks is Fragile <https://arxiv.org/pdf/1710.10547.pdf>`_

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

*Lectures : assemblage de modèles simples*

* `Intelligible Models for Classification and Regression <http://www.cs.cornell.edu/~yinlou/papers/lou-kdd12.pdf>`_

*Lectures : local*

* `Learning Deep Nearest Neighbor Representations Using Differentiable Boundary Trees <https://arxiv.org/abs/1702.08833>`_

*Lectures : modèle graphique*

* `Factor Graph <http://deepdive.stanford.edu/assets/factor_graph.pdf>`_
* `An Introduction to Conditional Random Fields for Relational Learning <http://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf>`_
* `Factor Graphs and the Sum-Product Algorithm <http://www.comm.utoronto.ca/~frank/papers/KFL01.pdf>`_

*Lectures : erreurs, outliers*

* `BoostClean: Automated Error Detection and Repair for Machine Learning <https://arxiv.org/abs/1711.01299>`_
* `Scorpion: Explaining Away Outliers in Aggregate Queries <http://sirrice.github.io/files/papers/scorpion-vldb13.pdf>`_
* `Outlier Detection Techniques <https://www.siam.org/meetings/sdm10/tutorial3.pdf>`_,
  `abod.py <https://github.com/MarinYoung4596/OutlierDetection/tree/master/OutlierDetection/Python%20Implementation>`_

*Lectures : information bottleneck*

* `Information bottleneck method <https://en.wikipedia.org/wiki/Information_bottleneck_method>`_ (wikipédia)
* `The information bottleneck method <https://arxiv.org/pdf/physics/0004057.pdf>`_
* `Deep Learning and the Information Bottleneck Principle <https://arxiv.org/pdf/1503.02406.pdf>`_
* `Opening the black box of Deep Neural Networks via Information <https://arxiv.org/pdf/1703.00810.pdf>`_

*Lectures : causalité*

.. index:: causalité, causality

* `Machine Learning Methods Economists Should Know About <https://arxiv.org/abs/1903.10075>`_
* `Counterfactual Inference <https://media.neurips.cc/Conferences/NIPS2018/Slides/Counterfactual_Inference.pdf>`_
* `The State of Applied Econometrics: Causality and Policy Evaluation <https://pubs.aeaweb.org/doi/pdfplus/10.1257/jep.31.2.3>`_
* `Estimating Treatment Effects with Causal Forests: An Application <https://arxiv.org/abs/1902.07409>`_

*Vidéos*

* `Explaining behavior of Machine Learning models with eli5 library <http://pyvideo.org/europython-2017/explaining-behavior-of-machine-learning-models-with-eli5-library.html>`_

*Modules*

* `eli5 <https://github.com/TeamHG-Memex/eli5>`_
* `shap <https://github.com/slundberg/shap>`_ (développement actif)
* `edward <http://edwardlib.org/>`_
* `deepdive <http://deepdive.stanford.edu/>`_: ce n'est pas un module python,
  cet outil a été développé pour étudier les relations dans les données et plus
  particulièrement les `dark data <https://en.wikipedia.org/wiki/Dark_data>`_
* `treeinterpreter <https://pypi.python.org/pypi/treeinterpreter>`_
* `lime <https://github.com/marcotcr/lime>`_ (`notebooks <https://github.com/marcotcr/lime/tree/master/doc/notebooks>`_)
* `ml-insights <https://ml-insights.readthedocs.io/en/latest/>`_ :
  méthode empiriques pour observer les prédictions en fonctions
  de variations des features
* `savvy <https://github.com/lmc2179/savvy>`_

*Modules de visualisation*

* `Netron <https://github.com/lutzroeder/Netron>`_ : cet outil n'explique pas vraiment
  mais permet de visualiser des modèles de machine learning.
* `VisualDL <https://github.com/PaddlePaddle/VisualDLn>`_ : cet outil n'explique pas vraiment
  mais permet de visualiser des modèles de deep learning.

*A suivre*

* `Been Lim <https://beenkim.github.io/>`_
