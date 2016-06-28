# coding: latin-1
import sys
import copy
sys.path.append ("../donnees_personnalisees")
from tutoriel_99 import *
import numpy
import math
import struct
import urllib, os

nom_prenom = "llotteMhlo Cevai"
i = 3 # i=3 mais on fait référence au 4ieme caractère
valeur = ord ( nom_prenom [i] )



def somme_caractere (nom_prenom) :
    s = 0
    for c in nom_prenom : s += ord (c)
    return s
    
print somme_caractere (nom_prenom), somme_caractere (nom_prenom) % 200

class MonGraphe :
    def __init__ (self, num, valeur) :
        self.valeur = valeur
        self.num    = num
        self.arcs   = [] # liste d’éléments MonGraphe
        
def ConstruireMonGraphe (noeuds, arcs) :
    nodes = {}
    for i,v in noeuds.iteritems () :
        nodes [i] = MonGraphe (i,v)
    for k in arcs :
        i,j = k
        nodes[i].arcs.append (nodes [j])
        nodes[j].arcs.append (nodes [i])
    return nodes[0]

def NombreArcs (racine) :
    edges = {}
    pile = [ ]
    done = { }
    pile.append (racine)
    while len(pile) > 0 :
        r               = pile.pop ()
        if r.num in done : continue
        done [r.num]    = None
        for node in r.arcs :
            if node.num in done : continue
            edges [ r.num, node.num ] = None
            pile.append (node)            
            
    final = { }
    for k in arcs :
        i,j = k
        if i != j and (j,i) not in final : final [i,j] = None
            
    return len(final)
    
def NombreArcsRecursive (r, edges = {}, done = { }) :
    if r.num in done : return 0
    done [ r.num ] = None
    for node in r.arcs :
        edges [ r.num, node.num ] = None
        NombreArcsRecursive (node, edges, done)
        
    final = { }
    for k in arcs :
        i,j = k
        if i != j and (j,i) not in final : final [i,j] = None
        
    return len(final)
    
def nbComposanteConnexe (edges, maxid) :
    mini = { }
    modif = 1
    while modif > 0 :
        modif = 0
        for arc in edges :
            i,j = arc
            if i not in mini : 
                mini [i] = min (i,j)
                modif = 1
            if j not in mini : 
                mini [j] = min(i,j)
                modif = 1
            m = min (mini[i],mini[j])
            if m != mini [i] :
                mini [i] = m
                modif = 1
            if m != mini [j] :
                mini [j] = mini[i]
                modif = 1
    temp = { }
    for i,j in mini.iteritems () :
        temp [j] = j
        
    add = 0
    if maxid != -1 :
        count = { }
        for k in edges :
            i,j = k
            count [i] = count.get (i,0) + 1
            count [j] = count.get (j,0) + 1
        for i in xrange (0,maxid) :
            if count.get (i, 0) == 0 : add += 1
    return len (temp) + add
    
def Laplacien (edges) :
    mat = { }
    for k in edges :
        i,j = k
        if i != j :
            mat [i,j] = -1
            mat [j,i] = -1
            if (i,i) not in mat : mat [i,i] = 0
            if (j,j) not in mat : mat [j,j] = 0
            mat [i,i] += 1
            mat [j,j] += 1
    return mat
    
def TransformationEnMatrice (d) :
    keys = d.keys ()
    maxid = max ( max ( [ _[0] for _ in keys ] ), max ( [ _[1] for _ in keys ] ) )
    maxid += 1
    mat = [ [ 0 for _ in xrange (0,maxid) ] for __ in xrange (0,maxid) ]
    for k,v in d.iteritems () :
        i,j = k
        mat [i][j] = v
    return numpy.array (mat)
    
def Eigen (mat, sort = True) :
    l, v = numpy.linalg.eig(mat)
    
    if sort :
        li = list (l)
        li = [ (_,i) for i,_ in enumerate (li) ]
        li.sort ()
        
        pos = [ _[1] for _ in li ]
        l   = numpy.array ( [ _[0] for _ in li ] )
            
        mat = copy.copy (v)
        for i in xrange (0, len (pos)) :
            mat [ :,i] = v [ :,pos[i] ]
        
        return l,mat
    else :
        return l,v
    
def DrawGraph (noeuds, arcs, cl, cl2 = None, nopause = False) :
    sys.path.append (r"D:\Dupre\_data\program\hal\hal_Python")
    import hal_python as HAL
    HAL.Begin ()
    cl = [ 1 if c > 0 else -1 for c in cl ]
    if cl2 == None :
        n = [ (i,"*", "ellipse", "red" if c == 1 else "blue") for i,c in enumerate (cl) ]
    else :
        color = { (-1,-1) : "blue", (1,1):"red", (-1,1):"green", (1,-1):"yellow" }
        cl2 = [ 1 if c > 0 else -1 for c in cl2 ]
        z   = zip (cl,cl2)
        n = [ (i,"*", "ellipse", color[c]) for i,c in enumerate (z) ]
    edges = arcs.keys ()    
    image = HAL.ArcGraphDraw (n, edges)
    image.Display ()
    if not nopause : HAL.Pause ()
        
def CouperLesArcs (noeuds, arcs, cl):
    cl = [ 1 if c > 0 else -1 for c in cl ]
    count = { }
    newarcs = {}
    for k in arcs :
        i,j = k
        if i > j : i,j = j,i
        if cl [i] != cl [j] : count [k] = None
        else : newarcs [k] = arcs [k]
    lapl    = Laplacien (newarcs)
    mat     = TransformationEnMatrice (lapl)
    l,vect  = Eigen (mat)
    return len (count), nbComposanteConnexe (newarcs, len (noeuds)),list (l[0:4])
    
def distance (p1, p2) :
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.exp (- (dx**2 + dy**2) )

def CreateProximityMatrix (points) :
    n = len (points)
    mat = [ [ 0.0 for i in xrange (0,n)] for j in xrange (0,n) ]
    for i in xrange (0, n) :
        for j in xrange (0, n) :
            if i != j :
                mat [i][j] = - distance (points [i], points [j])
    for i in xrange (0, n) :
        mat [i][i] = -sum (mat [i])
    return mat
    
def DrawXY (points, cl, nopause = False) :
    import hal_python as HAL
    HAL.Begin ()
    cl = [ 1 if c > 0 else -1 for c in cl ]
    p1,p2 = [],[]
    for p,c in zip (points, cl) :
        if c == 1 : p1.append (p)
        else : p2.append (p)
    
    pl = HAL.PlotGraph ( [  ["p1", p1, "point"],["p2", p2, "point"] ] )
    pl.Display ()
    if not nopause : HAL.Pause ()    

racine = ConstruireMonGraphe (noeuds, arcs)
nb     = NombreArcs (racine)
nb2    = NombreArcsRecursive (racine)
print nb, nb2, len (arcs)
print nbComposanteConnexe (arcs, len (noeuds))
lapl   = Laplacien (arcs)
mat    = TransformationEnMatrice (lapl)
l,vect    = Eigen (mat)
print "*"
print l
print vect [:,1]
print "*"
for i in xrange (1, len (noeuds)) :
    cl = vect [:,i]
    print i,CouperLesArcs (noeuds, arcs, cl),len(arcs), l[i]

if True :
    cl = vect [:,1]
    DrawGraph (noeuds, arcs, cl, nopause = True)
    cl = vect [:,4]
    DrawGraph (noeuds, arcs, cl, nopause = True)
    if False :
        cl = vect [:,7]
        DrawGraph (noeuds, arcs, cl, nopause = True)
        cl = vect [:,49]
        DrawGraph (noeuds, arcs, cl, nopause = True)
        cl = vect [:,7]
        cl2 = vect [:,4]
        DrawGraph (noeuds, arcs, cl, cl2, nopause = False)
        
print "***********"
print len(points), points  
lapl    = CreateProximityMatrix (points)
mat     = numpy.array (lapl)
l,vect  = Eigen (mat)
print l
cl = vect [:,1]
print cl
if True :
    DrawXY (points, cl)


