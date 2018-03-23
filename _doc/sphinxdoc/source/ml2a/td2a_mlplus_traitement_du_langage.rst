
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Traitement du langage
+++++++++++++++++++++

Cette partie regroupe principalement des techniques
relevant du `word embedding <https://en.wikipedia.org/wiki/Word_embedding>`_ qui
consiste à convertir des données textuelles en données numériques directement
exploitable par les algorithmes d'apprentissage.

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_nlp

*Lectures - articles*

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

*Lectures - cours*

* `Deep Learning for Natural Language Processing <https://github.com/oxford-cs-deepnlp-2017/lectures>`_

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
