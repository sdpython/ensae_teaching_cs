
.. _l-codingparty1:


Coding Party 22 mai 2014
========================

On connaît toutes les minutes le nombre de places et vélos disponibles pour chaque station
d'une même ville de 2h du matin à 15h aujourd'hui. Il faut estimer la vitesse moyenne
d'une randonnée en vélo.


**Données réelles**


    * `Amiens - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/amiens.zip>`_ ou `Amiens - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/amiens.df.txt.zip>`_
    * `Besancon - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/besancon.zip>`_ ou `Besancon - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/besancon.df.txt.zip>`_
    * `Lyon - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/lyon.zip>`_ ou `Lyon - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/lyon.df.txt.zip>`_
    * `Mulhouse - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/mulhouse.zip>`_ ou `Mulhouse - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/mulhouse.df.txt.zip>`_
    * `Nancy - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/nancy.zip>`_ ou `Nancy - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/nancy.df.txt.zip>`_
    * `Paris - json <http://www.xavierdupre.fr/site2013/enseignements/tddata/paris.zip>`_ ou `Paris - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/paris.df.txt.zip>`_
    
Elles ont été fabriquées en suivant l'exemple : 
`Récupérer les données Velib et les visualiser <http://www.xavierdupre.fr/app/pyensae/helpsphinx/notebooks/pyensae_velib.html>`_.

**Données synthétiques**    

`données synthétiques - dataframe <http://www.xavierdupre.fr/site2013/enseignements/tddata/velib_synthetique.zip>`_

Ce fichier contient plusieurs simulations, chacune disponible avec deux fichiers :
    * La liste des trajets.
    * Les places et vélos disponibles pour chaque station (de Besançon).
    
Les simulations vérifient quelques contraintes :
    * Toutes les stations démarrent à 5 places et vélos disponibles.
    * Il peut y avoir 1,2,3, 5, 10 vélos qui circulent en parallèle. Chaque nombre
      fait l'objet d'une simulation différente.
    * Au bout d'une heure, les vélos retournent à la première station à proximité (si elle est vide).



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
