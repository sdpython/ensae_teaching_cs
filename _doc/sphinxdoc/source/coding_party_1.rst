
.. _l-codingparty1:


Coding Party 22 mai 2014 : inférer des trajectoires de vélos
============================================================

Le problème
-----------

On connaît toutes les minutes le nombre de places et vélos disponibles pour chaque station
d'une même ville de 2h du matin à 15h aujourd'hui. Il faut estimer la vitesse moyenne
d'une randonnée en vélo.


Données réelles
^^^^^^^^^^^^^^^


* `Amiens - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/amiens.zip>`_ ou `Amiens - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/amiens.df.txt.zip>`_
* `Besancon - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/besancon.zip>`_ ou `Besancon - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/besancon.df.txt.zip>`_
* `Lyon - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/lyon.zip>`_ ou `Lyon - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/lyon.df.txt.zip>`_
* `Mulhouse - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/mulhouse.zip>`_ ou `Mulhouse - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/mulhouse.df.txt.zip>`_
* `Nancy - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/nancy.zip>`_ ou `Nancy - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/nancy.df.txt.zip>`_
* `Paris - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/paris.zip>`_ ou `Paris - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/paris.df.txt.zip>`_
    
Elles ont été fabriquées en suivant l'exemple : 
`Récupérer les données Velib et les visualiser <http://www.xavierdupre.fr/app/pyensae/helpsphinx/notebooks/pyensae_velib.html>`_.

Données synthétiques
^^^^^^^^^^^^^^^^^^^^

`données synthétiques - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/velib_synthetique.zip>`_

Ce fichier contient plusieurs simulations, chacune disponible avec deux fichiers :

* La liste des trajets.
* Les places et vélos disponibles pour chaque station (de Besançon).
    
Les simulations vérifient quelques contraintes :

* Toutes les stations démarrent à 5 places et vélos disponibles.
* Il peut y avoir 1,2,3, 5, 10 vélos qui circulent en parallèle. Chaque nombre
  fait l'objet d'une simulation différente.
* Au bout d'une heure, les vélos retournent à la première station à proximité (si elle est vide).

Une façon d'estimer la vitesse moyenne des vélos est de reconstituer les trajectoires
des vélos à partir des décomptes des places et vélos disponibles
dans chaque stations.

Les données synthétiques fournissent à la fois les décomptes et les trajectoires
afin d'évaluer un algorithme. Une fois que celui-ci est bien calé, on peut 
l'évaluer sur les données réelles.

    
Description des données
^^^^^^^^^^^^^^^^^^^^^^^

Les colonnes importantes :

* **lng,lat** : longitude, latitude
* **name** : nom de la station
* **number** : numéro de la station
* **available_bike_stands** : nombre de places disponibles
* **available_bikes** : nombre de vélos disponibles
* **file** : fichier d'où sont tirés les données (à chaque minute, toutes les données relatives
  à toutes les stations sont mises dans un fichier, c'est l'identifiant unique)
* **collect_date** : date à laquelle sont collectées les données (elle peut légèrement varier
  au sein d'un même fichier)
      
Autres colonnes (uniquement pour les données réelles) :

* **status** : une station peut être fermée, en général, elle est ouvert (``OPEN``)
* **last_update** : dernière mise à jour de la station, cela correspond à la date du dernier mouvement

Bouts de code
^^^^^^^^^^^^^

On fournit le code de la `distance de Haversine <http://en.wikipedia.org/wiki/Haversine_formula>`_ ::

    def distance_haversine(lat1, lng1, lat2, lng2):
        radius = 6371
        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
                * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c
        return d   
        
Pour récupérer les données ::

    from pyensae import download_data
    download_data('velib_synthetique.zip', website = 'xdtd', whereTo = whereto)    
    download_data('besancon.df.txt.zip', website = 'xdtd', whereTo = whereto)  
    
Pour les charger dans un DataFrame ::

    import pandas
    df = pandas.read_csv(jeu, sep="\t", encoding="utf8")

Solutions
---------

Le problème était un peu trop complexe pour être résolu en quelques heures.
Le premier jeu de données avec un seul vélo au plus pouvant circuler a été
traité par la plupart mais il ne présentait pas de difficulté. Pour les autres jeux,
ce fut une autre paire de manches. Néanmoins, deux idées se sont dégagées :

#. une solution basée sur l'appariement des sorties et des entrées de vélos,
#. une solution d'inspiration bayésienne (Monte Carlo).
    
Si entre deux minutes consécuties et pour les mêmes stations, 
le comte des places disponibles (ou celui des vélos) évolue, on est certain
qu'un vélo est arrivé ou est parti. A partir de là, il est possible de construire 
pour l'ensemble des stations deux séries :
    
#. la série des vélos retirés d'une station,
#. la série des vélos réposés à une station.

Ces séries n'ont pas forcément le même nombre d'élément mais cela devrait être marginal.
On peut considérer qu'à chaque vélo retiré correspond un vélo reposé. Il ne reste plus
qu'à apparié chaque élément de ces deux séries. Pour cela, il faut construire 
un coût d'appariement (une fonction d'erreur) et implémenter un algorithme
qui minimise cette fonction de coût. 

C'est l'option que j'ai choisie (voir :func:`appariement <coding_party.coding_party1_velib.appariement>`).
C'est à mon sens celle qui était le plus facile à coder en quelques heures. 
Elle présente deux inconvénients : 

#. Je ne suis pas sûr qu'elle passe à l'échelle (la ville de Paris a plus de 1000 stations).
#. Elle ne fonctionne pas extrêmement bien sur les jeux de données que j'ai simulés : 
   le jeu avec deux vélos en parallèle est assez cyclique. Si on considère les deux séries 
   de vélos (retirés et reposés), elles se comporte comme deux peignes.
   Décaler ces deux peignes pour apparier leur dents n'a pas beaucoup d'impact
   sur la fonction de coût mais il a un grand impact sur la vitesse moyenne.
       
`Voici <https://github.com/sdpython/ensae_teaching_cs/commit/7da003de4bb8bac7d3a59a5cfd372d8187cbc9aa>`_ 
ce que j'ai rajouté en vitesse pour essayer d'avoir une solution probable.       
       
Pour la solution d'inspiration bayésienne, elle revient à prendre des hypothèses 
sur la vitesse moyenne. J'en dirai peut-être plus un peu plus tard. En attendant,
vous pouvez reproduire la solution de l'appariement dans ce notebook :
`Déterminer la vitesse moyenne des vélib <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/expose_velib.html>`_.




