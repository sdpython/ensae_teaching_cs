

.. blogpost::
    :title: Numpy, Hadoop, PIG, Java
    :keywords: Map Reduce, Java, PIG, Hadoop, JyNI, Jep
    :date: 2016-01-25
    :categories: Hadoop
    
    Le fait qu'on puisse utiliser des scripts 
    `Python <https://www.python.org/>`_
    dans un script `PIG <https://pig.apache.org/>`_ est un peu trompeur.
    De là à penser que la librairie `numpy <http://www.numpy.org/>`_ serait utilisable...
    Tout d'abord, les versions officielles de numpy et Python sont
    implémentaires en `C <https://fr.wikipedia.org/wiki/C_(langage)>`_
    voire un peu de `Fortran <https://fr.wikipedia.org/wiki/Fortran>`_
    et Hadoop / PIG est implémenté en 
    `java <https://fr.wikipedia.org/wiki/Java_%28langage%29>`_
    qui a l'avantage de bénéficier d'un 
    `garbage collector <https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)>`_
    contrairement au langage C.
    Ceci explique que la version de Python utilisée par PIG 
    pour définir des UDF (User Defined Function)
    est `Jython <http://www.jython.org/>`_. 
    Utiliser numpy dans une fonction UDF n'est pas simple.
    La première direction consiste à utiliser une version java 
    de numpy :
    
    * `JyNI <http://jyni.org/>`_: 
      JyNI is a compatibility layer with the goal to enable Jython to use native CPython extensions like NumPy or SciPy.
    * `jep <https://pypi.python.org/pypi/jep/>`_: 
      Jep embeds CPython in Java through 
      `JNI <https://en.wikipedia.org/wiki/Java_Native_Interface>`_
      and is safe to use in a heavily threaded environment.
    
    Deuxième direction, utiliser le streaming en ligne de commande.
    Le script écrit en Python recevra du texte, devra le parser
    pour former les matrices dont il a besoin, faire son calcul,
    et sortir la matrice résultante sous forme de texte.
    
    Dans les deux cas, les scripts ont besoin de dépendences pour s'exécuter.
    Il faut soit que ces dépndences soient disponibles sur chaque machine
    du cluster Hadoop, soit qu'elles soient référencées dans le script PIG
    lui-même afin qu'elles soient distribuées sur chaque machine.
    
    
    