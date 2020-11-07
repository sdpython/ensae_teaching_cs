
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

*Modules*

* `lifelines <https://github.com/CamDavidsonPilon/lifelines>`_
