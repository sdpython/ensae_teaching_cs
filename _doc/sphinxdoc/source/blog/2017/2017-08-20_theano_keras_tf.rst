
.. blogpost::
    :title: Installer theano et un compilateur C++
    :keywords: python, theano, keras
    :date: 2017-08-20
    :categories: modules
    :lid: blog-install-theno-keras

    epkg:`theano` est un module difficile à installer
    car il utilise une compilation C++ pour optimiser les
    calculer que le programmeur demmande. Cela veut dire qu'il
    fait appel à un compilateur C++ pour convertir des instructions
    :epkg:`Python` en un code qui s'exécute rapidement.
    Les portables ont peu souvent des processeurs GPU mais rien n'empêche
    de développer un programme de deep learning en CPU d'abord.
    C'est plus facile sous Linux (ou sous
    `Windows Subsystem for Linux <https://blogs.windows.com/buildingapps/2017/08/08/windows-subsystem-linux-windows-server/>`_.
    Il suffit d'installer `g++ <https://en.wikipedia.org/wiki/GNU_Compiler_Collection>`_ :

    ::

        sudo apt-get install g++

    Sous Windows, c'est un peu plus compliqué mais à peine plus long.
    Il faut lire l'article de blog :
    `Theano and Mingw <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2017/2017-08-17_theano.html>`_.
