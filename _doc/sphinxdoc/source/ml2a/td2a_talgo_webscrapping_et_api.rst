
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. _l-2a-scraping:

Web-scraping et API
+++++++++++++++++++

Le site contient quelques notebooks à propos du :epkg:`scraping`.
Je distingue souvent deux niveaux de difficultés. Le plus simple
est d'utiliser une :epkg:`API REST`. On récupère alors des informations
formatées prêtes à être utilisées. Ces API sont souvent stables
mais nécessitent de s'authentifier.

Lorsque ces API n'existent pas, on peut alors
récupérer le contenu de pages HTML mais il faut se débrouiller
pour extraire le contenu intéressant des pages le plus souvent
avec des :epkg:`expressions régulières`.

Ca marche plutôt bien si ce n'est que ce n'est pas très
stables, les sites ont tendance à mettre à jour leurs
styles souvent ce qui nécessite quelques mises à jour
d'expressions régulières si on souhaite mettre en place
un processus régulier. Les sites se protègent également
contre les adresses IP qui les scrapent trop fréquemment.
Avec quelques règles simples, il est possible de distinguer
un humain d'un robot qui récupère un contenu.

Enfin, la dernière difficulté vient du :epkg:`javascript`
qui change le contenu de la page après son chargement.
Il faut donc exécuter ce code si on souhaite récupérer
un contenu tel qu'il est affiché. Ce n'est pas le plus
évident mais surtout ça ralentit beaucoup la récupération
des données. Pour ce faire, le plus simple est d'utiliser le
module :epkg:`selenium`.

*Notebooks*

.. toctree::
    :maxdepth: 1

    ../notebooks/2018-10-02_scraping_recuperer_images
    ../notebooks/TD2A_eco_les_API

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_eco_scraping
    ../notebooks/_gs2a_eco_api

*Ressources*

* `API de geocoding <https://www.data.gouv.fr/fr/faq/reuser/>`_
* `adresse.data.gouv.fr <https://adresse.data.gouv.fr/csv/>`_

*Modules*

* `beautifulsoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_
* `ghost.py <http://jeanphix.me/Ghost.py/>`_
* `selenium <http://selenium-python.readthedocs.io/>`_
* `scrapy <https://scrapy.org/>`_
* `scrapoxy <http://scrapoxy.io/>`_, `python api <https://github.com/fabienvauchelles/scrapoxy-python-api>`_
