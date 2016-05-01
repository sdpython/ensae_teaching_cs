

.. blogpost::
    :title: Mise à jour des liens Jupyter
    :keywords: Jupyter, magic commands, documenation
    :date: 2016-05-01
    :categories: Jupyter
    
    IPython a beaucoup évolué depuis que j'ai commencé à écrire mes premiers 
    notebooks. Il a même changé de nom et certains liens vers la documentation
    étaient faux pour ne pas dire presque tous. J'ai commencé la mise à jour
    qui devrait s'étaler sur quelques mois. Voici les deux premiers commits :
    
    * `rename Csharp code (IPython --> jupyter) <https://github.com/sdpython/ensae_teaching_cs/commit/ffa990e2872c414dd0507660deb7d1d35bd2116a>`_
    * `ipython --> jupyter <https://github.com/sdpython/ensae_teaching_cs/commit/7d76635affce4fbfd165ae8d51d5d0aa9f2b42dc>`_
    
    Les notebooks sont unit testés donc le code présent fonctionne toujours.
    Il faudrait sans doute que j'ajoute une fonctionnalité dans `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_
    pour tester la validité des liens ajoutés à la documentation.