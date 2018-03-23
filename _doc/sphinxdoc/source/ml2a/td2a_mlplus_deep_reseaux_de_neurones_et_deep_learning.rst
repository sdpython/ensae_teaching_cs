
.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-deep-learning01:

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
* :ref:`Comparaison de librairies de deep learning <b-deep-learning-2018-cmp>`

*Descente de gradient*

* `Optimization Methods for Large-Scale Machine Learning <https://arxiv.org/abs/1606.04838>`_
* `Diagonal Rescaling For Neural Networks <https://arxiv.org/abs/1705.09319>`_

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

*Livres*

* `Deep Learning <http://www.deeplearningbook.org/>`_ de entre autres Yoshua Bengio

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
