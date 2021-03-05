
.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Prédire en environnement contraint
++++++++++++++++++++++++++++++++++

C'est l'option la plus facile. Elle consiste à apprendre
sur un ordinateur classique puis à exporter le modèle dans un environnement
différent où seule la prédiction est disponible. On l'appelle parfois
le *runtime*. Il existe encore peu d'outils communs même s'il est fortement
probable que chacun ait développé des outils en interne adaptés à son architecture.
Il est très facile d'apprendre une régression logistique puis de réimplémenter
la fonction de prédiction partout où on en a besoin avec les coefficients
du modèle plutôt que de chercher à installer :epkg:`Python`.

*Modules*

* `Embedded Learning Library (ELL) <https://github.com/Microsoft/ELL>`_ :
  deep learning sur :epkg:`RaspberryPI`, :epkg:`Arduino`
* `onnx <https://github.com/onnx/onnx>`_
* `coremltools <https://pypi.python.org/pypi/coremltools>`_
