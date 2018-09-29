
.. _l-ml:

Machine Learning
================

.. contents::
    :local:

Le site `CS 188: Artificial Intelligence (Berkeley) <http://inst.eecs.berkeley.edu/~cs188/fa10/lectures.html>`_
propose des projets informatiques qui ont la particularité de partir d'un squelette existant.
Ce sont des problèmes de machines learning très guidés où l'essentiel de l'effort
est tourné vers les algorithmes.

.. _l-ml-renf:

Apprentissage par renforcement
------------------------------

Un problème souvent évoqué lorsqu'on parle d'apprentissage par renforcement est celui du
`tic tac toe <https://en.wikipedia.org/wiki/Tic-tac-toe>`_.
L'objectif de ce projet est de résoudre
ce problème en utilisant l'apprentissage par renforcement. Quelques liens :

* `Rémi Munos, part 1 <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part1.pdf>`_
* `Rémi Munos, part 2 <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part2.pdf>`_
* `Rémi Munos, part 3, parlant spécifiquement du bandit manchot <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part3.pdf>`_
* `Reinforcement Learning: An Introduction <http://webdocs.cs.ualberta.ca/~sutton/book/ebook/the-book.html>`_, Richard S. Sutton and Andrew G. Barto
* `Apprentissage par renforcement <http://www.grappa.univ-lille3.fr/~coulom/Renforcement/>`_
* `Agents adaptatifs Prise de décision séquentielle <http://www.grappa.univ-lille3.fr/~ppreux/mri/>`_
* `UCL Course on RL <http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html>`_
* `Machine Learning for Humans, Part 5: Reinforcement Learning <https://medium.com/machine-learning-for-humans/reinforcement-learning-6eacf258b265>`_

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
* `Reinforcement Learning Assignment: Easy21 <http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/Easy21-Johannes.pdf>`_
* `Un chariot qui maintient un poteau en équilibre <https://medium.com/@tuzzer/cart-pole-balancing-with-q-learning-b54c6068d947>`_,
  avec `tensorflow <http://kvfrans.com/simple-algoritms-for-solving-cartpole/>`_

On peut envisager des contextes différents tels que le jeu de Pacman ou de Pong :

* `Reinforcement Learning (Berkeley) <http://inst.eecs.berkeley.edu/~cs188/fa10/projects/reinforcement/reinforcement.html>`_
* `pg-pong.py <https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5>`_

Autres pistes :ref:`l-td2a-reinforcement-learning`,
:ref:`l-td2a-reinforcement-learning-marl`.

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

Deux outils pour annoter des images si vous n'en avez pas :

* `sloth <https://github.com/cvhciKIT/sloth>`_
* `labelImg <https://github.com/tzutalin/labelImg>`_

.. _l-ml-deepext:

Deep et Extreme Machine Learning
--------------------------------

.. index:: deep learning, extreme machine learning

C'est assez ambitieux comme premier projet.
`MNIST <http://yann.lecun.com/exdb/mnist/>`_ est le premier problème mentionnant le
*Deep Learning*. Ce site recense les différentes performances obtenues jusqu'à présent sur ce modèle.

Sujet à préciser en fonction des attentes des élèves.

* `Visualizing MNIST: An Exploration of Dimensionality Reduction <http://colah.github.io/posts/2014-10-Visualizing-MNIST/>`_
* `Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis <http://www.math-info.univ-paris5.fr/~menasri/ENSAE/0176_689_patrice_p.pdf>`_, Patrice Y. Simard, Dave Steinkraus, John C. Platt
* `Extreme Learning Machines <http://www.ntu.edu.sg/home/egbhuang/pdf/IEEE-IS-ELM.pdf>`_, Erik Cambria, Guang-Bin Huang
* `Fast, simple and accurate handwritten digit classification using extreme learning machines with shaped input-weights <http://arxiv.org/abs/1412.8307>`_, Mark D. McDonnell, Migel D. Tissera, André van Schaik, Jonathan Tapson
* `Extreme Learning Machine: Theory and Applications <http://www.kovan.ceng.metu.edu.tr/~erol/Courses/CENG569/student-presentations/Yamac%20Kurtulus%20Ceng569%20Slide.pdf>`_, Guang-Bin Huang, Qin-Yu Zu, Chee-Kheong Siew
* `Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ (Chapitre 1 `Using neural nets to recognize handwritten digits <http://neuralnetworksanddeeplearning.com/chap1.html>`_)
* `Why does Deep Learning work? - A perspective from Group Theory <http://arxiv.org/abs/1412.6621>`_, Arnab Paul, Suresh Venkatasubramanian

Librairies, modules :

* `The Infinite MNIST <http://leon.bottou.org/projects/infimnist>`_
* `VowPal Wabbit and MNIST <https://github.com/JohnLangford/vowpal_wabbit/tree/master/demo/mnist>`_
* `pytorch <https://pytorch.org/>`_

.. _l-ml-align:

Alignement de mots dans l'optique de constuire un traducteur automatique
------------------------------------------------------------------------

L'algorithme est présentée dans l'article :
`Word Alignment via Quadratic Assignment <http://homes.cs.washington.edu/~taskar/pubs/naacl06_qap.pdf>`_
de Simon Lacoste-Julien, Ben Taskar, Dan Klein, Michael I. Jordan.
On pourra commencer sur un jeu de données petit et fabriqué manuellement. On pourra ensuite s'attaquer à
des sites web qui proposent des traductions anglais/français de leur contenu.
Autres liens intéressants proposés par les élèves qui ont travaillé sur ce sujet :

* `Traduction automatique statistique et adaptation à un domaine sp ecialis e <https://tel.archives-ouvertes.fr/tel-00879945/document>`_
* `Identification des cognats et alignement bi-textuel : une étude empirique <http://www.atala.org/taln_archives/TALN/TALN-1999/taln-1999-long-019.pdf>`_
* `Improved Word Alignments for Statistical Machine Translation <http://www.cis.uni-muenchen.de/~fraser/pubs/fraser_diss.pdf>`_

.. _l-fast-k-NN:

Fast k-NN (2016)
----------------

L'algorithme des `k plus proches voisins <https://fr.wikipedia.org/wiki/M%C3%A9thode_des_k_plus_proches_voisins>`_
est un des plus simples algorithmes d'apprentissage mais très coûteux. L'article suivent propose une façon
d'optimiser le calcul dans des espaces de grande dimension.

`Fast k-NN search <http://arxiv.org/abs/1509.06957>`_

.. _l-ml-gradient-geom:

Accélération de la descente de gradient dans le cadre d'une optimisation convexe (2016)
---------------------------------------------------------------------------------------

.. index:: gradient descente, descente de gradient, convexe

La `descente de gradient <https://en.wikipedia.org/wiki/Gradient_descent>`_ est une technique
d'optimisation très connue utilisée lorsqu'on ne sait pas exprimer de façon explicite
la solution d'un problème d'optimisation : on cherche le minimum ou le maximum de la fonction.

Si l'algorithme converge lorsque la fonction à optimiser est convexe,
il existe des cas particuliers où on peut accélérer la convergence
comme dans le cas de cet article qui propose une façon intuitive de le faire :
`A geometric alternative to Nesterov's accelerated gradient descent <http://arxiv.org/abs/1506.08187>`_.

L'objectif est d'implémenter cet algorithme puis de le comparer avec
d'autres méthodes.

On pourra également regarder :
`Linear Coupling: An Ultimate Unification of Gradient and Mirror Descent <http://arxiv.org/abs/1407.1537>`_
et `Revisiting Nesterov’s Acceleration <https://blogs.princeton.edu/imabandit/2015/06/30/revisiting-nesterovs-acceleration/>`_.

.. _l-ml-reg-geod:

Régression à base de plus proches voisins (2017)
------------------------------------------------

.. index:: régression, plus proche voisins

Il faut implémenter la méthode de l'article qui suit :

* `Minimax-optimal semi-supervised regression on unknown manifolds <https://arxiv.org/abs/1611.02221>`_

.. _l-ml-ethique:

Construction d'un estimateur du caractère éthique d'un moteur de recherche (2017)
---------------------------------------------------------------------------------

On se pose de plus en plus la question du caractère éthique des algorithmes :
`Tous algorithmés, tous concernés <http://www.modernisation.gouv.fr/la-semaine-de-linnovation-publique/revivez-la-semaine-de-linnovation-publique-2016/tous-algorithmes-tous-concernes>`_,
`Google, democracy and the truth about internet search <https://www.theguardian.com/technology/2016/dec/04/google-democracy-truth-internet-search-facebook>`_.
On se place dans le cas ici d'un site qui proposent des contenus à partir d'une requête
(moteur de recherche, vente en ligne, publicité). Comment exprimer le fait
que les résultats produits par le site ne sont pas biaisés éthiquement,
comment mesurer le caractère éthique des résultats ?
Le sujet est assez libre mais implique certainement la manipulation de texte.
Côté scientidique, on pourra s'inspirer de l'article
`FairTest: Discovering Unwarranted Associations in Data-Driven Applications <https://arxiv.org/pdf/1510.02377.pdf>`_.

.. _l-ml-fire-detection:

Détection de fumée dans les images (2017)
-----------------------------------------

C'est une idée extraite de l'article :
`Early Fire Detection Using HEP and Space-time Analysis <https://arxiv.org/pdf/1310.1855v1.pdf>`_.
Elle ne requiert pas nécessaire de machine learning mais s'appuie plus simplement
sur des indicateurs construits à partir des images. Le projet devra commencer par récupérer
des images sur Internet (via un moteur de recherche par exemple).

.. _l-ml-snn:

Implémenter un SNN : Spiking Neural Network (2018)
--------------------------------------------------

* `Python Tutorial: How to Write a Spiking Neural Network Simulation From Scratch <http://www.mjrlab.org/2014/05/08/tutorial-how-to-write-a-spiking-neural-network-simulation-from-scratch-in-python/>`_

Voir aussi :ref:`l-ml2a-snn`.

.. _l-ml-tree-graph:

Ecrire une librairie pour représenter des modèles de machine learning (2018)
----------------------------------------------------------------------------

Supposons qu'une forêt aléatoire a été appris pour classifier un jeu de
données, est-il possible de la représenter de façon à faciliter 
son interprétation. On pourra s'inspirer du module 
`animl <https://github.com/parrt/animl>`_.
On choisira de limiter le nombre de dépendance au minimum.


