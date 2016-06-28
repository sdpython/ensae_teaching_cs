# coding: cp1252
"""décomposition de la base d'image MNIST"""

import os
import struct
import PIL  # ligne à supprimer si on n'a pas besoin des images
import PIL.Image as PIM  # ligne à supprimer si on n'a pas besoin des images

def transcription_entier (str) :
    """convertit un entier lu en format binaire en entier"""
    t = struct.unpack ("BBBB", str)
    i = t [3] + t [2] * 256 + t [1] * 256 * 256 + t [0] * 256 * 256 * 256
    return i
    
def lire_image (fim, nl, nc) :
    """lit une image dans le fichier fim, cette image a nl lignes et nc colonnes,
    retourne l'image sous la forme d'un t-uple"""
    nb  = nl * nc
    str = fim.read (nb)
    t   = struct.unpack ("B" * nb, str)
    return t
    
def lire_image (fim, nl, nc) :
    """lit une image dans le fichier fim, cette image a nl lignes et nc colonnes,
    retourne l'image sous la forme d'un t-uple"""
    nb  = nl * nc
    str = fim.read (nb)
    t   = struct.unpack ("B" * nb, str)
    return t

def lire_label (fla) :
    """lit un label (un chiffre) dans le fichier fla, retourne un entier"""
    str = fla.read (1)
    t   = struct.unpack ("B", str)
    return t [0]

def binarisation (image, binar) :
    """binarisation d'une image"""
    
    res = []
    for i in image :
        if i < 255 - binar : res.append (255)
        else : res.append (0)
    return res


def write_image_matlab (fmat, image) :
    """écrit une image au format matlab, chaque nombre indique 
    la position du prochain pixel noir,
    la suite est aussi longue qu'il y a de pixels dans l'image
    et se termine par une suite de 0 qui indique qu'il n'y a plus de pixels noirs"""
    nb = 0
    for i in xrange (0, len(image)) :
        if image [i] == 0 :
            fmat.write ("," + str (i+1))
            nb += 1
    for i in xrange (0, len (image) - nb) :
        fmat.write (",0")

def decompose_mnist (file_image, file_label, file_matlab, binar, \
                        nbcl = -1, dir_image1 = None, dir_image2 = None) :
    """décompose la base MNIST en un format utilisable sous MATLAB,
    commence par [, termine par ], chaque ligne est composée comme suit :
    premier nombre = classe, voir fonction write_image_matlab ;,
    nbcl est le nombre d'images à extraire par classe, 
    si nbcl == -1, traite toute la base,
    binar est le seuil de binarisation, voir fonction binarisation,
    si dir_image1 != None, les images des nombres sont écrites,
    si dir_image2 != None, on continue d'explorer le fichier des images 
    mais les images des nombres sont écrites dans le répertoire dir_image2"""
    
    fim = open (file_image, "rb")
    fla = open (file_label, "rb")
    
    s           = fla.read (4) # , (Hal_byte*) &umagic_an) ;
    magic_an    = transcription_entier (s)
    s           = fla.read (4) # , (Hal_byte*) &unb_an) ;
    nb_an       = transcription_entier (s)
    
    s           = fim.read (4) # , (Hal_byte*) &umagic_im) ;
    magic_im    = transcription_entier (s)
    s           = fim.read (4) # , (Hal_byte*) &unb_im) ;
    nb_im       = transcription_entier (s)
    s           = fim.read (4) #, (Hal_byte*) &unl_im) ;
    nl_im       = transcription_entier (s)
    s           = fim.read (4) #, (Hal_byte*) &unc_im) ;
    nc_im       = transcription_entier (s)
    
    if nbcl == -1 : nbcl = nb_im
    
    print "nombre de labels ", nb_an
    print "nombre magique label , vérification (2049) ", magic_an
    print "nombre d'images ", nb_im
    print "nombre magique image, vérification (2051) ", magic_im
    print "nombre de lignes ", nl_im
    print "nombre de colonnes ", nc_im

    if file_matlab != None :
        fmat = open (file_matlab, "wt")
        fmat.write ("[")
        
    label_count = { }
    
    nb      = 0
    cent    = int (nb_im / 100)
    while nb < nb_im :
        
        if nb % cent == 0 : print "avancement ", nb / cent, " %"
        nb += 1
        
        image = lire_image (fim, nl_im, nc_im)
        label = lire_label (fla)
        
        image = binarisation (image, binar)
        
        if not label_count.has_key (label) : label_count [label] = 0
        if 0 <= label_count [label] < nbcl : 
            dir_image = dir_image1
        elif nbcl <= label_count [label] < nbcl * 2 : 
            dir_image = dir_image2
        else : 
            dir_image = None
            continue 
            

        if file_matlab != None :
            fmat.write (str (label))
            write_image_matlab (fmat, image)
            fmat.write (";\n")
        
        if dir_image != None :
            nom     = "image_%d_%5d" % (label, label_count [label] % nbcl)
            nom     = dir_image + "\\" + nom + ".tif"
            surf    = PIM.new ("RGB", (nc_im, nl_im) )
            for i in xrange (0, len (image)) :
                x,y = i % nc_im, i // nc_im
                c   = image [i]
                surf.putpixel ((x,y), (c,c,c))
                
            surf.save (nom)
            
        label_count [label] += 1
    
    if file_matlab != None :
        fmat.write ("]")
        fmat.close ()
        
    fim.close ()
    fla.close ()
    
    key = label_count.keys ()
    key.sort ()
    for i in key :
        print "label ", i , " \t : ", label_count [i]
    
    return label_count


if __name__ == "__main__" : 
        file_image  = "C:\\Downloads\\data_image\\mnist\\t10k-images.idx3-ubyte"
        file_label  = "C:\\Downloads\\data_image\\mnist\\t10k-labels.idx1-ubyte"
        file_matlab = "c:\\temp\\mnist2\\matlab.txt"
        dir_image   = None # "c:\\temp\\mnist2"
        nb          = 20
        binar       = 190
        
        decompose_mnist (file_image, file_label, file_matlab, \
                        binar, nb, dir_image1, dir_image2)