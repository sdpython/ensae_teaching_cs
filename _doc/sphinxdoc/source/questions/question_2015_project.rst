
.. _question_projet_2015:

Questions Projets 2015
======================

.. contents::
    :local:

.. _question_2015_projet_1A:

.. index:: design, génie logiciel

C'est quoi le design dans un programme informatique ?
+++++++++++++++++++++++++++++++++++++++++++++++++++++

L'article de blog :ref:`blog-design-program` répond en partie à cette question.
Lorsqu'on est chercheur, on s'intéresse surtout au design des algorithmes afin
de concevoir des méthodes mathématiques qui soient modulaires. L'algorithme
de la descente du gradient peut s'appliquer à différents types de problèmes.
Comment les implémenter pour écrire le moins de code possible ?

Le `téléphone en kit <http://ecrans.liberation.fr/ecrans/2015/03/03/ara-le-telephone-en-kit-selon-google_1213246>`_
illustre cet aspect design. Il est difficile d'improviser ce type de lego électronique.
Outre le design artistique de l'oject, il y a les aspects branchements électroniques.

On peut également aborder les aspects de génie logiciel. Comment s'assurer que le code
produit contient le moins de bug possibles ? Tous les logiciels sont buggés (ont au moins un bug)
et pourtant les avions sont truffés de logiciels. Comme tout produit industriels,
un logiciel doit être testés et la méthode la plus commune sont les tests unitaires.
Un code informatique est plus ou moins facile à tester selon la façon dont il est
implémenté.

Ce genre de préoccupation paraît futile à tous ceux qui commencent à programmer,
beaucoup pour ceux qui ont passés plusieurs à chercher une erreur dans une partie
insufissamment testée.

.. _question_2015_projet_2_2A:

Le R2 est proche de 1 et le modèle est mauvais (séries temporelles) ?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Le coefficient :math:`R^2` qui juge de la pertinence d'une régression
est souvent proche de 1 dans le cas de la prédiction de le valeur d'une action pour demain
à partir de ses valeurs passées. La valeur de l'action est considérée comme
une série temporelle :math:`(Y_t)`.
En fait, le :math:`R^2` est aussi grand si on
utilise :math:`Y_{t-1}` comme estimateur de :math:`Y_t`.
Cela signifie que la série temporelle n'est pas stationnaire et que la tendance
est d'un ordre de grandeur plus grand que les oscillations locales.
Dans le cas de l'action, il passer à la série dérivée des rendements.
Dans le cas général, il faudrait soit enlever la tendance soit comparer le
:math:`R^2` obtenu à celui obtenu en utilisant :math:`Y_{t-1}` comme prédiction.
