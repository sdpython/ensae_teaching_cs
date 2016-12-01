

.. _l-siteflask:


Site Web
========

En entreprise, on a parfois besoin d'exposer de partager des données d'une machine 
à une autre, d'exécution des scripts sur une machine distante sans avoir
à installer le langage Python. Dans le cas, le module
`Flask <http://flask.pocoo.org/>`_ permet de créer 
facilement un site web.

.. contents::
    :local:

Tutoriel
--------

C'est un notebook qui fait partie de l'ensemble 
:ref:`Python pour un économiste <l-eco-website>`.


Outils pour tester un site
--------------------------

* :ref:`f-simpleflasksite`
* :ref:`f-flaskhelper`

.. _l-flask-unittest:


Unit Test
---------

Cet exemple contient une fonction ``shutdown`` qui permet de 
dire au serveur de s'interrompre si jamais un lui demande un certain
url. Dans ce cas, on peut écrire un test unitaire qui :

* démarrer le serveur depuis un thread
* essaye différents urls et vérifie le résultat

Cela donne ::

    import sys, os, unittest, requests
    from pyquickhelper.loghelper import fLOG, get_url_content
    from src.ensae_teaching_cs.td_1a.simple_flask_site import app
    from src.ensae_teaching_cs.td_1a.flask_helper import FlaskInThread


    class TestSimpleFlask (unittest.TestCase):

        def test_flask(self) :
            fLOG (__file__, self._testMethodName, OutputPrint= __name__ == "__main__")
            
            th = FlaskInThread(app, host="localhost", port=8025)
            th.start()
            
            site = "http://localhost:8025/"
            
            # main page
            c = get_url_content(site)
            assert "Simple Flask Site"
            
            # exception
            c = get_url_content(site + "help/exception")
            assert "STACK:" in c
            
            # help for 
            c = get_url_content(site + "help/ask/for/help")
            fLOG(c)
            assert "help for command: ask/for/help" in c
            
            # shutdown
            c = requests.post(site + "shutdown/")
            fLOG(c.text)
            assert "Server shutting down..." in c.text
            
            
La fonction `get_url_content <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/loghelper/url_helper.html?highlight=get_url_content#pyquickhelper.loghelper.url_helper.get_url_content>`_
récupère le contenu d'une page HTML. Pour faire bien, elle devrait 
prendre un compte un timeout.

L'autre astuce consiste à attraper les exceptions dans le serveur
puis à retourner la pile des exceptions afin que le programmeur
débugge facilement le code du serveur. Dans le cas contraire,
il faut ajouter des lignes logs dans le serveur pour savoir
ce qu'il fait. C'est de toutes façons une bonne habitude à prendre.

A noter : le module `requests <http://docs.python-requests.org/en/latest/>`_
simplifie beaucoup de choses dès qu'on commence à se pencher 
sur des problèmes d'authentification.


Autres alternatives
-------------------

Pour un plus petit site, il existe le module
`bottle <http://bottlepy.org/docs/dev/index.html>`_
mais celui ne permet d'écrire simplement 
des tests unitaires.
Pour des sites plus conséquents, la référence est
`django <https://www.djangoproject.com/>`_.

`autobahn/python <http://autobahn.ws/python/>`_
permet d'écrire simplement des sites qu'on programme
par événements. Cela permet de ne pas laisser le serveur bloqué
pendant qu'il effectue un traitement.
Enfin, `brython <http://www.brython.info/>`_ permet de remplacer le 
`javascript <https://fr.wikipedia.org/wiki/JavaScript>`_ par *python*.
Plus simple à coder lorsqu'on ne connaît pas `javascript <https://fr.wikipedia.org/wiki/JavaScript>`_ 
mais cela revient à se priver de tout un tas d'outils écrit dans ce langage :
`jquery <http://jquery.com/>`_,
`angularJS <https://angularjs.org/>`_,
`node.js <http://nodejs.org/>`_,
`meteor <https://www.meteor.com/>`_ ...

Une dizaine de modules Python permettant de créer un site web
sont comparées par
`Python's Web Framework Benchmarks <http://klen.github.io/py-frameworks-bench/>`_.
`django <https://www.djangoproject.com/>`_ est le choix le plus connu
pour un site web professionnel écrit en Python.
`Flask <http://flask.pocoo.org/>`_ est la référence pour un site minimaliste
ou `micro-frameworks <https://wiki.python.org/moin/WebFrameworks>`_ mais
il ne gère pas très bien la désynchronisation et une seule requête peut être
géré en même temps.
Le projet `falcon <https://falconframework.org/>`_ est plus rapide.

* `Django vs Flask vs Pyramid: Choosing a Python Web Framework <https://www.airpair.com/python/posts/django-flask-pyramid>`_
* `What are the best Python microframeworks? <https://www.slant.co/topics/532/~python-microframeworks>`_
* `13 Best Python Framework For Python Geeks <http://www.techaltair.com/best-python-framework-python-geeks/>`_

