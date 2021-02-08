
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Text Embedding (NLP)
++++++++++++++++++++

Les modèles de machine learning n'acceptent que des
entrées numériques. Il faut nécessairement convertir
le texte d'une manière ou d'une autre en vecteurs
et si possible dans un espace vectoriel de dimension fixe.
Il faut donc passer d'un texte de longueur variable
à un vecteur de dimension fixe.
La section :ref:`l-ml2a-text-features` détaille les
méthodes les plus courantes. La section
:ref:`l-td2a-nlp` explore d'autres directions.

*Lectures*

* `Google Brain Introduces Symbolic Programming + PyGlove Library to Reformulate AutoML
  <https://medium.com/huggingface/encoder-decoders-in-transformers-a-hybrid-pre-trained-architecture-for-seq2seq-af4d7bf14bb8>`_
* `Encoder-decoders in Transformers: a hybrid pre-trained architecture for seq2se
  <https://medium.com/huggingface/encoder-decoders-in-transformers-a-hybrid-pre-trained-architecture-for-seq2seq-af4d7bf14bb8>`_

*Modules*

* `spacy <https://spacy.io/>`_
* `gensim <https://radimrehurek.com/gensim/>`_
* *HuggingFace*:
  * `huggingface/transformers <https://github.com/huggingface/transformers>`_
    (State-of-the-art Natural Language Processing for PyTorch and TensorFlow 2.0)
  * `tokenizers <https://github.com/huggingface/tokenizers>`_
    (Provides an implementation of today's most used tokenizers,
    with a focus on performance and versatility.)
* `pyglove <https://github.com/Lguyogiro/pyglove>`_