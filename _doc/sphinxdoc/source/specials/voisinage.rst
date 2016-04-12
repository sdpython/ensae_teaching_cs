



.. _l-simulation_voisinage:


Evolution d'un voisinage, d'une population
==========================================

Voisinage, ségrégation
++++++++++++++++++++++

La mixité au sein d'une ville n'est pas une chose facile à
obtenir. Les habitants ont plutôt tendance à se regrouper
selon un sentiment d'appartenance à un groupe ou une classe.
Il en résulte une forme de ségrégation que l'économiste
`Thomas Schelling <https://en.wikipedia.org/wiki/Thomas_Schelling>`_ a 
tenté de modéliser. Le module 
:mod:`voisinage_evolution <ensae_teaching_cs.special.voisinage_evolution>`
s'inspire de `Schelling's Model of Segregation <http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/>`_
pour simuler l'évolution de la ville de Paris
en fonction de ce que le prix du mètre carré révèle en terme d'appartenance de classe.

La simulation en vidéo :

.. raw:: html

    <video autoplay="" controls="" loop="" height="500">
    <source src="http://www.xavierdupre.fr/enseignement/complements/voisinage.mp4" type="video/mp4" />
    </video>


Epidémie
++++++++

Au moment de la grippe aviaire, le gouvernemetn français a dû prendre
la décision d'acheter des vaccins pour protéger la population.
Combien en acheter pour éviter une épidémie ? Quel taux de vaccination
est nécessaire pour stopper sa progression ?
Une réponse consiste à simuler cette progression à partir d'un modèle
micro-économique. La vidéo qui suit est une illustration grossière
de ce que pourrait être une simulation de ce type.

.. raw:: html

    <video autoplay=" controls="" loop="" height="400">
    <source src="http://www.xavierdupre.fr/enseignement/complements/epidemic.mp4" type="video/mp4" />
    </video>
    
Voir module :mod:`propagation_epidemic <ensae_teaching_cs.special.propagation_epidemic>`.
