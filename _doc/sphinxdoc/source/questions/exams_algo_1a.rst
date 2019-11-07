
.. index:: examens, algorithme, 1A

.. _l-examens-1A-algo:

.. _l-examens-1A-algo-2048:

Réalisation d'un module python par groupe de 3 à 5
==================================================

Un embryon de jeu :epkg:`2048` est implémenté dans l'exemple
suivant `cp2048.py
<https://github.com/sdpython/ensae_teaching_cs/blob/master/src/ensae_teaching_cs/td_1a/cp2048.py>`_,
un exemple complet de projet est illustré par le module
`pystrat2048 <https://github.com/sdpython/pystrat2048>`_
(`documentation <http://www.xavierdupre.fr/app/pystrat2048/helpsphinx/index.html>`_).
Un exemple d'utilisation est présent dans un second fichier
`test_cp2048.py <https://github.com/sdpython/ensae_teaching_cs/blob/master/_unittests/ut_td_1a/test_cp2048.py>`_.
La strétagie à implémenter doit pouvoir être
évaluée avec la fonction: :func:`evaluate_strategy
<ensae_teaching_cs.td_1a.cp2048.evaluate_strategy>`.
Voici un exemple :

.. runpython::
    :showcode:

    import random
    from ensae_teaching_cs.td_1a.cp2048 import evaluate_strategy

    def random_strategy(game, moves):
        return random.randint(0, 3)

    scores = list(evaluate_strategy(random_strategy))
    print(scores)

La stratégie devra venir du module que vous devrez implémenter
de la façon suivant :

::

    import random
    from ensae_teaching_cs.td_1a.cp2048 import evaluate_strategy
    from un_module import strategy_2048

    scores = list(evaluate_strategy(strategy_2048))
    print(scores)

La meilleure stratégie sera évaluée sur 1000 parties.
Pour finir, les deux notebooks suivants vous seront utiles :
:ref:`l-ci-1a-notebooks`.

**Rendu**

Le projet doit être rendu sous la forme d'un fichier zip
avec les sources accompagnées d'un exemple sous la forme
d'un fichier python ou notebook. La documentation
n'est pas indispensable. Le projet minimal doit ressembler
à ce qui suit :

::

    zip
     +-- votre_module
     |      +-- __init__.py
     |      +-- fichier.py
     +-- tests
     |      +-- test_strategy.py
     +-- setup.py
     |
     +-- example.py ou example.ipynb
