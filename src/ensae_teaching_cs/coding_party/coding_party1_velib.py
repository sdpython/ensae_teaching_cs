#-*- coding: utf-8 -*-
"""
@file
@brief Une solution au problème proposée : 
`Reconstruction de trajectoire velib <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/coding_party_1.html>`_
"""
import os, pandas, random
from pyensae import download_data, DataVelibCollect
from pyquickhelper import str_to_datetime

def get_data(whereto):
    """
    récupère les données
    
    @param      whereto     destination
    """
    download_data('velib_synthetique.zip', website = 'xdtd', whereTo = whereto)    
    download_data('besancon.df.txt.zip', website = 'xdtd', whereTo = whereto)    
    
def enumerate_events(df):
    """
    construit la liste des événements
    
    @param      df      DataFrame
    @return             énumère événéments (ierator) ("file", "collect_date", "name", "lat", "lng", +1 ou -1)
    """
    df = df [["file", "collect_date", "name", "lat", "lng", 
            "available_bike_stands", "available_bikes"]]
    df = df.sort( ["name","file", "collect_date"])
    lastrow = None
    for row in df.values :
        if lastrow != None and lastrow[2] == row[2]:
            d1 = row[-2] - lastrow[-2] # nombre de place en plus
            d2 = row[-1] - lastrow[-1] # nombre de vélos en plus
            if d1 != 0 : 
                step = d1 // abs(d1)
                for i in range(1,abs(d1)+1):
                    yield tuple(row[:-2]) + (step,)
            elif d2 != 0 : 
                step = d2 // abs(d2)
                for i in range(1,abs(d2)+1):
                    yield tuple(row[:-2]) + (step,)
            
        lastrow = row
        
def vitesse( c,d):
    """
    calcule la vitesse d'un déplacement
    
    @param      c       tuple ("file", "collect_date", "name", "lat", "lng", +1 ou -1)
    @param      d       tuple ("file", "collect_date", "name", "lat", "lng", +1 ou -1)
    @return             vitesse
    """
    if c[0] == None or d[0] == None :
        # cas des vélos perdus
        if c[0] == None :
            if d[0] == None : return None
            else : return 0.0   # je ne sais pas trop quoi mettre 
        else :
            return 0.0 # je ne sais pas trop quoi mettre 
    else:
        lat1,lng1 = c[3],c[4]
        lat2,lng2 = d[3],d[4]
        dh = DataVelibCollect.distance_haversine(lat1,lng1,lat2,lng2)
        dt = d[1] - c[1]
        if dt.total_seconds() <= 0 : return 1e8  #infini
        return dh / (dt.total_seconds() / 3600)
    
def distance ( positif, negatif, appariement ):
    """
    calcul une distance pour un appariement conçu ici comme
    la variance de la vitesse de chaque déplacement
    
    @param      positif     vélos pris (ou l'inverse)
    @param      négatif     vélos remis (ou l'inverse)
    @return                 vitesse moyenne, distance
    """
    val = []
    for i,j in appariement:
        p = positif[i]
        n = negatif[j]
        d = vitesse(p,n)
        if d != None : val.append(d)
    
    mean = sum(val) / len(val)
    dev  = sum( (x - mean)**2 for x in val ) / len(val)
    return mean, dev**0.5
    
def appariement(events, iter = 1000, fLOG = print):
    """
    on veut apparier les événemens -1 aux événemens +1
    
    on s'attend aux colonnes suivantes:
        - "file", "collect_date", "name", "lat", "lng", +1 ou -1
    
    @param      events      list d'événements produits par la fonction
                            @see fn enumerate_events
    @param      iter        nombre d'itérations
    @param      fLOG        logging function
    @return                 tuple (mindist, moyenne, appariement, positif, negatif)
    """
    events = sorted(events)
    
    # on élimine tous les -1 du début (forcément des vélos pris avant la période d'étude)
    for i,ev in enumerate(events):
        if ev[-1] == 1 : break
    if i > 0 : del events[:i]

    # pareil de l'autre côté
    for i,ev in enumerate(reversed(events)):
        if ev[-1] == -1 : break
    if i > 0 : del events[len(events)-i:]
    
    default = (None,None, None, 0,0,0)
    
    positif = [ e for e in events if e[-1] > 0 ]
    negatif = [ e for e in events if e[-1] < 0 ]
    
    # on veut autant d'événements de chaque côté
    while len(positif) > len(negatif) :
        negatif.append( default ) 
    while len(positif) < len(negatif) :
        positif.append( default ) 
        
    appariement = [ (i,i) for i in range( 0, len(positif) ) ]
    vit, mindist = distance(positif, negatif, appariement)
    
    for it in range(0,iter):
        if it % 100 == 0 :
            fLOG("iteration ", it, ":", mindist, "vitesse ", vit)
        for ij in range(0,len(appariement)):
            i = random.randint(0,len(appariement)-1)
            j = random.randint(0,len(appariement)-1)
            if i == j : continue
            ki,kj = appariement[i],appariement[j]
            appariement[i] = ( ki[0],kj[1])
            appariement[j] = ( kj[0],ki[1])
            v, dist = distance(positif, negatif, appariement)
            if dist < mindist :
                mindist = dist
                vit = v
            else :
                appariement[i],appariement[j] = ki,kj
                
    moyenne = distance(positif, negatif, appariement)[0]
                
    return mindist, moyenne, appariement, positif, negatif
        
    
if __name__ == "__main__":
    dest = r"c:\temp\codpart1"
    if not os.path.exists(dest): os.makedirs(dest)
    get_data(dest)
    
    # récupère les données
    jeu = os.path.join(dest, "out_simul_bike_nb2_sp10_data.txt")
    df = pandas.read_csv(jeu, sep="\t")
    # conversion des dates
    df ["collect_date"] = df.apply( lambda r: str_to_datetime(r["collect_date"]),axis=1)
    #print(df.head())
    
    # on regarde s'il existe le fichier des trajectoires
    path = jeu.replace(".data.",".path.")
    if os.path.exists(path):
        dfp = pandas.read_csv(path, sep="\t")
        print(dfp.head())
        
    
    # on calcule les événements (1 vélo apparu, 1 vélo disparu)
    events = list(sorted(enumerate_events(df)))
    
    mindist, moyenne, appariement, positif, negatif = appariement(events)
    print("vitesse moyenne", moyenne)
    
    