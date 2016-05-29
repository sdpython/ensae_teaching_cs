

.. _l-production:


Coder facilement, coder à plusieurs, qualité du code
====================================================

L'industrie logiciel a beaucoup évolué en 20 ans et plusieurs standards ont émergé
pour travailler à plusieurs et produire un logiciel avec peu d'erreurs.

(en construction)

.. toc::


Tests
-----


Tests unitaires
^^^^^^^^^^^^^^^

`tests unitaires <https://fr.wikipedia.org/wiki/Test_unitaire>`_

* `unittest <https://docs.python.org/3.5/library/unittest.html>`_
* `nose <http://nose.readthedocs.io/en/latest/>`_
* `pytest <http://pytest.org/latest/>`_
* `green <https://github.com/CleanCut/green>`_

*resource distantes*

Les tests unitaires sont difficiles à mettre en place dès qu'une resource distance est impliquée.
Le test peut échouer parce qu'internet n'est pas accessible, parce que le site web ne répond pas,
pour un problème d'identification. Ce problème est abordée au paragraphe suivant
avec le concept de `mock <https://fr.wikipedia.org/wiki/Mock_%28programmation_orient%C3%A9e_objet%29>`_.

*site web, serveur*

* :ref:`<test unitaire est flask <l-flask-unittest>`
* `Testing Flask Applications <http://flask.pocoo.org/docs/testing/>`_, `Flask testing <https://pythonhosted.org/Flask-Testing/>`_
* `Writing and running tests with Django <https://docs.djangoproject.com/en/1.9/topics/testing/overview/>`_

Pour vérifier certains aspects du site web tels qu'ils seront par un internaute :

* `Selenium with Python <http://selenium-python.readthedocs.io/>`_
* `Splinter <http://splinter.readthedocs.io/en/latest/>`_

*GUI*

* *autopy3 <https://pypi.python.org/pypi/autopy3/>`_

*autre module intéressants*

* `cricket <http://pybee.org/cricket/>`_


Mock
^^^^

* `unittest.mock <https://docs.python.org/3/library/unittest.mock.html>`_



Couverture des tests unitaires
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `coverage <http://coverage.readthedocs.io/>`_

Vitesse
-------


Profiling
^^^^^^^^^

* `profile <https://docs.python.org/3/library/profile.html>`_, 
  `cProfile <https://docs.python.org/3/library/profile.html#module-cProfile>`_
* `memory_profiler <https://pypi.python.org/pypi/memory_profiler>`_
* `line_profiler <https://pypi.python.org/pypi/line_profiler/>`_

*Affichage graphique*

* `vprof <https://github.com/nvdv/vprof>`_
* `SnakeViz <https://jiffyclub.github.io/snakeviz/>`_


Outils
++++++

Logiciel de suivi de source
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `git <https://git-scm.com/>`_
* `GitHub <https://github.com/>`_

Revue de code
-------------

Une `revue de code <https://fr.wikipedia.org/wiki/Revue_de_code>`_  
intervient avant la mise à jour du code d'un logiciel.
C'est l'occasion pour un dévelopeur de partager ses modifications avec le reste de son équipe
qui commentent les parties du code qui leur déplaisent ou approuvent si la mise à jour leur convient.


Style
+++++


Annotations
^^^^^^^^^^^

* `Tutorial <http://code.tutsplus.com/tutorials/python-3-function-annotations--cms-25689>`_
* `pep-484 <https://www.python.org/dev/peps/pep-0484/>`_, `pep-3107 <https://www.python.org/dev/peps/pep-3107/>`_
* `mypy <http://www.mypy-lang.org/>`_

PEP8
^^^^

* `pep8 <https://pypi.python.org/pypi/pep8>`_
* `pyflakes <https://pypi.python.org/pypi/pyflakes>`_, `flake8 <https://pypi.python.org/pypi/flake8/>`_
* `pylint <https://www.pylint.org/>`_


Design
^^^^^^

* petites fonctions
* séparation GUI / web / algorithme
* long process : prévoir une interruption, logging, processus asynchrone
* GUI réactive : asynchrone

à suivre