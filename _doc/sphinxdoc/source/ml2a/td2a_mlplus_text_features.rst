
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-ml2a-text-features:

Du texte aux features
+++++++++++++++++++++

Ces méthodes sont non-supervisées et apparaissent
le plus souvent comme prétraitements pour convertir
le texte sous forme de features numériques ou
tout simplement des vecteurs. On parlera ici de texte
comme texte libre et non simplement une variable catégorielle
représentée sous forme de texte.

*Notebooks*

* :ref:`td2asentimentanalysisrst` (:ref:`correction <td2asentimentanalysiscorrectionrst>`)

.. index:: word2vec, glove, tf-idf

*Lectures*

* `Texte et catégories <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/preprocessing.html#texte-categorie>`_
* `Texte comme une séquence de mots <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/preprocessing.html#texte-sequence>`_
* `tf-idf <https://en.wikipedia.org/wiki/Tf%E2%80%93idf>`_
* `Efficient Estimation of Word Representations in Vector Space <https://arxiv.org/abs/1301.3781>`_
* `GloVe: Global Vectors for Word Representation <https://nlp.stanford.edu/pubs/glove.pdf>`_
* `Multi-label Text Classification using BERT - The Mighty Transformer <https://medium.com/huggingface/multi-label-text-classification-using-bert-the-mighty-transformer-69714fa3fb3d>`_

*Modules*

* :epkg:`gensim`
* :epkg:`spacy` (:ref:`ressources spacy <spacy-ressource>`)
* :epkg:`nltk`
* :epkg:`scikit-learn`
* `glove sur GitHub <https://github.com/stanfordnlp/GloVe>`_
