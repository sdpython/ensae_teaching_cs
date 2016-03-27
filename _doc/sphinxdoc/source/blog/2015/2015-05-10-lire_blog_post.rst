

.. blogpost::
    :title: Lire les articles de blog
    :keywords: blog, pyrsslocal
    :date: 2015-05-10
    :categories: blog
    
    Il suffit d'aller sur internet pour les lire le contenu
    de ce blog mais c'est parfois un peu fastidieux d'en suivre plusieurs.
    Et puis blogger apparaît parfois comme suranné.
    On publie
    plus sur les réseaux sociaux comme Facebook, Linkedin ou Twitter
    ou la visibilité est meilleure et les retours plus immédiats.
    Les articles sont toutefois peu techniques et plus courts.
    D'ailleurs, je ne crois qu'on publie vraiment, on communique plutôt.
    Le blog est un moment d'écriture et de lecture qu'on passe seul. 
    Et pour lire
    ces longs textes, des solutions existent comme
    `Digg Reader <http://digg.com/reader>`_,
    `Feedly <http://feedly.com/i/welcome>`_.
    Ce n'est pas toujours gratuit et il faut d'identifier
    et puis dans ce module Python, il existe une façon de lire
    ce blog ::
    
        from pyquickhelper.pycode import write_module_scripts
        from ensae_teachins_cs import __blog__
        write_module_scripts(".", blog_list=__blog__)
    
    Cette fonction créé quelques fichiers commençant par ``auto_rss*.py``.
    Si vous êtes sous Windows, il suffit d'exécuter ``auto_run_blog.bat``
    pour lancer le navigator par défaut avec et découvrir les derniers articles
    publiés. Il est facile d'ajouter d'autres blog mais je vous laisse découvrir
    par vous même comment faire. Après tout, c'est un site pour apprendre 
    à programmer, à quoi ça sert que j'explique tout si c'est pour ne plus rien
    faire par soi-même.    
    Le tout s'appuie sur le module
    `pyrsslocal <http://www.xavierdupre.fr/app/pyrsslocal/helpsphinx/>`_.
    Vous y découvrirez quelques copies d'écran.
    