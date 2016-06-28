# coding:latin-1
def import_Graphviz () :
    import os, urllib,struct
    files = [ "_graphviz_draw.exe"]
    if not os.path.exists (files[-1]) :
        # on télécharge les fichiers nécessaires d'abord
        for f in files :
            print "téléchargement de ", f
            url = "http://www.xavierdupre.fr/enseignement/tutoriel_python/graphviz/" + f
            u = urllib.urlopen (url, "rb")
            all = u.read ()
            if "404 Not Found" in all :
                raise Exception ("fichier introuvable")
            u.close ()
            u = open (f, "wb")
            u.write ( struct.pack ("c"*len(all), *all))
            u.close()
    if not os.path.exists (files[-1]) :
        raise Exception ("mauvais téléchargement")
    return files
    
def drawDiGraph (text, image) :
    f = open ("graph.gv", "w")
    f.write ( text )
    f.close ()
    
    files = import_Graphviz ()
    cmd = "%s . graph.gv %s png neato" % (files[-1], image)
    import os
    os.system (cmd)
        
def drawGraph (edges, image) :
    """
    dessine un graph en utilisant Graphviz (http://www.graphviz.org/
    edges = [ (1,2), (3,4), (1,3), ... ]  , liste d'arcs
    image = bom d'image (format png)
    """
    li = [ "digraph{" ]
    for i,j in edges :
        li.append ( "%d -> %d ;" % (i,j) )
    li.append ("};")
    text = "\n".join(li)
    drawDiGraph(text, image)
    
def drawGraphEdgesVertices (vertices, edges, image) :
    """
    dessine un graph en utilisant Graphviz (http://www.graphviz.org/
    edges    = [ (1,2, label, couleur), (3,4), (1,3), ... ]  , liste d'arcs
    vertices = [ (1, label, couleur), (2), ... ]  , liste de noeuds
    image = bom d'image (format png)
    """
    memovertex = { }
    for v in vertices :
        if len(v) == 1 : memovertex[v[0]] = None
        else : memovertex[v[0]] = v[1:]
    for edge in edges :
        i,j = edge[:2]
        if i not in memovertex : memovertex[i] = None
        if j not in memovertex : memovertex[j] = None
    
    li = [ "digraph{" ]
    for k,v in memovertex.iteritems() :
        if v == None : li.append("%s ;" % k)
        elif len(v) == 1 : li.append ("\"%s\" [label=\"%s\"];" % (k, v[0]))
        elif len(v) == 2 : li.append ("\"%s\" [label=\"%s\",fillcolor=%s,color=%s];" % (k, v[0], v[1], v[1]))
        else : raise Exception("unable to understand " + str(v))
            
    for edge in edges :
        i,j = edge[:2]
        if len (edge) == 2 : li.append ( "\"%s\" -> \"%s\" ;" % (i,j) )
        elif len (edge) == 3 : li.append ( "\"%s\" -> \"%s\" [label=\"%s\"];" % (i,j,edge[2]) )
        elif len (edge) == 4 : li.append ( "\"%s\" -> \"%s\" [label=\"%s\",color=%s];" % (i,j,edge[2],edge[3]) )
        else : raise Exception("unable to understand " + str(edge))
    li.append ("};")
    
    text = "\n".join(li)
    drawDiGraph(text, image)
    

if __name__ == "__main__" :
    drawGraph ([(1,2),(3,4), (1,3)], "image.png")
    drawGraphEdgesVertices ([(1,"eee","red")], 
                            [(1,2,"blue"),(3,4), (1,3)], "image2.png")
    