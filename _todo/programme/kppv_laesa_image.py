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
import kppv_laesa
import time
import kppv_image

# définit une classe héritant de kppv.nuage_points qui surcharge les 
# fonctions distance et label
class nuage_point_leasa_distance_label (kppv_laesa.nuage_point_laesa) :
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
    
        
class nuage_image_leasa (kppv_image.nuage_image) :
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
                
        kppv_image.nuage_image.__init__(self, nuage_ppv, rep, nb, extension)
        self.ppv.selection_pivots (20)

        
        
        
        
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
        
    ppv1 = nuage_point_leasa_distance_label ()
    ppv2 = nuage_point_leasa_distance_label ()

    print "construction du nuage d'apprentissage"
    nuage_app = nuage_image_leasa (ppv1, rep_app, nb_app)
    print "nombre de points : ", len (nuage_app)
    
    print "construction du nuage de test"
    nuage_test = nuage_image_leasa (ppv2, rep_test, nb_test)
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
    

