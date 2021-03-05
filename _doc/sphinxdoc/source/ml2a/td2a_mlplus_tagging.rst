
.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

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
* `Establishing a New State-of-the-Art for French Named Entity Recognition
  <https://hal.inria.fr/hal-02617950/file/lrec19ner.pdf>`_
* `Extracting an Etymological Database from Wiktionary
  <https://hal.inria.fr/hal-01592061/file/paper44.pdf>`_
* `Cheating a Parser to Death: Data-driven Cross-Treebank Annotation Transfer
  <https://hal.inria.fr/hal-01798801/file/1101.pdf>`_

*Modules*

* `NLTK.tag <http://www.nltk.org/api/nltk.tag.html>`_
* `hmmlearn <https://github.com/hmmlearn/hmmlearn>`_
* `sklearn-crfsuite <https://sklearn-crfsuite.readthedocs.io/en/latest/>`_
* `spacy - entity recognition <https://spacy.io/docs/usage/entity-recognition>`_,
  voir aussi :ref:`ressources spacy <spacy-ressource>`
* `tagger <https://github.com/glample/tagger>`_
* `MITIE <https://github.com/mit-nlp/MITIE>`_ (le module n'a pas l'air d'être vraiment maintenu)
* `stanza <https://github.com/stanfordnlp/stanza>`_

*Modules deep learning*

* `LightRNN <https://github.com/Microsoft/CNTK/tree/master/Examples/Text/LightRNN>`_
* `pytorch - bi-LSTM CRF <http://pytorch.org/tutorials/beginner/nlp/advanced_tutorial.html>`_

*Expérimental*

* `NeuroNER <https://github.com/Franck-Dernoncourt/NeuroNER>`_

.. index:: corpus

*Corpus*

* `https://camembert-model.fr/ <https://camembert-model.fr/>`_
