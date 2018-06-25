
.. _l-td2a-mlplus:

=========================================
Galleries de problèmes résolus ou presque
=========================================

Cette rubrique étend la liste des références avec des articles
exposant des méthodes de machine learning appliquées à des problèmes
précis.

.. contents::
    :local:

3D
++

Pas d'articles précis, juste une liste de problèmes résolus.

* `3D-Machine-Learning <https://github.com/timzhang642/3D-Machine-Learning>`_

Apprentissage par renforcement
++++++++++++++++++++++++++++++

* `Towards Reinforcement Learning in the Real World <https://vimeo.com/238221551>`_

Awesome, Playground...
++++++++++++++++++++++

* `Awesome-Pytorch-list <https://github.com/bharathgs/Awesome-pytorch-list>`_
* `pytorch-playground <https://github.com/aaron-xichen/pytorch-playground>`_ :
  modèle préentraînés
* `pytorch-yolo2 <https://github.com/marvis/pytorch-yolo2>`_

Pretrained-models
+++++++++++++++++

* `pretrained-models.pytorch <https://github.com/Cadene/pretrained-models.pytorch>`_
* `PyTorch for Semantic Segmentation <https://github.com/ZijunDeng/pytorch-semantic-segmentation>`_
* `fcn - Fully Convolutional Networks <https://github.com/wkentaro/fcn>`_
* `pytorch-fcn/torchfcn/models <https://github.com/wkentaro/pytorch-fcn/tree/master/torchfcn/models>`_

Adversarial Examples
++++++++++++++++++++

* `The Limitations of Deep Learning in Adversarial Settings <https://arxiv.org/pdf/1511.07528v1.pdf>`_

.. _l-prob-solved-archi:

Architecture de Deep Learning
+++++++++++++++++++++++++++++

* `Neural Network Zooo Prequel: Cells and Layers <http://www.asimovinstitute.org/neural-network-zoo-prequel-cells-layers/>`_ :
  revue d'architectures de réseaux de neurones
* `Deformable Convolutional Networks <https://arxiv.org/abs/1703.06211>`_

Compétitions et datasets
++++++++++++++++++++++++

* `ImageNet <http://www.image-net.org/>`_
* `SQuAD The Stanford Question Answering Dataset <https://rajpurkar.github.io/SQuAD-explorer/>`_

Compter les objets dans une image
+++++++++++++++++++++++++++++++++

* `Fully Convolutional Crowd Counting On Highly Congested Scenes <https://arxiv.org/pdf/1612.00220.pdf>`_

.. _l-ml2a-resolu-detexpr:

Détection d'expressions
+++++++++++++++++++++++

* `Prediction and Localization of Student Engagement in the Wild <https://arxiv.org/abs/1804.00858>`_

.. _l-ml2a-resolu-detobj:

Détection d'objets
++++++++++++++++++

* `Pascal VOC Dataset <https://github.com/Microsoft/CNTK/tree/master/Examples/Image/DataSets/Pascal>`_
* `YOLO9000: Better, Faster, Stronger <https://arxiv.org/abs/1612.08242>`_ : détection en temps
  d'objets sur des images ou dans une vidéo, le code est sur github
  `darknet <https://github.com/pjreddie/darknet>`_, wrapper Python :
  `darknetpy <https://github.com/danielgatis/darknetpy>`_,
  `demo <https://pjreddie.com/darknet/yolo/>`_
* `Automatic Salient Object Detection for Panoramic Images Using Region Growing and Fixation Prediction Model <https://arxiv.org/abs/1710.04071>`_

.. _l-ml2a-resolu-detobj3d:

Détection d'objets en 3D
++++++++++++++++++++++++

* `PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space <https://arxiv.org/abs/1706.02413>`_,
  `Frustum PointNets for 3D Object Detection from RGB-D Data <https://arxiv.org/abs/1711.08488>`_,
  (`pointnet <https://github.com/charlesq34/pointnet>`_,
   `pointnet2 <https://github.com/charlesq34/pointnet2>`_)
* `3DContextNet: K-d Tree Guided Hierarchical Learning of Point Clouds Using Local and Global Contextual Cues <https://arxiv.org/abs/1711.11379>`_

.. _l-ml2a-resolu-detpartobj:

Détection de parties d'objets
+++++++++++++++++++++++++++++

* `Structured Set Matching Networks for One-Shot Part Labeling <https://arxiv.org/abs/1712.01867>`_

Fraudes
+++++++

*  `Detecting Fraudulent Personalities in Networks of Online Auctioneers <http://www.cs.cmu.edu/~dchau/papers/auction_fraud_pkdd06.pdf>`_

Deep Learning Artistique
++++++++++++++++++++++++

* `Pramit Choudhary - Learn to be a painter using Neural Style Painting <https://www.youtube.com/watch?v=WXDr5H1hVOU&list=PLGVZCDnMOq0rxoq9Nx0B4tqtr891vaCn7&index=60>`_ (vidéo)
* `Visual Attribute Transfer through Deep Image Analogy <https://arxiv.org/abs/1705.01088>`_
* `Coherent Online Video Style Transfer <https://arxiv.org/abs/1703.09211>`_
* `StyleBank: An Explicit Representation for Neural Image Style Transfer <https://arxiv.org/abs/1703.09210>`_
* `msracver/Deep-Image-Analogy <https://github.com/msracver/Deep-Image-Analogy>`_

Génération d'images à partir de texte
+++++++++++++++++++++++++++++++++++++

* `AttnGAN <https://github.com/taoxugit/AttnGAN>`_,
  `AttnGAN: Fine-Grained Text to Image Generation with Attentional Generative Adversarial Networks <https://arxiv.org/pdf/1711.10485.pdf>`_

Images en vrac
++++++++++++++

Les réseaux de neurones profonds fonctionnent très bien sur les images
car ce sont des entrées homogènes. Le traitement des images
cachent plusieurs types de problématiques :

* **classification** : reconnaître un object dans l'image sans savoir extactement où il est
* **segmentation** : reconnaître des objects dans une images, sous la forme de boîtes
  englobantes ou au pixel près
* **transformation** : déflouter, extraire le squelette, mettre en couleur,
  fusionner image et style

Ce ne sont pas les seules mais ces problématiques commencent à être
assez bien résolus. Il faut noter qu'on n'utilisent pas mêmes modèles
s'il s'agit d'images prises par un appareil photos ou d'images médicales.

* `Time-Contrastive Networks: Self-Supervised Learning from Multi-View Observation <https://arxiv.org/abs/1704.06888>`_ :
  un robot apprend à imiter les mouvements d'une personne
  (`vidéo <https://sermanet.github.io/tcn/>`_)
* `Device Placement Optimization with Reinforcement Learning <https://arxiv.org/pdf/1706.04972.pdf>`_
* `Automatic Colorization <http://tinyclouds.org/colorize/>`_
* `Image Completion <http://bamos.github.io/2016/08/09/deep-completion/>`_
* `Perceptual Losses for Real-Time Style Transfer and Super-Resolution <https://arxiv.org/pdf/1603.08155.pdf>`_,
  article : `neural-style <https://jayanthkoushik.github.io/neural_style.html>`_,
  code : `neural-style <https://github.com/jayanthkoushik/neural-style>`_.
* `Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network <https://arxiv.org/pdf/1609.04802.pdf>`_ :
  entraîner un réseau de neurones pour améliorer la netteté des images
* `YOLO9000: Better, Faster, Stronger <https://arxiv.org/abs/1612.08242>`_ : détection en temps
  d'objets sur des images ou dans une vidéo, le code est sur github
  `darknet <https://github.com/pjreddie/darknet>`_, wrapper Python :
  `darknetpy <https://github.com/danielgatis/darknetpy>`_,
  `demo <https://pjreddie.com/darknet/yolo/>`_
* `openalpr <https://github.com/openalpr/openalpr>`_ :
  reconnaissance de plaques d'immatriculation, pas vraiment du deep learning
* `Fully Convolutional Networks for Semantic Segmentation <https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf>`_
* `Deep Supervision with Shape Concepts for Occlusion-Aware 3D Object Parsing <https://arxiv.org/pdf/1612.02699.pdf>`_

Histoire
++++++++

* `Revisiting Unreasonable Effectiveness of Data in Deep Learning Era <https://arxiv.org/pdf/1707.02968.pdf>`_

Jeux
++++

* `Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm <https://arxiv.org/pdf/1712.01815.pdf>`_,
  voir quelques parties `The future is here - AlphaZero learns chess <https://en.chessbase.com/post/the-future-is-here-alphazero-learns-chess>`_.
  Avec ce type d'algorithme adapté à la finance, le trader humain a du soucis à se faire.

.. _l-prob-solved-speech:

Parole
++++++

* `Achieving Human Parity in Conversational Speech Recognition <https://arxiv.org/abs/1610.05256>`_ (2016)
* `Achieving Human Parity on Automatic Chinese to English News Translation <https://www.microsoft.com/en-us/research/publication/achieving-human-parity-on-automatic-chinese-to-english-news-translation/>`_ (2018)
* `Honk: CNNs for Keyword Spotting <https://github.com/castorini/honk>`_

Parole + Audio
++++++++++++++

* `Looking to Listen at the Cocktail Party: A Speaker-Independent Audio-Visual Model for Speech Separation <https://arxiv.org/pdf/1804.03619.pdf>`_

Portraits
+++++++++

* `Face Segmentation <https://github.com/YuvalNirkin/face_segmentation>`_ :
  il est plus facile de déterminer une boîte englobante autour d'un visage,
  le modèle référencé extrait un visage au pixel près,
  `Simple Classification Segmentation <https://github.com/arahusky/Tensorflow-Segmentation/blob/master/notebooks/simple_classification_segmentation.ipynb>`_,
  `Upsampling segmentation <https://github.com/arahusky/Tensorflow-Segmentation/blob/master/notebooks/upsampling_segmentation.ipynb>`_
* `FaderNetworks <https://github.com/facebookresearch/FaderNetworks>`_ :
  vieillir un visage, rajeunir, ajouter des lunettes, ce réseaux de neurones a été
  appris pour transformer un portrait
  (données : `Large-scale CelebFaces Attributes (CelebA) Dataset <http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html>`_)

.. _l-ml2a-reconstruction-image:

Reconstruction d'images
+++++++++++++++++++++++

* `Deep Image Prior <https://arxiv.org/pdf/1711.10925.pdf>`_

.. _l-ml2a-resolu-sketch:

Reconstruction de sketchs
+++++++++++++++++++++++++

.. index:: sketch

On entend par *sketch* des dessins filiformes représentant un objet,
une silhouette. Cela ressemble beaucoup aux dessins présents
sur les panneaux signalétiques dans la plupart des transports
en commun tout autour du monde.

* `SketchMate: Deep Hashing for Million-Scale Human Sketch Retrieval <https://arxiv.org/abs/1804.01401>`_

.. _l-ml2aresolu-socnet:

Réseaux Sociaux
+++++++++++++++

* `Social Clicks: What and Who Gets Read on Twitter? <https://hal.inria.fr/hal-01281190/document>`_
* `Real-time Detection of Content Polluters in Partially Observable Twitter Networks <https://arxiv.org/abs/1804.01235>`_

Retail
++++++

* `Data Mining Problems in Retail <https://highlyscalable.wordpress.com/2015/03/10/data-mining-problems-in-retail/>`_

.. _l-prob-solved-segmentation:

Segmentation d'images
+++++++++++++++++++++

* `Fully Convolutional Networks for Semantic Segmentation <https://arxiv.org/abs/1605.06211>`_
* `SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation <https://arxiv.org/abs/1511.00561>`_
* `Pyramid Scene Parsing Network <https://arxiv.org/abs/1612.01105>`_
* `U-Net: Convolutional Networks for Biomedical Image Segmentation <https://arxiv.org/abs/1505.04597>`_
* `RefineNet: Multi-Path Refinement Networks for High-Resolution Semantic Segmentation <https://arxiv.org/abs/1611.06612>`_
* `pytorch-semseg <https://github.com/meetshah1995/pytorch-semseg>`_
* `Pixel-wise segmentation on the VOC2012 dataset using pytorch <https://github.com/bodokaiser/piwise>`_
* `Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation <https://arxiv.org/pdf/1802.02611.pdf>`_
* `Xception: Deep Learning with Depthwise Separable Convolutions <https://arxiv.org/pdf/1610.02357.pdf>`_
* `DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs <https://arxiv.org/abs/1606.00915>`_
* `Rethinking Atrous Convolution for Semantic Image Segmentation <https://arxiv.org/pdf/1706.05587.pdf>`_

Texte / Traduction
++++++++++++++++++

* `Neural Machine Translation (seq2seq) Tutorial <https://github.com/tensorflow/nmt>`_
* `Representing Sentences as Low-Rank Subspaces <https://arxiv.org/abs/1704.05358v1>`_
* `SQuAD: 100,000+ Questions for Machine Comprehension of Text <https://arxiv.org/abs/1606.05250>`_,
  cette compétition fera sans doute émerger la nouvelle version des moteurs de recherche.
* `whatthelang <https://github.com/indix/whatthelang>`_ :
  module Python pour reconnaître la langue d'un texte,
  s'appuie sur :epkg:`FastText`

Voiture autonome
++++++++++++++++

* `Computer Vision for Autonomous Vehicles: Problems, Datasets and State-of-the-Art <https://arxiv.org/abs/1704.05519>`_

Notebooks
+++++++++

*CNTK*

* `Complex Neural Network Data Modelling with CNTK <http://dacrook.com/complex-neural-network-data-modelling-with-cntk/>`_

*Keras*

* `Using a pre-trained convnet <https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.3-using-a-pretrained-convnet.ipynb>`_
