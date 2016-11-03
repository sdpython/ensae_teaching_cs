

.. blogpost::
    :title: Coordonnées des données carroyées
    :keywords: carroyées, carreaux, INSEE, carroyage, Spatial reference system, EPSG, shapefiles
    :date: 2016-11-03
    :categories: plotting
    :lid: blog-donnees-carroyees-2016
    
    Les `données carroyées <http://www.insee.fr/fr/themes/detail.asp?reg_id=0&ref_id=donnees-carroyees>`_
    sont fournies par l'INSEE et proposent différentes variables
    économiques agrégées par carreaux : 
    *Un carroyage est un découpage de l'espace géographique en mailles régulières de forme carrée et de taille fixe.*
    Il survient toujours un moment où on cherche à représenter ses données
    qui sont localisées avec un système de coordonnées :
    `Lambert Azimutal Equal Area <http://www.insee.fr/fr/themes/detail.asp?reg_id=0&ref_id=donnees-carroyees&page=donnees-detaillees/donnees-carroyees/donnees_carroyees_doc.htm>`_.
    Pour les convertir an longitude, latitude, il faut utiliser le module 
    `pyproj <https://pypi.python.org/pypi/pyproj>`_.
    Exemple : `Conversion de coordonnées <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/notebooks/chsh_geo.html>`_.
    La plupart des systèmes de coordonnées (ou *Spatial reference system*) sont identifiés par un code 
    `EPSG <https://en.wikipedia.org/wiki/International_Association_of_Oil_%26_Gas_Producers#European_Petroleum_Survey_Group>`_. 
    Dans le cas des données carroyées, le code est **EPSG:3035**.
    Il est répertorié sur `spatialreference.org <http://spatialreference.org/ref/epsg/3035/>`_
    qui listent façons de l'écrire avec différents outils.
    Lorsqu'on télécharge des fichiers shapefiles, elles viennent souvent avec un fichier 
    *.prj* qui décrit le système de coordonnées utilisé. Le site 
    `prj2epsg <http://prj2epsg.org/search>`_ permet d'obtenir le code
    *EPSG* correspondant ouvrant la porte à toutes sortes de conversions.