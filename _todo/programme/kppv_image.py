# coding: cp1252
import os
import os.path
import mnist
import string
import PIL
import PIL.Image
import html_file as html
import psyco
import random
import kppv
import time

# définit une classe héritant de kppv.nuage_points qui surcharge les 
# fonctions distance et label
class nuage_point_distance_label (kppv.nuage_points) :
    """hérite de kppv.nuage_point et surcharge les méthodes :
            - distance
            - label
    """

    def distance (self, obj1, obj2) :
        """surcharge de la fonction distance, comme les images sont toutes
        de dimensions identiques, on peut compter les pixels de couleurs différentes,
        le résultat est la distance entre deux images"""
        if len (obj1) != len (obj2) :
            print "erreur, len (obj1) != len (obj2)"
        d = 0
        for i in xrange (2, len (obj1)) :
            if obj1 [i] != obj2 [i] : d += 1
        return d
                
    def label (self, obj) :
        """retourne le label d'un objet"""
        return obj [0]
    
        
class nuage_image (object) :
    """nuage de points, chaque élément est une image, 
    les images sont en noir et blanc, liste de 0 ou 1"""
    
    def __init__ (self, nuage_ppv, rep, nb, extension = "tif") :
        """initialise le nuage d'images avec un répertoire
        qui est l'emplacement des images pour ce nuage, 
        le nom des images contient une chaîne de caractères suivi 
        d'un label séparés par un blanc soulignés, 
        extension est le type de images à charger,
        on ne considère que les nb premières images,
        nuage est une instance de la classe nuage_point ou nuage_point_laesa"""
        
        def binarise (p) :
            if p [0] == 0 : return 1
            else : return 0
        
        self.nb     = 0
        self.nuage  = []
        
        file = os.listdir (rep)
        nb   = min (nb, len (file))
        step = nb / 10
        n    = 0 
        for f in file :
            if n >= nb : break
            if n % step == 0 : print "nuage_image, avancement ", n * 100 / nb, "%"
            n += 1
            ext = os.path.splitext (f)
            ext = ext [len (ext) - 1].lower ()
            ext = ext [1 : len (ext)]
            if ext != "tif" : continue 
            s       = f.split ("_")
            label   = s [1]
            im      = PIL.Image.open (rep + "\\" + f)
            size    = im.size
            data    = [ binarise (im.getpixel ((x,y))) for y in xrange (0, size [1]) \
                                                        for x in xrange (0, size [0]) ]
            data.insert (0, size)
            data.insert (0, label)
            self.nuage.append ( tuple (data))
            
        self.ppv          = nuage_ppv 
        self.ppv.nb       = self.nb
        self.ppv.nuage    = self.nuage

        
    def image (self, obj) :
        """reconstruit une image à partir d'un élément"""
        size    = obj [1]
        im      = PIL.Image.new ("RGB", size)
        nb      = len (obj) - 2
        for i in xrange (0, nb) :
            if obj [i] == 0 : im.putpixel ( (i % size [0], i // size [1]), (255,255,255))
            else : im.putpixel ((i % size [0], i // size [1]), (0,0,0))
        return im
    
    def html_couple (self, fichier, l, zoom = None) :
        """écrit un fichier html contenant toutes les images mal classées, 
        à partir de la liste erreur construite par la méthode nuage_points.ppv_nuage"""
        
        # nombre de colonnes maximales
        maxc = 0
        for x in l : maxc = max (maxc, len (x))
     
        f = html.html_file (fichier)
        f.open ()
        f.table_begin (maxc*2+1)
        
        f.text ("indice")
        f.table_next ()
        f.text ("label")
        f.table_next ()
        f.text ("à classer")
        f.table_next ()
        for n in xrange (1, maxc) :
            f.text ("label")
            f.table_next ()
            f.text ("voisin " + str (n))
            f.table_next ()
        f.table_next_line ()

        n = 0
        for x in l :
            f.text (str (n))
            f.table_next ()
            n += 1
            for el in x :
                im = self.image (el)
                f.text (self.ppv.label (el))
                f.table_next ()
                f.add_image (im, zoom = zoom)
                f.table_next ()
            f.table_next_line ()
            
        f.table_end ()
        f.close ()
        
    def ppv_nuage (self, nuage, bienclasse = None, erreur = None) :
        """appelle self.nuage.ppv_nuage"""
        return self.ppv.ppv_nuage (nuage, bienclasse, erreur)
        
    def __len__ (self) :
        """retourne len (self.nuage)"""
        return len (self.ppv)
                
    def __iter__(self) :
        """retourne iter (self.nuage)"""
        return iter (self.ppv)
        
        
        
if __name__ == "__main__" :

    psyco.full ()
    
    rep_app     = "c:\\temp\\mnist\\app"
    rep_test    = "c:\\temp\\mnist\\test"
    nb_app      = 400
    nb_test     = 400
    html_file1   = "c:\\temp\\mnist\\bienclasse.html"
    html_file2   = "c:\\temp\\mnist\\erreur.html"
    
    # si les images n'existent pas
    if not os.path.exists (rep_app) or not os.path.exists (rep_test) :
        file_image  = "C:\\Downloads\\data_image\\mnist\\t10k-images.idx3-ubyte"
        file_label  = "C:\\Downloads\\data_image\\mnist\\t10k-labels.idx1-ubyte"
        os.makedirs (rep_app)
        os.makedirs (rep_test)
        binar = 220
        nbcl  = 40
        mnist.decompose_mnist (file_image, file_label, None, binar, nbcl, \
                                rep_app, rep_test)
        
    ppv1 = nuage_point_distance_label ()
    ppv2 = nuage_point_distance_label ()

    print "construction du nuage d'apprentissage"
    nuage_app = nuage_image (ppv1, rep_app, nb_app)
    print "nombre de points : ", len (nuage_app)
    
    print "construction du nuage de test"
    nuage_test = nuage_image (ppv2, rep_test, nb_test)
    print "nombre de points : ", len (nuage_test)
    
    print "résultat de la classification"
    erreur      = []
    bienclasse  = []
    temps1      = time.clock ()
    good,bad = nuage_app.ppv_nuage (nuage_test, bienclasse, erreur)
    temps2      = time.clock ()
    print "---------------------------------------------------------------------------"
    print "temps de traitement en secondes ", temps2 - temps1
    print "good, bad = ", good, bad
    print "taux de classification  : ", float (good) / (good + bad)
    print "écriture du fichier ", html_file1
    nuage_app.html_couple (html_file1, bienclasse,   zoom = 4)
    print "écriture du fichier ", html_file2
    nuage_app.html_couple (html_file2, erreur,       zoom = 4)
    

