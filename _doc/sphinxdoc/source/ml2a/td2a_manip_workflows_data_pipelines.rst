
.. |pyecopng| image:: ../_static/pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: ../_static/pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

|pystatpng|

Workflows - Data Pipelines
++++++++++++++++++++++++++

Au fur et à mesure qu'une société construire des modèles
de machine learning pour automatiser certaines parties de
traitement de données, il devient important de rafraîchir
ces modèles avec des données plus récentes. On se retrouve vite
avec une multitud de besoins comme automatiser,
garder la trace des précédentes exécutions,
paralléliser sur plusieurs machines ou infrastructures,
garder une vue exhaustive et simple de toute cette complexité
croissante. La dénomination communue est *pipeline* ou
*workflow* et cet ensemble de traitements est souvent
représenté sous formes de graphe où chaque arc
symbolise une dépendances entre deux traitements de données.
Chaque société a développé ses propres outils,
certaines l'ont mis à disposition de façon open source.
Cette partie vise à présenter l'une d'entre elles.

(*à venir*)

*Lectures*

* `Luigi vs Airflow vs Pinball <http://bytepawn.com/luigi-airflow-pinball.html>`_
* `Luigi vs Airflow vs zope.wfmc: Comparison of Open-Source Workflow Engines <https://medium.com/@cyrusv/luigi-vs-airflow-vs-zope-wfmc-comparison-of-open-source-workflow-engines-de5209e6dac1>`_
* `Airflow Tutorial for Data Pipelines <https://blog.godatadriven.com/practical-airflow-tutorial>`_

*Modules*

* `airflow <https://airflow.apache.org/>`_
* `luigi <https://github.com/spotify/luigi>`_
* `pinball <https://github.com/pinterest/pinball>`_
