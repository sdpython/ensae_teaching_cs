#-*- coding: utf-8 -*-
"""
@file
@brief Code implémentant la première solution proposée à `Parcourir les rues de Paris <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/rue_paris_parcours.html>`_.
"""
import os, sys, copy, random, math
import pyensae

def distance_paris(lat1, lng1, lat2, lng2):
    """
    distance euclidienne approchant la distance de Haversine (uniquement pour Paris)

    @param      lat1    lattitude
    @param      lng1    longitude
    @param      lat2    lattitude
    @param      lng2    longitude
    @return             distance
    """
    return ((lat1-lat2)**2+(lng1-lng2)**2)**0.5 * 90

def distance_haversine(lat1, lng1, lat2, lng2):
    """
    calcule la distance de Haversine `Haversine formula <http://en.wikipedia.org/wiki/Haversine_formula>`_

    @param      lat1    lattitude
    @param      lng1    longitude
    @param      lat2    lattitude
    @param      lng2    longitude
    @return             distance
    """
    radius = 6371
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lng2-lng1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d

def get_data(whereTo = "."):
    """
    Retourne les données des rues de Paris. On suppose que les arcs sont uniques
    et qu'il si :math:`j \rightarrow k` est présent, :math:`j \rightarrow k` ne l'est pas.
    Ceci est vérifié par un test.

    @param      whereTo         répertoire dans lequel télécharger les données
    @return                     liste d'arcs

    Un arc est défini par un 6-uple contenant les informations suivantes :
        - v1: indice du premier noeud
        - v2: indice du second noeud
        - ways: sens unique ou deux sens
        - p1: coordonnées du noeud 1
        - p2: coordonnées du noeud 2
        - d: distance
    """
    data = pyensae.download_data("paris_54000.zip", whereTo=whereTo)
    name = data[0]
    with open(name, "r") as f : lines = f.readlines()

    vertices = []
    edges    = [ ]
    for i,line in enumerate(lines) :
        spl = line.strip("\n\r").split(" ")
        if len(spl) == 2 :
            vertices.append ( (float(spl[0]), float(spl[1]) ) )
        elif len(spl) == 5 and i > 0:
            v1,v2 = int(spl[0]),int(spl[1])
            ways = int(spl[2]) # dans les deux sens ou pas
            p1 = vertices[v1]
            p2 = vertices[v2]
            edges.append ( (v1,v2,ways,p1,p2, distance_haversine(p1[0],p1[1],p2[0],p2[1]) ))
        elif i > 0 :
            raise Exception("unable to interpret line {0}: ".format(i) + line)

    pairs = { }
    for e in pairs :
        p = e[:2]
        if p in pairs:
            raise ValueError("unexpected pairs, already present: " + str(e))
        pairs[p] = True

    return edges

def graph_degree(edges):
    """
    calcul le degré de chaque noeud

    @param      edges       list des arcs       (voir ci-dessus)
    @return                 degrés
    """
    nb_edges = { }
    for edge in edges :
        v1,v2 = edge[:2]
        nb_edges[v1] = nb_edges.get(v1,0)+1
        nb_edges[v2] = nb_edges.get(v2,0)+1
    return nb_edges

def possible_edges(edges, threshold, fLOG = None, distance = distance_haversine):
    """
    Construit la liste de tous les arcs possibles en filtrant sur la distance à vol d'oiseau.

    @param      edges       liste des arcs
    @param      threshold   seuil au-delà duquel deux noeuds ne seront pas connectés
    @param      fLOG        logging function
    @param      distance    la distance de Haversine est beaucoup trop longue sur de grands graphes, on peut la changer
    @return                 arcs possibles (symétrique --> incluant edges)
    """
    vertices = { e[0]:e[3] for e in edges }
    vertices.update ( { e[1]:e[4] for e in edges } )

    possibles = { (e[0],e[1]) : e[-1] for e in edges }
    possibles.update ( { (e[1],e[0]) : e[-1] for e in edges } )
    initial = possibles.copy()
    for i1,v1 in vertices.items():
        for i2,v2 in vertices.items():
            if i1 >= i2 : continue
            d = distance(* (v1 +v2))
            if d < threshold :
                possibles [ i1,i2 ] = d
                possibles [ i2,i1 ] = d

    if fLOG is not None:
        total_possible_edges = (len(vertices)**2 - len(vertices))/2
        possible_edges = len(possibles)//2
        leninit = len(edges)
        fLOG("original",leninit,"/",total_possible_edges,"=", leninit/total_possible_edges)
        fLOG("addition",possible_edges-leninit,"/",total_possible_edges,"=", (possible_edges-leninit)/total_possible_edges)

    return possibles

def bellman(edges, iter = 20, fLOG = print, allow = None, init = None) :
    """
    Implémente l'algorithme de `Bellman-Ford <http://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford>`_.

    @param      iter        nombre d'itérations maximal
    @param      fLOG        logging function
    @param      allow       fonction déterminant si l'algorithme doit envisager cette liaison ou pas
    @param      init        initialisation (pour pouvoir continuer après une première exécution)
    @return                 listes des arcs et des distances calculées
    """

    if init is None :
        init = { (e[0],e[1]) : e[-1] for e in edges }
        init.update ( { (e[1],e[0]) : e[-1] for e in edges } )

    if allow is None:
        allow = lambda e : True

    edges_from = {  }
    for e in edges :
        if e[0] not in edges_from : edges_from[e[0]] = []
        if e[1] not in edges_from : edges_from[e[1]] = []
        edges_from[e[0]].append(e)
        edges_from[e[1]].append( (e[1], e[0], e[2], e[4], e[3], e[5] ) )

    modif = 1
    total_possible_edges = (len(edges_from)**2 - len(edges_from))//2
    it = 0
    while modif > 0 :
        modif = 0
        initc = init.copy()   # to avoid RuntimeError: dictionary changed size during iteration
        s = 0
        for i,d in initc.items() :
            if allow(i):
                fromi2 = edges_from[i[1]]
                s += d
                for e in fromi2 :
                    if i[0] == e[1] : # on fait attention à ne pas ajouter de boucle sur le même noeud
                        continue
                    new_e = i[0], e[1]
                    new_d = d + e[-1]
                    if new_e not in init or init[new_e] > new_d :
                        init[new_e] = new_d
                        modif += 1
        fLOG("iteration ", it, " modif ", modif, " # ", len(initc)//2,"/",total_possible_edges,"=",
                "%1.2f" %(len(initc)*50 / total_possible_edges) + "%")
        it += 1
        if it > iter :
            break

    return init

def kruskall(edges, extension, fLOG = None):
    """
    Applique l'algorithme de Kruskal (ou ressemblant) pour choisir les arcs à ajouter.

    @param      edges       listes des arcs
    @param      extension   résultat de l'algorithme de Bellman
    @param      fLOG        logging function
    @return                 added_edges
    """

    original = { (e[0],e[1]) : e[-1] for e in edges }
    original.update ( { (e[1],e[0]) : e[-1] for e in edges } )
    additions = { k:v for k,v in extension.items() if k not in original }
    additions.update( { (k[1],k[0]):v for k,v in additions.items() } )

    degre = { }
    for k,v in original.items() :  # original est symétrique
        degre[k[0]] = degre.get(k[0],0) + 1

    tri = [ (v,k) for k,v in additions.items() if degre[k[0]] %2 == 1 and degre[k[1]] %2 == 1  ]
    tri.extend( [ (v,k) for k,v in original.items() if degre[k[0]] %2 == 1 and degre[k[1]] %2 == 1  ] )
    tri.sort()

    impairs = sum ( v%2 for k,v in degre.items()  )

    added_edges = []

    if fLOG is not None:
        fLOG("nb odd degrees",impairs, "nb added edges",len(added_edges))

    if impairs > 2 :
        for v,a in tri :
            if degre[a[0]] % 2 == 1 and degre[a[1]] % 2 == 1 :
                # il faut refaire le test car degre peut changer à chaque itération
                degre[a[0]] += 1
                degre[a[1]] += 1
                added_edges.append ( a + (v,) )
                impairs -= 2
                if impairs <= 0 :
                    break

    if fLOG is not None:
        fLOG("nb odd degrees",impairs, "nb added edges",len(added_edges))
        fLOG("added length ", sum( v for a,b,v in added_edges ))
        fLOG("initial length", sum( e[-1] for e in edges ))
        t = sorted([ _ for _,v in degre.items() if v%2 == 1 ])
        if len(t) > 10 : t = t[:10]
        fLOG("degrees", t)
    return added_edges

def eulerien_extension(edges, iter = 20, fLOG = print, alpha = 0.5, distance = distance_haversine):
    """
    Contruit une extension eulérienne d'un graphe.

    @param      edges       liste des arcs
    @param      iter        nombre d'itérations pour la fonction @see fn bellman
    @param      fLOG        logging function
    @param      alpha       coefficient multiplicatif de ``max_segment``
    @param      distance    la distance de Haversine est beaucoup trop longue sur de grands graphes, on peut la changer
    @return                 added edges
    """
    max_segment = max ( e[-1] for e in edges )
    fLOG("possible_edges")
    possibles   = possible_edges(edges, max_segment * alpha, fLOG = fLOG, distance=distance)
    fLOG("next")
    init        = bellman(edges, fLOG = fLOG, allow = lambda e : e in possibles)
    added       = kruskall(edges, init, fLOG = fLOG)
    d           = graph_degree(edges + added)
    allow       = [ k for k,v in d.items() if v%2 == 1 ]
    totali      = 0
    while len(allow) > 0 :
        fLOG("------- nb odd vertices", len(allow), "iteration",totali)
        allowset = set(allow)
        init     = bellman(edges, fLOG = fLOG, iter = iter,
                        allow = lambda e : e in possibles or e[0] in allowset or e[1] in allowset,
                        init = init)
        added    = kruskall(edges, init, fLOG = fLOG)
        d        = graph_degree(edges + added)
        allow    = [ k for k,v in d.items() if v%2 == 1 ]
        totali  += 1
        if totali > 20 :
            # tant pis, ça ne marche pas
            break

    return added

def connected_components(edges):
    """
    computes the connected components

    @param      edges       edges
    @return                 dictionary { vertex : id of connected components }
    """
    res = { }
    for k in edges :
        for _ in k[:2]:
            if _ not in res :
                res[_] = _
    modif = 1
    while modif > 0 :
        modif = 0
        for k in edges :
            a,b = k[:2]
            r,s = res[a],res[b]
            if r != s :
                m = min(res[a],res[b])
                res[a] = res[b] = m
                modif += 1

    return res

def euler_path(edges, added_edges):
    """
    Compute an eulerian path. We assume every vertex has an even degree.

    @param      edges           initial edges
    @param      added_edges     added edges
    @return                     path, list of (vertex,edge)
    """
    alledges = { }
    edges_from = { }
    somme = 0
    for e in edges:
        k = e[:2]
        v = e[-1]
        alledges[k] = ["street"] + list(k + (v,))
        a,b = k
        alledges[b,a] = alledges[a,b]
        if a not in edges_from:edges_from[a] =[]
        if b not in edges_from:edges_from[b] =[]
        edges_from[a].append ( alledges[a,b] )
        edges_from[b].append ( alledges[a,b] )
        somme += v

    for e in added_edges:  # il ne faut pas enlever les doublons
        k = e[:2]
        v = e[-1]
        a,b = k
        alledges[k] = ["jump"] + list(k + (v,))
        alledges[b,a] = alledges[a,b]
        if a not in edges_from:edges_from[a] =[]
        if b not in edges_from:edges_from[b] =[]
        edges_from[a].append ( alledges[a,b] )
        edges_from[b].append ( alledges[a,b] )
        somme += v

    degre = { }
    for a,v in edges_from.items():
        t = len(v)
        degre[t] = degre.get(t,0)+1

    two = [ a for a,v in edges_from.items() if len(v) == 2 ]
    odd = [ a for a,v in edges_from.items() if len(v) %2 == 1 ]
    if len(odd) > 0 :
        raise ValueError("some vertices have an odd degree")
    begin = two [0]

    # checking
    for v,le in edges_from.items():
        for e in le :
            to = e[1] if v != e[1] else e[2]
            if to not in edges_from :
                raise Exception("unable to find vertex {0} for edge {0},{1}".format(to,v))
            if to == v :
                raise Exception("circular edge {0}".format(to))

    # loop
    path = _explore_path(edges_from, begin)
    for p in path:
        if len(p) == 0 :
            stop
    while len(edges_from) > 0 :
        start = None
        for i,p in enumerate(path):
            if p[0] in edges_from :
                start = i,p
                break
        sub = _explore_path(edges_from, start[1][0])
        i = start[0]
        path [i:i+1] = sub + path[i:i+1]
    return path

def _delete_edge(edges_from, n, to):
    """
    removes an edge from the graph

    @param      edges_from      structure which contains the edges (will be modified)
    @param      n               first vertex
    @param      to              second vertex
    @return                     the edge
    """
    l = edges_from[to]
    f = None
    for i,e in enumerate(l) :
        if (e[1] == to and e[2] == n) or (e[2] == to and e[1] == n) :
            f = i
            break

    assert f is not None
    del l[f]
    if len(l) == 0 :  del edges_from[to]

    l = edges_from[n]
    f = None
    for i,e in enumerate(l) :
        if (e[1] == to and e[2] == n) or (e[2] == to and e[1] == n) :
            f = i
            break

    assert f is not None
    keep = l[f]
    del l[f]
    if len(l) == 0 :  del edges_from[n]

    return keep

def _explore_path(edges_from, begin) :
    """
    explore an eulerian path, remove used edges from edges_from

    @param      edges_from      structure which contains the edges (will be modified)
    @param      begin           first vertex to use
    @return                     path
    """
    path = [ (begin, None) ]
    stay = True
    while stay and len(edges_from) > 0 :

        n = path [-1][0]
        if n not in edges_from:
            # fin
            break
        l = edges_from[n]

        if len(l) == 1 :
            h = 0
            e = l[h]
            to = e[1] if n != e[1] else e[2]
        else :
            to = None
            nb = 100
            while to is None or to == begin :
                h = random.randint(0,len(l)-1) if len(l) > 1 else 0
                e = l[h]
                to = e[1] if n != e[1] else e[2]
                nb -= 1
                if nb < 0 :
                    raise Exception("algorithm issue {0}".format(len(path)))

        if len( edges_from [to] ) == 1 :
            if begin != to :
                raise Exception("wrong algorithm")
            else :
                stay = False

        keep = _delete_edge(edges_from, n, to)
        path.append( ( to, keep) )

    return path[1:]