

.. blogpost::
    :title: Introduction aux Bag of Words, Statistical Machine Translation
    :keywords: bag of words, statistical machine translation
    :date: 2015-04-07
    :categories: machine learning, natural language processing
    
    Comment fonctionne les logiciels de traduction automatique tels
    Bing ou Google proposent ?
    L'article
    `Being good at programming competitions correlates negatively with being good on the job <http://www.catonmat.net/blog/programming-competitions-work-performance/>`_
    contient un lien vers une conférence de `Peter Norvig <http://en.wikipedia.org/wiki/Peter_Norvig>`_
    qui travaillent sur ce genre de problèmes chez Google.
    Il amène le public de manière assez intuitive depuis les 
    vers les `bag of words <http://fr.wikipedia.org/wiki/Sac_de_mots>`_
    `Statistical Machine Translation <http://en.wikipedia.org/wiki/Statistical_machine_translation>`_.
    En prenant temps de chercher deux ou trois termes qui traînent sur 
    certains graphes, on y découvrent également un algorithme :
    `Winnow <http://en.wikipedia.org/wiki/Winnow_%28algorithm%29>`_
    ou des sources de données :
    `ImageNet <http://image-net.org/>`_,
    `WordNet <https://wordnet.princeton.edu/wordnet/>`_.
    
    La présentation montre également un graphe illustrant
    l'évolution des performances en fonction du nombre de mots
    inclus dans l'ensemble d'apprentissage. Elle montre aussi
    que le modéle obtenant les meilleurs performances n'est pas forcément
    le même lorsqu'on apprend avec plus de données.