
.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-ml2a-survival-analysis:

Survival Analysis
+++++++++++++++++

L'analyse de survie couvre une façon de modéliser les problèmes
qui répond à une problématique assez fréquente dans les données
liés aux événements. Lorsqu'on cherche à prédire si un individu
peut ou non voir son cancer récidiver, le fait de savoir que cela ne
s'est pas produit ne veut pas dire ce que cela ne se produira pas.
Des données sont manquantes en quelque sorte puisque la réponse à
prédire n'est pas toujours connue. On sait juste qu'elle ne
s'est pas encore produite. L'analyse de survie nécessite de prendre
en compte la date à laquelle les données ont été récoltées et la
date à laquelle on cherche à prédire. On ne peut pas prédire
si un cancer reviendra mais on peut prédire s'il reviendra
en deça d'un certain laps de temps.

*Notebooks*

*(à venir)*

*Lectures*

* `Introduction to Survival Analysis
  <http://www.stat.columbia.edu/~madigan/W2025/notes/survival.pdf>`_
* `Survival Analysis Part A
  <https://towardsdatascience.com/survival-analysis-part-a-70213df21c2e>`_
* `Introduction to Survival Analysis with scikit-survival
  <https://scikit-survival.readthedocs.io/en/stable/user_guide/00-introduction.html>`_
* `Cox Regression
  <https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Cox_Regression.pdf>`_
* `Learning Transformation Models for Ranking and Survival Analysis
  <https://jmlr.org/papers/volume12/vanbelle11a/vanbelle11a.pdf>`_
* `Time-to-Event Prediction with Neural Networks and Cox Regression
  <https://jmlr.org/papers/volume20/18-424/18-424.pdf>`_
* `Effective Ways to Build and Evaluate Individual Survival Distributions
  <https://www.jmlr.org/papers/volume21/18-772/18-772.pdf>`_
* `Estimateur de Kaplan-Meier
  <https://fr.wikipedia.org/wiki/Estimateur_de_Kaplan-Meier>`_
* `Regression de Cox
  <https://fr.wikipedia.org/wiki/R%C3%A9gression_de_Cox>`_

*Livres*

* David G. Kleinbaum and Mitchel Klein (2012), Survival Analysis: A Self-Learning Text, Springer.
* John P. Klein and Melvin L. Moeschberger (2003),
  Survival Analysis: Techniques for Censored and Truncated Data, Springer.
  `pdf <http://sistemas.fciencias.unam.mx/~ediaz/Cursos/Estadistica3/Libros/0a9X.pdf>`_

*Modules*

* `lifelines <https://github.com/CamDavidsonPilon/lifelines>`_
* `scikit-survival <https://scikit-survival.readthedocs.io/en/stable/index.html>`_
* `pycox <https://github.com/havakv/pycox>`_
