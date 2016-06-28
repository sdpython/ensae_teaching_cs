#coding:latin-1
import urllib, os, os.path
from importme import *
GV = import_module ("use_graphivz")
webhelper = import_module ("webhelper")
drawGraph = GV.drawGraphScript
graphviz_script = GV.graphviz_script

# coding:latin-1

def charge_donnees (file = "matrix_distance_7398.txt") :
    webhelper.import_module_or_file_from_web_site(file)
    f = open (file, "r")
    text = f.read ()
    f.close ()
    lines = text.split ("\n")
    lines = [ l.split("\t") for l in lines if len(l) > 1 ]
    return lines
    
def conversion_en_dictionnaire (lines) :
    res = { }
    for a,b,c in lines :
        c = int (c)
        res [a,b] = c
        res [b,a] = c
    return res
    
if __name__ == "__main__" :
    matrice_line = charge_donnees ()
    mat = conversion_en_dictionnaire (matrice_line)
    script = graphviz_script (mat)
    drawGraph([], script , "im.png")
