# coding:latin-1
import urllib
import os
import os.path
# coding:latin-1


def drawGraph(edges, script, image):
    """
    dessine un graph en utilisant Graphviz (http://www.graphviz.org/
    edges = [ (1,2), (3,4), (1,3), ... ]  , liste d'arcs
    image = bom d'image (format png)
    """
    import os
    import urllib
    import struct
    files = ["_graphviz_draw.exe"]
    if not os.path.exists(files[-1]):
        # on télécharge les fichiers nécessaires d'abord
        for f in files:
            print "téléchargement de ", f
            url = "http://www.xavierdupre.fr/enseignement/tutoriel_python/graphviz/" + f
            u = urllib.urlopen(url, "rb")
            all = u.read()
            if "404 Not Found" in all:
                raise Exception("fichier introuvable")
            u.close()
            u = open(f, "wb")
            u.write(struct.pack("c" * len(all), *all))
            u.close()
    if not os.path.exists(files[-1]):
        raise Exception("mauvais téléchargement")

    if script == None:
        li = ["digraph{"]
        for i, j in edges:
            li.append("%d -> %d ;" % (i, j))
        li.append(";")
        f = open("graph.gv", "w")
        f.write("\n".join(li))
        f.close()
    else:
        f = open("graph.gv", "w")
        f.write(script)
        f.close()

    cmd = "%s . graph.gv %s png neato" % (files[-1], image)
    os.system(cmd)

#drawGraph ([(1,2),(3,4), (1,3)], "image.png")


def charge_donnees(file="matrix_distance_7398.txt"):
    if os.path.exists(file):
        # si le fichier existe (il a déjà été téléchargé une fois)
        f = open(file, "r")
        text = f.read()
        f.close()
    else:
        # si le fichier n’existe pas
        link = "http://www.xavierdupre.fr/enseignement/td_python/" + \
            "python_td_minute/data/court_chemin/" + file
        url = urllib.urlopen(link)
        text = url.read()
# on enregistre les données pour éviter de les télécharger une seconde fois
        f = open(file, "w")
        f.write(text)
        f.close()
    lines = text.split("\n")
    lines = [l.split("\t") for l in lines if len(l) > 1]
    return lines


def conversion_en_dictionnaire(lines):
    res = {}
    for a, b, c in lines:
        c = int(c)

        res[a, b] = c
        res[b, a] = c
    return res


def graphviz_script(mat_dict):
    script = ["graph {"]
    vertex = {}
    villes = [_[0] for _ in mat_dict.keys()]
    for v in villes:
        if v not in vertex:
            vertex[v] = len(vertex)
    for k, v in vertex.iteritems():
        script.append("%d [label=\"%s\"];" % (v, k))
    for k, v in mat_dict.iteritems():
        i1 = vertex[k[0]]
        i2 = vertex[k[1]]
        if i1 < i2 and v < 15000:
            # on coupe des arcs car le tracé est trop long sinon
            script.append("%d -- %d [label=\"%skm\"];" % (i1, i2, v / 1000))
    script.append("}")
    return "\n".join(script)
if __name__ == "__main__":
    matrice_line = charge_donnees()
    mat = conversion_en_dictionnaire(matrice_line)
    drawGraph([], graphviz_script(mat), "im.png")
