
.. _l-projinfo2a:

2A - Projets informatiques - Data Scientist - Economiste
========================================================

.. contents::
    :local:

**Dates de rendu**

* dernier jour avant les vacances de Noël pour le rapport / notebook / programme
* première semaine de janvier pour la vidéo

Data Scientist
++++++++++++++

Le projet informatique sera centré sur la résolution d'un problème de
machine learning à partir d'un jeu de données préparé à cet effet.
Le choix du sujet est libre et vous trouverez une liste de suggestions à
:ref:`l-datasources`.

Le site
`Kaggle <https://www.kaggle.com/competitions/search?SearchVisibility=AllCompetitions&ShowActive=true&ShowCompleted=true&ShowProspect=true&ShowOpenToAll=true&ShowPrivate=true&ShowLimited=true&DeadlineColumnSort=Descending>`_ `(2) <http://inclass.kaggle.com/>`_
référence de nombreuses compétitions intéressantes.
Toutefois, avant d'utiliser les données Kaggle, je vous encourage à lire les articles
`Date use for teaching after competition concludes <http://www.kaggle.com/c/decoding-the-human-brain/forums/t/8331/date-use-for-teaching-after-competition-concludes>`_
et `Using a Kaggle contest as a term project <http://www.kaggle.com/forums/t/2745/using-a-kaggle-contest-as-a-term-project>`_.
Les règles peuvent varier d'un projet à l'autre, prenez soin de les lire avant de choisir un projet
car on ne peut pas tout faire avec les données disponibles sur ce site.

Les publications scientifiques mettent parfois leurs données à dispositions :

* `Patient Risk Stratiﬁcation with Time-Varying Parameters: A Multitask Learning Approach <http://www.jmlr.org/papers/volume17/15-177/15-177.pdf>`_
* `Trend Filtering on Graphs <http://www.jmlr.org/papers/volume17/15-147/15-147.pdf>`_

Travail attendu
+++++++++++++++

On vous demande de vous poser une problématique et d'y répondre en utilisant des données.
Le projet est orienté plus machine learning pour les data scientist,
plus qualitatif et collecte de données pour les économistes.

* Rapport + code (PDF, Notebook, HTML)
  il peut être converti au format PDF ou HTML avec `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_ et Latex).
  Si le rapport n'est pas un notebook, il faudra indiquer la fonction à l'origine de chaque table ou graphique.
* Une introduction : quel est le problème à résoudre, les questions auxquelles on cherche à répondre, un aperçu des données.
* Une attention particulière sur la rigueur de la démarche (base d'apprentissage / test,
  overfitting, validation croisée, vérification sur quelques exemples,
  type de variable - continues, discrètes, catégorielles).
* On pourra également souligner le raisonnement ou l'intuition qui vous amène
  à essayer tel modèle, tel feature, telle méthode.
* La présence d'au moins un graphique.
* Une conclusion : le modèle, les résultats sont-ils exploitables ?
* Une vidéo, pas plus de 5 minutes pour présenter votre projet.

**data scientist**

* La comparaison de deux modèles sur le même jeu de données (soit deux modèles différents,
  soit le même modèle avec des paramètres différents), on s'intéressera aux observations
  pour lesquelles les modèles sont en désaccords. On pourra également comparer
  les vitesse d'apprentissages et les performances.
* L'ajout d'une variable/feature non présente dans le jeu de données initial
  (cela peut être une combinaison des précédentes).
* Prolongements / perspectives : le problème à résoudre est souvent extrait de son contexte,
  il s'agit de le replacer dans un environnement industriel. Cela peut passer par
  une réflexion autour des questions suivantes (qui ne s'appliquent pas forcément à tous les jeux de données).

Les questions à se poser :

* Le modèle est-il exploitable avec ses performances ?
* Est-il exploitable seul ou associé à autre chose (est-il une feature d'un autre modèle) ?
* Quel est sa durée de vie ? Ses performances vont-elle se dégrader dans le temps ? Peut-on le détecter ?
* Le modèle peut-il passer à l'échelle et être entraîné sur des jeux 10, 100, 1000 fois plus grand ?
* Certaines variables/information sont coûteuses à obtenir,
  est-il envisageable de faire moins coûteux sans trop de perte de performances ?
* Doit-il être maintenu, rafraîchi, à quel coût ?
* Si le modèle doit être rafraîchi régulèrement, le modèle peut-il être utilisé
  voire réappris sans intervention humaine ?
* Si le modèle est rafraîchi régulièrement et automatique,
  serai-il facile de détecter qu'une mise à jour a échoué ?
* Lorsque l'apprentissage est long et coûteux, l'estimation d'un nouveau
  modèle pourrait-elle être faite à partir de la précédente ou non ?
  (nouvel apprentissage ou simple mise à jour)
* Si vous deviez vendre ce modèle de machine learning, quel modèle économique choisiez-vous ?
  (une application, une extension Excel, un service distant payé à chaque prédiction,
  une application smartphone, le modèle seulement...)
* Lorsque le modèle se trompe, se trompe-t-il de beaucoup ? Quel serait le coût de l'erreur ?
  Peut-on le réduire ?

**economiste**

Trois dimensions doivent être présentes dans le projet.
Pour chacune de ces parties, il est possible d'aller plus ou moins loin.
Il est recommandé d'aller loin sur au moins une des dimensions.

#. **La récupération de données :**
   Ces données peuvent être directement disponibles sous la forme de fichiers txt, csv ...
   ou provenir de sites internet (scrapping, API).  Plus le travail
   sur la récupération de données est important (par exemple scrapping sur plusieurs
   sites), plus la partie obtiendra de points. En partant des données de
   `IMBD sur les films <http://www.imdb.com/interfaces>`_.
   Vous pouvez récupérer des informations sur les films ressemblants grâce à
   l'API de `Tasktekid <https://www.tastekid.com/>`_ et répondre à la question de
   qu'est ce qui rend des films similaires (le casting, le thème, le réalisateur ...)
#. **Le traitement et l'analyse :**
   La présence de statistiques descriptives est indispensable dans le projet.
   De la description de la base aux premières grandes tendances des données,
   cette partie permet d'avoir une vision globale des données : le lien avec
   la problématique, comment elle permet d'y répondre, quels sont les premiers éléments de réponse...
   Chaque résultat doit être interprété : pas la peine de faire un describe et de ne pas le commenter.
   Vient ensuite la phase de modélisation : un modèle peut être le bienvenu quand des
   statistiques descriptives ne suffisent pas à apporter une solution complète à
   votre problématique. Le modèle importe peu (régression linéaire, random forest ou autre) :
   il doit être approprié et justifié.
#. **La représentation / application :** Là encore, plusieurs niveaux sont envisageables.
   Vous pouvez simplement représenter vos données en utilisant matplotlib, aller plus loin
   avec `seaborn <http://seaborn.pydata.org/>`_
   (voire `D3.js <https://en.wikipedia.org/wiki/D3.js>`_ pour les plus motivés)
   ou encore réaliser une application en `Flask <http://flask.pocoo.org/>`_.
   La base d'une bonne visualisation est de trouver le type de graphique adéquat
   pour ce que vous voulez montrer (faut-il un scatter ou un line pour
   représenter une évolution ?) et de le rendre visible : une légende
   qui a du sens, des axes avec des noms etc.

Barème
++++++

* rapport : 5 points
* graphiques : 5 points
* prolongements : 3 points
* démarche scientifique : 5 points
* vidéo : 2 points

Le projet doit être réalisé seul ou par groupe de deux, voire trois.
Le jeu de données doit être conséquent (plus de 5000 observations).
Un des modèles utilisés n'est pas linéaire et n'est pas un arbre de décision.
Chaque membre d'un groupe doit mentionner une contribution personnelle au projet.

Vidéo
+++++

* `The best stats you've ever seen <http://www.ted.com/talks/hans_rosling_shows_the_best_stats_you_ve_ever_seen>`_, Hans Rosling
* `Let my dataset change your mindset <http://www.ted.com/talks/hans_rosling_at_state?language=en>`_, Hans Rosling
* `Hans Rosling's 200 Countries, 200 Years, 4 Minutes - The Joy of Stats - BBC Four <https://www.youtube.com/watch?v=jbkSRLYSojo>`_, Hans Rosling (4 minutes)
* `Convertir votre présentation en vidéo <http://office.microsoft.com/fr-fr/powerpoint-help/convertir-votre-presentation-en-video-HA010336763.aspx>`_
* `Ma thèse en 180 secondes <http://mt180.fr/>`_
* `Quelques outils pour faire des captures vidéo d'écrans <http://www.xavierdupre.fr/blog/2014-10-24_nojs.html>`_

Un exemple réalisé avec `iMovie <https://www.apple.com/fr/mac/imovie/>`_ :
`Le traitement des données <http://www.xavierdupre.fr/blog/2014-10-27_nojs.html>`_.
On peut aussi réaliser des vidéos à partir de séquences d'images
(voir la fonction :func:`make_video <ensae_teaching_cs.helpers.video_helper.make_video>`).

.. raw:: html

    <video autoplay=" controls="" loop="" height="400">
    <source src="http://www.xavierdupre.fr/enseignement/complements/epidemic.mp4" type="video/mp4" />
    </video>

Liens
+++++

- :ref:`Bien démarrer un projet de machine learning <l-debutermlprojet>`
- `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
- `Using Python to Dive into Signalling Data with CellNOpt and BioServices <http://arxiv.org/abs/1412.6386>`_
- `SPySort: Neuronal Spike Sorting with Python <http://arxiv.org/abs/1412.6383>`_
- `Machine learning isn't Kaggle competitions <http://jvns.ca/blog/2014/06/19/machine-learning-isnt-kaggle-competitions/>`_.
- :ref:`gitnotebookrst`

.. _l-question-projet-2A-ml:

Questions
+++++++++

* :ref:`question_2014_projet_1_2A`
* :ref:`question_2014_projet_2_2A`
* :ref:`question_2014_projet_3_2A`
* :ref:`question_2014_projet_4_2A`
* :ref:`question_2014_projet_5_2A`
* :ref:`question_2014_projet_6_2A`
* :ref:`question_2015_projet_2_2A`
* :ref:`question_projet_2016`
