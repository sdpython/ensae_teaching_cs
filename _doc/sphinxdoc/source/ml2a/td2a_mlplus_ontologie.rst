
.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Ontologie
+++++++++

Il existe des méthodes efficaces pour faire du clustering de texte,
chaque cluster illustre un groupe de document parlant du même sujet
avec les mêmes termes, si possible un concept.
Une *ontologie* implique en plus des relations de sous-concept.
On ne cherche pas seulement à déterminer les concepts principaux
mais aussi les ramifications. Cela peut être le style de cuisine,
cuisine française, la région, ... et ainsi de suite. Une *ontologie*
peut être vu comme une nomenclature à plusieurs étages.
Est-il possible de construire une telle structure de façon automatique ?

*Lectures*

* `Ontology-based Top-N Recommendations on New Items with Matrix Factorization <https://pdfs.semanticscholar.org/dc42/b2bec435fad0b1e66172c434edc03ff1c419.pdf>`_
* `Ontology-Based Collaborative Recommendation <http://ceur-ws.org/Vol-606/paper2.pdf>`_
* `YAGO: A Large Ontology from Wikipedia and WordNet <https://classes.soe.ucsc.edu/cmps140/Winter11/papers/yago-ontology-jws2008.pdf>`_
* `PARIS: Probabilistic Alignment of Relations, Instances, and Schema <https://arxiv.org/pdf/1111.7164.pdf>`_
* `Ontology Learning <https://userpages.uni-koblenz.de/~staab/Research/Publications/2009/handbookEdition2/ontology-learning-handbook2.pdf>`_
* `An automatic taxonomy of galaxy morphology using unsupervised machine learning <https://arxiv.org/pdf/1709.05834.pdf>`_

*Site web*

* `PARIS - Probabilistic Alignment of Relations, Instances, and Schema <http://webdam.inria.fr/paris/>`_
* `MOLE - Machine Learning and Ontology Engineering <http://aksw.org/Groups/MOLE.html>`_

*Module*

* `Owlready2 <https://pypi.python.org/pypi/Owlready2>`_ (pas de machine learning)
* `rdflib <https://github.com/RDFLib/rdflib>`_
