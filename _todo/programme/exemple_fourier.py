import pygame
import pygame.mixer
import pygame.sndarray
import FFT
import math
import numpy as Numeric
import string
import copy
import pylab
import numpy

pygame.mixer.init ()
pygame.init ()


fourier = None
indice = None

def get_sound ():
    """charge le son sound010.wav"""
    s = pygame.mixer.Sound ("sound010.wav")
    t = pygame.sndarray.array (s)
    return s
    
def play_sound(s):
    """joue un son"""
    s.play ()

def convert_array(t, s):
    """joue un son decrit dans un tableau a une dimension"""
    
    s = pygame.sndarray.array (s)
    for i in range (0, len (s)) :
        s [i]= t [i]
    #tt = Numeric.array ([ [x, x] for x in t] )
    #print tt [0:10]
    s = pygame.sndarray.make_sound (s)
    return s
    
def array_sound(s):
    """convertit un son en un tableau d'entiers"""
    a = pygame.sndarray.array(s)
    t = Numeric.array([i for i in xrange(0,len(a))])
    for i in xrange(0,len(a)): t [i] = a [i][0]
    return t

def dessine_son(mem,t,fourier,ind,a,b):
    """dessine une partie du son, limite la taille a 512"""
    m = len (mem)
    if m > 256 : m = 256
    x  = [ i for i in xrange (ind,ind+m) ] 
    y1 = [ mem[i] for i in xrange (ind,ind+m) ] 
    y2 = [ t[i] for i in xrange (ind,ind+m) ] 
    pylab.figure (1)
    p1 = pylab.plot (x,y1)
    p2 = pylab.plot (x,y2)
    pylab.title ("Fourier")
    pylab.xlabel ("frequence")
    pylab.ylabel ("amplitude")
    pylab.legend ( ("son", "son + filtre"))

    m = len (fourier)
    if m > 256 : m = 256
    #x  = [ i for i in xrange (0,m) ] 
    pylab.figure (2)
    x  = [ i for i in xrange (0,m) ] 
    y1 = [ abs(fourier[i]) for i in xrange (0,m) ] 
    y2 = []
    for i in x :
        if a <= i <= b : y2.append (450000.0)
        else : y2.append (0.0)
    p3 = pylab.plot (x,y1)
    p4 = pylab.plot (x,y2)
    pylab.legend ( ("fourrier", "filtre"))
    pylab.show()

def filtre_son_extrait(t,a,b):
    """calcul de la transformee de Fourier, application du filtre [a,b],
    recomposition du signal"""
    fft = FFT.fft (t)
    global fourier             
    if fourier == None and indice != None : fourier = copy.copy(fft)
    for i in xrange(0,len(t)):
        if a <= i <= b:
            pass
        else:
            fft [i] = complex(0,0)
    tt = FFT.inverse_fft(fft)
    for i in xrange(0,len(t)):
        t [i] = int(tt [i].real)
       

def filtre_son(t,a,b,div = 256):
    """filtre un son par tranche de div frequences, ne garde que les
    frequences comprises entre a et b"""
    global indice
    nb = len (t) / div
    for i in xrange (0,nb):
        if i == nb / 2 : indice = i * div
        ext = t [i * div : (i+1) * div]
        filtre_son_extrait (ext,a,b)

def essai():
    print "chargement du son"        
    s = get_sound ()
    print "duree : ", s.get_length (), " secondes"
    print "musique"
    play_sound (s)
    pygame.time.delay (6000)
    t = array_sound (s)
    mem = copy.copy(t)
    print "nombre de donnees ", len (t)
    print "duree d'une donnee ", s.get_length () * 1000 / len (t), "millisecondes"


    rep = ""
    if rep != "n" :
        #rep = string.split (rep, ",")
        #a = int (rep [0])
        #b = int (rep [1])
        a,b = 10,100

        print "filtrage [%d,%d]" % (a,b)
        filtre_son (t,a,b)

        print "dessin des premiers instants, son filtre"
        dessine_son (mem,t,fourier,indice, a,b)

        print "son filtre"
        s = convert_array (t, s)
        play_sound (s)
        
        pygame.time.delay (6000)

essai ()
