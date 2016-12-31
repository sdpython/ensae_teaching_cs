
.. blogpost::
    :title: Map Reduce et Skew Join
    :keywords: map reduce, skew join
    :date: 2015-07-17
    :categories: map-reduce
    :lid: blog-skew-join

    .. index:: skew join

    Le langage `PIG <https://pig.apache.org/>`_ s'occupe de beaucoup de choses
    pour celui qui l'utilise. Entre autres, il s'occupe de distribuer les calculs
    sans trop avoir d'a priori sur les données qu'il traite.
    Mais comment concevoir une répartition des calculs qui fonctionne
    pour la plupart des cas ? L'un des problèmes les plus fréquents
    est celui du `skewed join <https://cwiki.apache.org/confluence/display/Hive/Skewed+Join+Optimization>`_ :
    on cherche à fusionner deux tables dont les clés ne sont pas distribuée de manière uniforme,
    loin de là.
    L'article suivant
    `Assignment Problems of Different-Sized Inputs in MapReduce <http://arxiv.org/abs/1507.04461>`_
    creuse aborde quelques aspects de cette problématique.
