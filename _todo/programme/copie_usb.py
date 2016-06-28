# coding: cp1252
"""copie de fichiers sur une clé USB"""

import re       # pour les expressions régulières
import os       # pour les fichiers et répertoires
import os.path  # pour les noms de fichiers et noms de répertoires
import copy
import shutil   # pour la copie de fichiers

class copie_usb (object):
    """recopie des fichiers sur une clé USB"""
    
    def __init__(self,ch1,ch2,accept = ".*",refuse = "") :
        """initialisation,
        @param      ch1         répertoire source
        @param      ch2         répertoire destination
        @param      accept      filtre pour les fichiers acceptés pour la copie
        @param      refuse      pour refuser des fichiers parmi ceux déjà acceptés"""
        self.ch1     = ch1
        self.ch2     = ch2
        self.accept  = re.compile (accept, re.IGNORECASE) # création des motifs
        self.refuse  = re.compile (refuse, re.IGNORECASE) # création des motifs
        
    def accepter (self, fichier) :
        """dit si un fichier est accepté à la copie ou non"""
        r = re.match (self.accept, fichier)
        if not r : return False
        r = re.match (self.refuse, fichier)
        return not r
        
    def aide (self) :
        """retourne une aide sur les formats d'expression"""
        help (re.engine)
        
    def liste_fichier_repertoire (self,repertoire):
        """récupération de la liste des répertoires et celle des fichiers, 
        inclus dans le répertoire repertoire"""
        rep     = []
        file    = []
        list    = os.listdir (repertoire)
        
        for cc in list :
            c = repertoire + "\\" + cc
            if os.path.isfile (c) : file.append (cc)
            if os.path.isdir (c) : rep.append (cc)
        
        rep2 = copy.copy (rep)
        for chemin in rep2 :
            r,f = self.liste_fichier_repertoire (repertoire + "\\" + chemin)
            for x in r :
                rep.append (chemin + "\\" + x)
            for x in f :
                file.append (chemin + "\\" + x)
            
        return rep,file
        
    def repertoire_selectionne (self, r, file_clean) :
        """dit si la liste file_clean contient au moins un fichier 
        inclus dans le repertoire r"""
        t = re.compile ("^" + r + "\\\\.*", re.IGNORECASE)
        for l in file_clean :
            if re.match (t,l) : return True
        return False
        
    def copie (self) :
        """effectue la copie"""
        
        # récupération de la liste des répertoires et fichiers
        rep,file = self.liste_fichier_repertoire (self.ch1)
        # élimination des importuns
        file_clean = [ f for f in file if self.accepter (f) ]
        
        # facultatif, exclue les répertoires pour lesquels 
        # aucun fichier n'est sélectionné
        rep_clean = [ r for r in rep if self.repertoire_selectionne (r, file_clean) ]
        
        # on créé les répertoires s'il n'existent pas
        if not os.path.exists (self.ch2) :
            print "création du répertoire ", self.ch2
            os.mkdir (self.ch2)

        for r in rep_clean :
            c = self.ch2 + "\\" + r
            if not os.path.exists (c) :
                print "création du répertoire ", r
                os.mkdir (c)
                
        # on recopie les fichiers
        for f in file_clean :
            s = self.ch1 + "\\" + f
            c = self.ch2 + "\\" + f
            print "copie du fichier ", f
            shutil.copy (s, c)
        

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
    
    c = copie_usb (ch1, ch2, filtre_accept, filtre_refuse)
    c.copie ()

