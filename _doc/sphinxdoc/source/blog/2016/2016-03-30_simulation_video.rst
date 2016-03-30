

.. blogpost::
    :title: Créer une vidéo à partir d'une simulation
    :keywords: simulation, vidéo
    :date: 2016-03-30
    :categories: simulation
    
    C'est une petite vidéo construire à partir d'une simulation de population.
    Elle représente le taux de mortalité au sein d'une population
    en fonction de certaines hypothèses au niveau de la transmission.
    Mais ce n'est pas le sujet de cet article.
    Comment créer cette petite vidéo ?

    .. raw:: html
    
        <video width="400" autoplay="" height="400">
        <source src="http://www.xavierdupre.fr/enseignement/complements/epidemic.mp4" type="video/mp4" />
        </video>    
        
    On construit d'abord une série d'images toutes de la même taille,
    avec `matplotlib <http://matplotlib.org/>`_, 
    `pygame <http://pygame.org/hifi.html>`_ ou autre.
    Dans le cas présent, c'est la fonction
    :func:`pygame_simulation <ensae_teaching_cs.special.propagation_epidemic.pygame_simulation>`
    qui enregistre 1000 images.
    On utilise ensuite  `opencv <http://opencv.org/>`_ pour construire la 
    vidéo. C'est ce que fait la fonction 
    :func:`make_video <ensae_teaching_cs.helpers.video_helper.make_video>`.
    Un logiciel comme `MovieMaker <http://windows.microsoft.com/en-us/windows/movie-maker>`_
    permet de convertir la vidéo dans un format qui passe mieux dans un navigateur,
    d'ajouter une bande son ou de faire un court montage.
    