
.. index:: examens, algorithme, 1A

.. _l-examens-1A-algo:

.. _l-examens-1A-algo-2048:

Réalisation d'un module python par groupe de 3 à 5
==================================================

.. contents::
    :local:

Objectif
++++++++

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

Rendu
+++++

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

Quelques retours
++++++++++++++++

Ci-dessous les résultats produits par les stratégies
que j'ai réussies à faire tourner. Dix parties ont été
jouées et le score pour chacune d'entre elle a été
enregistrée. Certaines stratégies produisent un score de 4
ce qui est probablement dû à un bug ou une maladresse de ma part.
Une stratégie sort clairement gagnante et quatre d'entre elles
atteignent le score de 2048. Cette stratégie étudie le gain
après deux coups. Elle fait attention à ce que la ligne
du bas ne change pas trop, que les nombres sur cette ligne
forme une séquence décroissante, et s'intéresse aux séquences
de deux nombres identiques placés côte à côte.

- 1.722 secondes - moyenne : 294.400 [128, 512] - scores: [512, 256, 256, 512, 256, 256, 128, 256, 256, 256]
- 12.430 secondes - moyenne : 3.800 [2, 4] - scores: [4, 4, 4, 4, 4, 4, 4, 2, 4, 4]
- 0.550 secondes - moyenne : 153.600 [64, 256] - scores: [128, 128, 64, 256, 64, 128, 256, 256, 128, 128]
- 965.660 secondes - moyenne : 275.200 [64, 512] - scores: [256, 64, 128, 256, 256, 256, 256, 512, 512, 256]
- 27.808 secondes - moyenne : 1126.400 [512, 2048] - scores: [512, 1024, 1024, 2048, 1024, 1024, 1024, 1024, 2048, 512]
- 34.587 secondes - moyenne : 44.800 [16, 64] - scores: [32, 64, 32, 16, 64, 32, 64, 64, 16, 64]
- 114.892 secondes - moyenne : 896.000 [256, 2048] - scores: [2048, 512, 256, 1024, 2048, 256, 256, 1024, 512, 1024]
- 0.836 secondes - moyenne : 4.000 [4, 4] - scores: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
- 1.519 secondes - moyenne : 345.600 [128, 512] - scores: [512, 128, 512, 256, 512, 128, 256, 512, 128, 512]
- 10.363 secondes - moyenne : 2048.000 [1024, 4096] - scores: [4096, 2048, 2048, 2048, 2048, 1024, 2048, 2048, 2048, 1024]
- 0.072 secondes - moyenne : 4.000 [4, 4] - scores: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
- 127.394 secondes - moyenne : 1126.400 [1024, 2048] - scores: [1024, 1024, 1024, 2048, 1024, 1024, 1024, 1024, 1024, 1024]
- 0.015 secondes - moyenne : 4.000 [4, 4] - scores: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
- 27.588 secondes - moyenne : 588.800 [256, 1024] - scores: [1024, 256, 256, 512, 512, 1024, 512, 512, 256, 1024]
- 0.017 secondes - moyenne : 4.000 [4, 4] - scores: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

Il fut malgré tout difficile d'exécuter les stratégies de chacun
des groupes. Tous les modules n'étaient pas installables via un
fichier ``setup.py`` rarement réussi. Les tests unitaires ont
été réussis dans leur ensemble. Ci-dessous le programme
utilisé pour tester les stratégies après quelques modifications
dans les programmes reçus.

::

    from collections import OrderedDict
    from time import perf_counter as clock
    from ensae_teaching_cs.td_1a.cp2048 import evaluate_strategy

    strats = OrderedDict()

    from Projet_2048.module_jeu.fonctions_jeu_2048 import jeu2048

    def test_g1(game, state, moves):
        j = jeu2048()
        j.matrice = game.copy()
        return j.fin_jeu()

    strats['g1'] = test_g1

    from module2048.Ai import strategy_2048
    # trop long
    # strats['g2'] = lambda a, b: strategy_2048(a, 0, b)

    from the2048PythonStrategy import PPW_strategy
    strats['g2'] = lambda a, s, b: PPW_strategy(a, b)

    from bc2048.module_2048 import mouvement
    strats['g3'] = lambda a, s, b: mouvement(a, b)

    from pystrat2048_info import nextmovescorebest
    strats['g4'] = lambda a, s, b: nextmovescorebest(a, b)

    from ca_strategie2048 import NewMeilleurCoup
    strats['g5'] = lambda a, s, b: NewMeilleurCoup(a, 4, 1, 4)

    from cs_strat_finale import strategy_2048
    strats['g6'] = lambda a, s, b: strategy_2048(a, s, b)

    from gwpystrat.strategie import strategie
    strats['g7'] = lambda a, s, b: strategie(a, b)

    from Game.strategie import best_move, Board

    def g8(a, s, b):
        bb = Board(a)
        bb.deplacements_possibles()
        return best_move(bb, 2)

    strats['g9'] = peltier

    from pack2048.strategy2048 import snake_strategy
    strats['g9'] = lambda a, s, b: snake_strategy(a, b, 2)

    from Projet2048 import choixcoup
    strats['g10'] = lambda a, s, b: choixcoup(a, 3)

    from strat_2048_rvk.strategy import strategy
    strats['g11'] = strategy

    from Jeu2048 import get_best_direction
    strats['g12'] = lambda a, s, b: get_best_direction(a)

    from strat_max_case_vides.strateugie_max_cases_vides import ma_strategie
    strats['g13'] = lambda a, s, b: ma_strategie(a, b)

    from Module.fichier import resolve
    strats['g14'] = lambda a, s, b: resolve(a, 0, 5)

    from _2048.strategie import strat
    # strats['g15'] = lambda a, s, b: strat.strategiefinale(a,5)

    from strategy_zip.strategie import strategie
    strats['g16'] = lambda a, s, b: strategie(a, b)

    from Notremodule.Strategie import Strategie_points_3, Strategie_points_6
    # strats['g17'] = Strategie_points_3

    ntries = 10

    for name, value in reversed(strats.items()):
        print("+ name", name)
        cl = clock()
        rs = list(evaluate_strategy(value, ntries=ntries))
        dur = clock() - cl
        mi, ma = min(rs), max(rs)
        av = sum(rs) / len(rs)
        print("- %1.3f seconds - %1.3f [%d, %d] - scores: %s" % (dur, av, mi, ma, str(rs)))
