#coding:latin-1
def GraphOHLC (title, dates, ohlc, file, size = (800,400), t1 = 0, t2 = -1) :
    """dessine une série financière avec matplotlib
    - title est une titre
    - dates est une liste de date
    - ohlc est une liste de dictionnaire avec les clés 
                      ("Open", "High", "Low", "Close", "Volume")
    - file est un nom de fichier, le graphe y sera sauvegardé
    - size est la taille désirée pour le graphique
    - t1 est l'indice de la première date du graphique
    - t2 est l'indice de la dernière date du graphique
    """
    
    # on coupe la série si besoin
    if t2 == -1 : t2 = len (dates)
    dates = dates [t1:t2]
    ohlc = ohlc [t1:t2]
    
    import pylab
    
    # on crée les labels pour les abscisses
    # sans afficher toutes les dates car elles deviennent illisibles sinon
    # on en affiche que 10
    ind  = pylab.arange (len (dates))
    lab  = ["" for i in ind]
    for i in range (0,len (dates),len(dates)/10) : lab [i] = dates [i]

    # on crée la figure
    fig  = pylab.figure (figsize=(size [0]/100, size [1]/100))
    ax   = fig.add_subplot(111)
    
    # la première série à tracer est celle des volumes sous forme d'histogramme
    for i in range (0, len (ohlc)) :
        oh = ohlc [i]
        
        # l'histogramme est vert si c'est un jour de hausse
        # rouge si c'est un jour de baisse
        if i == 0 : co = (0.5,0.5,0.5)
        elif ohlc [i]["Close"] > ohlc [i-1]["Close"] : co = (0.0,1.0,0.0)
        else : co = (1.0,0.0,0.0)
        if len (dates) > 300 : 
            pylab.plot ( [i, i], [0, oh ["Volume"]], "k", color = co)
        elif len (dates) > 100 : 
            pylab.plot ( [i, i], [0, oh ["Volume"]], "k", \
                                         linewidth = 2.0, color = co)
        else : 
            pylab.plot ( [i, i], [0, oh ["Volume"]], "k", \
                                          linewidth = 4.0, color = co)
        
    # on écrit la légende du volume
    v = [0.0 for i in ind]
    pylab.plot (ind, v, "c.")
    pylab.ylabel ("volume")
        
    # on construit un second axe au graphique pour la série des prix
    ymin, ymax = pylab.ylim()
    pylab.ylim (ymin, ymax*3)
    pylab.xticks (ind, lab, fontsize = "small", rotation = 13  )
    ax2 = pylab.twinx()
    
    # puis un dessine les prix sur le graphique selon le même schéma, 
    # la même série de points
    # (i-0.5, Open) (i,Open) (i,Low) (i,High) (i,Close) (i+0.5,Close)
    for i in range (0, len (dates)) :
        oh = ohlc [i]
        co = (0.0,0.0,1.0)
        pylab.plot ([i-0.5, i], [oh["Open"],  oh["Open"]],  "k", \
                                      linewidth = 1.0, color = co)
        pylab.plot ([i, i],     [oh["Low"],   oh["High"]],  "k", \
                                      linewidth = 1.0, color = co)
        pylab.plot ([i, i+0.5], [oh["Close"], oh["Close"]], "k", \
                                      linewidth = 1.0, color = co)

    # on termine par le titres, la légende du second axe et celles des abscisses
    pylab.title   (title)
    pylab.ylabel  ("euros")
    pylab.xticks  (ind, lab, fontsize = "small", rotation = 13)
    pylab.xlabel  ("dates")
    # il ne reste plus qu'à sauver la figure
    pylab.savefig (file, orientation='paysage')