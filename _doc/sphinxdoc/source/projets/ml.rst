
.. _l-ml:

Machine Learning
================

.. _l-ml-renf:

Apprentissage par renforcement
------------------------------


Un problème souvent évoqué lorsqu'on parle d'apprentissage par renforcement est celui du 
`bandit manchot <http://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)>`_ ou 
`multi-armed bandit <http://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)>`_ 
en anglais. L'objectif de ce projet est de résoudre 
ce problème en utilisant l'apprentissage par renforcement. Quelques liens :

* `Rémi Munos, part 1 <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part1.pdf>`_
* `Rémi Munos, part 2 <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part2.pdf>`_
* `Rémi Munos, part 3, parlant spécifiquement du bandit manchot <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part3.pdf>`_
* `Reinforcement Learning: An Introduction <http://webdocs.cs.ualberta.ca/~sutton/book/ebook/the-book.html>`_, Richard S. Sutton and Andrew G. Barto
* `Apprentissage par renforcement <http://www.grappa.univ-lille3.fr/~coulom/Renforcement/>`_
* `Agents adaptatifs Prise de décision séquentielle <http://www.grappa.univ-lille3.fr/~ppreux/mri/>`_

Le bandit manchot fait référence aux machines à sou dans les casinos. 
Tout l'enjeu de cette méthode consiste à maximiser ces gains en améliorant sa stratégie au fur et 
à mesure. Tout au long du jeu, il devient possible d'estimer la probabilité d'apparition 
des combinaisons gagnantes avec de plus en plus de précision. 
L'apprentissage par renforcement est une façon d'optimiser ses gains tout en apprenant cette distribution.


**Remarque :**

.. index:: morpion, tic-tac-toe

L'apprentissage par renforcement repose sur la connaissance de l'ensemble des 
états possibles du problèmes et ce nombre est souvent très grand. Trop grand.
Le jeu du morpion ou `tic-tac-toe <http://fr.wikipedia.org/wiki/Tic-tac-toe>`_
peut être résolu sans optimisation de l'algorithme initiale.
C'est le jeu utilisé par le surdoué dans 
`WarGame <http://fr.wikipedia.org/wiki/Wargames_%28film%29>`_ pour démontrer 
à une intelligence artificielle que, bien joués, 
certains finissent toujours par une partie nulle. Pour d'autres jeux, le plus simple
est souvent de chercher à réduire l'espace des états et des stratégies.
Quelques applications envisageables dans le cadre de ce projets :

* `tic-tac-toe <http://fr.wikipedia.org/wiki/Tic-tac-toe>`_
* `Tétris <https://interstices.info/jcms/c_32764/la-carotte-et-le-baton-et-tetris>`_ (voir aussi `Tetris, Colin Fahey <http://www.colinfahey.com/tetris/tetris.html>`_)
* `bandit manchot <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part3.pdf>`_
* `jeux de stratégie <http://www.bgu.ac.il/~shanigu/Publications/LearningInCiv.pdf>`_


.. _l-ml-chow:

Algorithme de Chow-Liu
----------------------

Cet algorithme `Chow Liu <http://en.wikipedia.org/wiki/Chow%E2%80%93Liu_tree>`_. 
Il sert à construire des relations entre des variables aléatoires. On pourra procéder en deux étapes :

* implémentation de l'algorithme et vérification sur un jeux de données synthétiques
* application sur un jeu de données plus conséquent


**Ressources**

* `MOOC: Learning Tree Structured Networks <https://class.coursera.org/pgm/lecture/97>`_,  Daphne Koller
  (pour aller plus loin `Probabilistic Graphical Models <https://class.coursera.org/pgm/lecture/preview>`_)
* `http://pgm.stanford.edu/ <Probabilistic Graphical Models>`_, Daphne Koller, Nir Friedman
* `Learning with Mixtures of Trees <http://www.jmlr.org/papers/volume1/meila00a/meila00a.pdf>`_, Marina Meila, Michael I. Jordan

.. _l-ml-visage:


Reconnaissance des visages de ses amis
--------------------------------------

.. index:: image processing

La librairie `OpenCV <http://opencv.org/>`_ 
permet d'effectuer des traitements d'images assez complexes comme localiser le
visage d'une personne prise en photo. L'image suivante
est extraite de `Face Detection in Static Images With Python <http://creatingwithcode.com/howto/face-detection-in-static-images-with-python/>`_.

.. image:: http://s3.amazonaws.com/static.creatingwithcode.com/wp-content/uploads/2009/02/output.jpg


La tâche qu'on veut pouvoir accomplir à l'aide d'un programme python est la suivante :

* On suppose qu'on dispose d'une vingtaine de photos de personnes, chacun distincte et
  identifiée. On suppose que les photos ont été prises avec le même appareil, un téléphone
  portable par exemple.
* On prend une nouvelle photo avec ce même appareil. On veut automatiquement ranger
  cette photo dans un répertoire associé à la personne reconnue.
  
On pourra lire les articles suivant :

* `Simple Face Detection using OpenCV <http://suksant.com/2013/04/03/simple-face-detection-using-opencv/>`_
* `Facial Detection with OpenCV and Python (1) <http://calebmadrigal.com/facial-detection-opencv-python/>`_
* `Facial Detection with openCV and Python (2) <http://fideloper.com/facial-detection>`_
* `Face Recognition with OpenCV <http://docs.opencv.org/trunk/modules/contrib/doc/facerec/facerec_tutorial.html>`_
* `Face Detection using Haar Cascades <http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html>`_

La version `OpenCV pour Python 3 <http://opencv.org/opencv-3-0-alpha.html>`_ est très récente
et la version finale devrait être prête pour fin 2014 / début 2015.

.. index:: deep learning, extreme machine learning

.. _l-ml-deepext:

Deep et Extreme Machine Learning
--------------------------------

C'est assez ambitieux comme premier projet. 
`MNIST <http://yann.lecun.com/exdb/mnist/>`_ est le premier problème mentionnant le
*Deep Learning*. Ce site recense les différentes performances obtenues jusqu'à présent sur ce modèle.

Sujet à préciser en fonction des attentes des élèves.

* `Visualizing MNIST: An Exploration of Dimensionality Reduction <http://colah.github.io/posts/2014-10-Visualizing-MNIST/>`_
* `Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis <http://www.math-info.univ-paris5.fr/~menasri/ENSAE/0176_689_patrice_p.pdf>`_, Patrice Y. Simard, Dave Steinkraus, John C. Platt
* `Extreme Learning Machines <http://www.ntu.edu.sg/home/egbhuang/pdf/IEEE-IS-ELM.pdf>`_, Erik Cambria, Guang-Bin Huang
* `Fast, simple and accurate handwritten digit classification using extreme learning machines with shaped input-weights <http://arxiv.org/abs/1412.8307>`_, Mark D. McDonnell, Migel D. Tissera, André van Schaik, Jonathan Tapson
* `Extreme Learning Machine: Theory and Applications <http://www.kovan.ceng.metu.edu.tr/~erol/Courses/CENG569/student-presentations/Yamac%20Kurtulus%20Ceng569%20Slide.pdf>`_, Guang-Bin Huang, Qin-Yu Zu, Chee-Kheong Siew
* `The Infinite MNIST <http://leon.bottou.org/projects/infimnist>`_
* `VowPal Wabbit and MNIST <https://github.com/JohnLangford/vowpal_wabbit/tree/master/demo/mnist>`_
* `Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ (Chapitre 1 `Using neural nets to recognize handwritten digits <http://neuralnetworksanddeeplearning.com/chap1.html>`_)
* `theano <http://deeplearning.net/software/theano/>`_, module Python spécialisé dans le deep learning, `caffe <http://caffe.berkeleyvision.org/>`_


