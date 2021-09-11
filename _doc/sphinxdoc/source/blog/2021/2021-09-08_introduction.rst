
.. blogpost::
    :title: Introduction à la programmation (sketch)
    :keywords: teachings
    :date: 2021-09-08
    :categories: article
    :lid: blog-intro-2021-ensae

    **Présentation**

    * Programmation en classes préparatoires,
      `Informatique en CPGE <https://info-llg.fr/>`_
        * architecture d'un ordinateur
        * base du langage python
        * arbre binaire, graphes
        * algorithme, parcours de graphe, distance d'édition,
          diviser pour régner, programmation dynamique
    * Langages haut niveau, bas niveau
        * C/C++
        * Rust
        * Javascript, Python, matlab...
    * Python : machine learning
        * datascience, deep learning = python
        * automatisation, site web
        * Python populaire (travails, universités)
        * interfaçage avec C++
    * Pratique
        * Trouver le plus court chemin d'une station de métro à une autre ? -->
          plus court chemin dans un graphe
        * Même question en tenant compte des temps de changement de ligne ?

    **Machine learning aujourd'hui**

    * Apprentissage fait avec python
        * :epkg:`scikit-learn`
        * deep learning : :epkg:`pytorch`
    * Code faisant les calculs écrit en C/C++/asm
        * :epkg:`numpy`, :epkg:`scipy`
        * :epkg:`scikit-learn`, `_tree.pyx
          <https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/tree/_tree.pyx>`_
    * Déploiement (utilisation des modèles) sur
      d'autres langages encore (javascript, C#, go, ...)
        * Python très lent malgré et difficile à maintenir
          d'une version de python à une autre
        * Le Cloud `AWS <https://aws.amazon.com/fr/>`_,
          `Azure <https://azure.microsoft.com/>`_ ...
    * Démocratisation dans de nombreux pays
        * `Health Data Hub <https://www.health-data-hub.fr/>`_
        * `data.gouv.fr <https://www.data.gouv.fr/fr/>`_

    **Deep Learning**

    * Le deep learning envahit la vie quotidienne
        * santé (aide au diagnotisque)
        * sécurité (vidéo surveillance),
        * automatisation (voiture)
        * publicité, objets connectées
        * ...
    * Besoin de calculs, besoin de codes rapides
        * CPU, GPU, TPU
        * `NVIDIA A100 <https://www.nvidia.com/en-us/data-center/a100/>`_,
          innovation matérielle et logicielle
        * recherche très active dans ce domaine
    * Modèles de plus en plus gros
    * Il ne suffit plus d'être bon en maths, ou bon en informatique,
      il faut être les deux

    **Ingéniérie logicielle**

    * Le point faible des ingénieurs français
        * On commence l'informatique avant la prépa dans d'autres pays
        * Pas assez de pratique, un bon codeur a beaucoup codé.
    * tests unitaires : à connaître avant d'aller passer un entretien d'embauche
    * intégration continue
        * A chaque modification, on vérifie que les tests unitaires passent.
    * documentation
        * C'est fastidieux mais indispensable dans un monde open source.
        * Les projets qui ont réussi ont toujours une bonne documentation.
    * culture algorithmique
        * un produit matriciel n'est pas aussi simple qu'on le dit quand on veut qu'il
          soit rapide
        * :ref:`l-algoculture`
    * git
        * Un outil injustement méconnu des juristes.

    **Thèse...**

    * C/C++ : même si vous n'en avez pas besoin tous les jours,
      on code mieux en python quand on connaît un langage bas niveau
      car on comprend mieux tout ce que le langage nous cache
    * linux

    Cours, premiere semestre

    * TD : :ref:`l-td1a`
    * Evaluation, anciens examens :ref:`l-seances-notees-1A`

    **Cours, second semestre**

    * Projet : :ref:`l-projinfo1a`

    **Ressource, supports pour ce cours**

    * TD : `Python dans tous ses états <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_
    * Rappels : `Petit voyage au pays du machine learning <http://www.xavierdupre.fr/app/papierstat/helpsphinx/index.html>`_
    * Programmation : `Apprendre la programmation avec Python <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/index.html>`_
    * Un peu plus mathématique : `Les maths d’abord, la programmation ensuite <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/index.html#mlstatpy>`_

    Et puis...

    * Les moteurs de recherche : `python + message d'erreur`, `cheatsheet`
    * `Questions tagged [python] <https://stackoverflow.com/questions/tagged/python>`_
    * `Compétition de code par Google <https://codingcompetitions.withgoogle.com/codejam>`_
    * `Compétition de code en français ou presque <https://tryalgo.org/contests/>`_
    * `Projet Euler <https://projecteuler.net/>`_

    **A la fin de l'année, vous devriez pouvoir...**

    * Imaginer une stratégie automatique au 2048.
    * Simuler une épidémie, des régimes de retraites
    * Supprimer les pesticides en programmant des drones pour couper
      les mauvaises herbes ou couper les feuilles infectées par le mildiou
    * Lutter contre les îlots de chaleur dans les villes en verdissant les toits
      avec un mélange de plantes en fonction de la disposition du toit
      (`Singapour : des gratte-ciels anti-pollution
      <https://www.francetvinfo.fr/monde/environnement/singapour-des-gratte-ciels-anti-pollution_2868081.html>`_)
    * Devenir le prochain `covidtracker <https://covidtracker.fr/>`_
    * Calculer l'exposition d'une économie à un certain type de produit...
      `PSA : l’usine de Rennes à l’arrêt par manque de semi-conducteurs
      <https://www.leparisien.fr/economie/psa-lusine-de-rennes-a-larret-par-manque-de-semi-conducteurs-19-08-2021-MADPPG5OMJA2LH5DYFHWB6CBTU.php>`_
      `Panne Orange : quelles conséquences ?
      <https://www.franceinter.fr/emissions/le-13-14/le-13-14-03-juin-2021>`_,
      `Xavier Jaravel, meilleur jeune économiste 2021 pour ses travaux sur l'innovation et les inégalités
      <https://start.lesechos.fr/societe/economie/xavier-jaravel-meilleur-jeune-economiste-2021-pour-ses-travaux-sur-linnovation-et-les-inegalites-1319721>`_,

    Tout est sur `GitHub <https://github.com/sdpython>`_.
