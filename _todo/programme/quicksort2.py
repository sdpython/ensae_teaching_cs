# coding: latin-1
import string
import pydot
import quicksort

class NoeudTri2 (quicksort.NoeudTri):

    def chaine_graphe (self):
        # le principe est le même que pour la méthode __str__
        # excepté que le format est différent
        g = str (id (self)) + ' [label="' + self.mot \
                            + '",style=filled,shape=record,fontsize=60]\n'
        if "avant" in self.__dict__:
            h  = self.avant.chaine_graphe ()
            g += h + str (id (self)) + " -> " + str (id (self.avant)) \
                   + ' [label="<",fontsize=60]' + '\n'
        if "apres" in self.__dict__:
            h  = self.apres.chaine_graphe ()
            g += h + str (id (self)) + " -> " + str (id (self.apres)) \
                   + ' [label=">",fontsize=60]' + "\n"
        return g

    #def nouveau_noeud (self, s) : return NoeudTri2 (s)
        
    def image (self, file, im) :
        # on crée un graphe : on récupère le code du graphe
        graph = self.chaine_graphe ()
        # auquel on ajoute un début et une fin
        graph = "digraph GA {\n" + graph + "}\n"
        
        # puis on l'écrit dans le fichier file
        g = open (file, "w")
        g.write (graph)
        g.close ()

        # enfin, on convertit ce fichier en image
        dot = pydot.graph_from_dot_file (file)
        dot.write_png (im, prog="dot")

def construit_arbre () :
    # même code que dans le programme précédent
    # mais inclus dans une fonction
    l = ["un", "deux", "unite", "dizaine", "exception", "dire", \
         "programme", "abc", "xyz", "opera", "quel"]
    racine = None
    for mot in l :
        if racine == None : racine = NoeudTri2 (mot)
        else : racine.insere (mot)
    return racine
    
racine = construit_arbre ()
print racine
racine.image ("graph.txt", "graph.png")