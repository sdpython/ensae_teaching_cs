# coding: cp1252
"""copie de fichiers sur une clé USB, interface fenêtrée, 
enregistrement des paramètres précédents"""

import copie_usb_window   # version avec fenêtre
import os.path            # pour détecter l'existence d'un fichier
import re                 # pour les expressions régulières

class copie_usb_window_save (copie_usb_window.copie_usb_window):
    """recopie des fichiers sur une clé USB avec une fenêtre graphique,
    et enregistrement des précédents paramètres"""

    def ecrire_parametre (self, txt) :
        """écriture des paramètres dans le fichier txt"""
        # ouverture du fichier en mode écriture
        f = open (txt, "w")
        f.write (self.ch1)
        f.write ("\n")
        f.write (self.ch2)
        f.write ("\n")
        f.write (self.accept.pattern)
        f.write ("\n")
        f.write (self.refuse.pattern)
        f.write ("\n")
        f.close ()
        
    def lire_parametre (self, txt) :
        """relecture des paramètres écrits dans le fichier txt s'il existe"""
        if os.path.exists (txt) :
            f           = open (txt, "r")
            
            s           = f.readline ()
            s = s.replace ("\n", "")
            self.ch1    = s
            
            s           = f.readline ()
            s = s.replace ("\n", "")
            self.ch2    = s
            
            s           = f.readline ()
            s = s.replace ("\n", "")
            self.accept = re.compile (s)
            
            s           = f.readline ()
            s = s.replace ("\n", "")
            self.refuse = re.compile (s)
            
            f.close ()

    def fenetre (self) :
        """méthode fenêtre surchargée pour lire les derniers paramètres
        et enregistrer les nouveaux"""
        # première étape, lire les précédents paramètres
        self.lire_parametre ("copie_usb_window_save.txt")
        # seconde étape, appel de la méthode précédente
        copie_usb_window.copie_usb_window.fenetre (self) 
        # troisième étape, écriture des paramètres
        self.ecrire_parametre ("copie_usb_window_save.txt")
        
        
if __name__ == "__main__" :
    
    print "copie de fichiers vers une clé USB"
    ch1             = "C:\\Documents and Settings\\Dupré\\" \
                        "Mes documents\\informatique\\support\\python_td"
    ch2             = "c:\\temp\\copie_usb"
    filtre_accept   = ".*[.].*"
    filtre_refuse   = ".*[.]pdf$|.*[.]html$|.*[.]bmp|programme\\\\.*[.]zip$"
    
    # filtre_accept accepte tout type de fichier
    # filtre_refuse refuse tous les fichiers dont l'extension est pdf, html ou 
    # inclus dans le répertoire programme et ayant l'extension zip
    
    c = copie_usb_window_save (ch1, ch2, filtre_accept, filtre_refuse)
    c.fenetre ()
    