
.. _l-gui:

Interface graphique (GUI)
=========================

Les interfaces graphiques (GUI = Graphical User Interface)
sont essentielles dès qu'on souhaite interagir avec l'utilisateur
du programme mais ce n'est pas la seule option :

* **Site Web :** il faut un navigateur mais ce choix offre l'avantage
  de bénéficier de librairies javascripts pour fair à peu près tout.
  Le résultat est aussi portable, il peut s'exécuter partout où le
  navigateur fonctionne.
* **API REST :** c'est l'interface la plus simple mais elle nécessite
  que l'utilisateur sache programmer. Mais c'est aussi la seule interface
  que l'utilisateur peut automatiser.
* **GUI :** comme l'interface fait partie du programme, il faut s'assurer
  qu'elle fonctionne sur Mac, Linux, Windows.

**Design**

Dans le cas d'un site web, il est conseillé de développer une API REST
à laquelle le front end (la partie affichée dans le navigateur) fera 
appelle. Cela permet de dissocier le code graphique du reste. Cela permet
aussi d'automatiser - ce qui arrive nécessairement quand on manipule des données.
Cela permet aussi de changer d'interface si besoin.

Pour une interface graphique, il est aussi conseillé de séparer les calculs
de l'interface graphique. Cela permet d'en changer, et de plus facilement
automatiser par la suite. Quand le code est organisé sous forme de modules
indépendants communiquant via des API, il est plus facile d'en changer un
sans avoir à modifier les autres.

Si l'interface graphique est la direction choisie, on peut se pencher sur
le choix d'une librairie. En voici quelques-unes. Il faut vérifier deux ou
trois petits choses avant de commencer :

* **La license :** toutes les librairies ne permettent pas les mêmes usages,
  *PySide2* a dévié de *PyQt* pour contourner la license.
* **Maintenance :** Il faut vérifier que la librairie est toujours développée,
  dans le cas contraire, il est peu probable qu'elle fonctionne sur les
  versions récentes de python ou du système d'exploitation.
* **Plateforme :** certaines librairies ne fonctionnent pas partout,
  il faut vérifier qu'elles sont portables.
* **Objets graphiques :** le programme a-t-il besoin de graphes
  (pour visualiser des données par exemple), toutes ne le font pas
  ou ne proposent pas les mêmes graphiques. En développent un soi-même
  prend souvent beaucoup de temps.

* `tkinter <https://docs.python.org/3/library/tkinter.html>`_ :
  cette librairie est distribuée avec Python, c'est la plus simple,
  mais elle ne permet pas de tout faire.
* `wxPython <https://www.wxpython.org/>`_
  (ou `Phoenix <https://github.com/wxWidgets/Phoenix>`_),
  le nom *Phoenix* n'est sans doute pas le plus accueillant, comme un
  projet plusieurs fois ressuscité.
* `PyQt5 <https://pypi.org/project/PyQt5/>`_ : un design simple,
   existe depuis très longtemps
* `PySide2 <https://pypi.org/project/PySide2/#description>`_ : open source,
  similaire à *PyQt5*, une license plus permissive mais sans doute moins
  de contributeurs
* `Kivy <https://kivy.org/#home>`_ : initialement développé pour fonctionner
  aussi sur un téléphone
* `libavg <https://github.com/libavg/libavg>`_ : graphes
* `DearPyGui <https://github.com/hoffstadt/DearPyGui>`_ : graphes
* `PySimpleGUI <https://github.com/PySimpleGUI/PySimpleGUI>`_ :
  son nom dit beaucoup de choses
* `pygame/pygame2 <https://github.com/pygame/pygame>`_ :
  pour faire des jeux simplement en 2D
* `Godot <https://github.com/touilleMan/godot-python>`_ :
  pour faire des jeux en 3D, mais nécessite un investissement
  certain.
* `BeeWare <https://docs.beeware.org/en/latest/>`_ : 
  Python sur Android.

