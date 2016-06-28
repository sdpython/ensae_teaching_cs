# coding: cp1252
"""parcours d'un fichier au format XML, l'exemple choisi est un fichier
XML décrivant une liste de morceaux musicaux pour le logiciel Winamp 
(www.winamp.com), ces morceaux placés en des endroits divers
du disque dur sont recopiés dans un répertoire unique"""
import xml.sax        as XML    # pour parser le fichier
import selection_file as FS     # pour sélectionner le nom d'un fichier
import shutil                   # pour la copie de fichier
import os.path                  # gestion des noms de fichiers et répertoires
import string                   # pour la fonction join

class XML_List (XML.ContentHandler) :
    """définition d'une classe dont les méthodes sont appelées à chaque fois
    qu'un élément dans le fichier XML est rencontré,
    cette classe remplit une liste contenant des triplets
    (niveau, balise, attribut, valeur) ou 
    (niveau, balise, None, valeur) ou 
    (niveau, None, None, valeur)"""
    
    def __init__ (self) :
        self.list   = []
        
    def get_list (self) :
        """retourne la liste"""
        return self.list
    
    def startDocument (self) :
        """méthode appelée lorsque le document XML est ouvert"""
        #print "ouverture du fichier XML"
        self.niveau = 0
        
    def endDocument (self) :
        """méthode appelée lorsque le document XML est fermé"""
        #print "fermeture du fichier XML"
        pass
        
    def startElement (self, ba, attr) :
        """méthode appelée chaque fois qu'une nouvelle balise
        est rencontrée, le nom de la balise est ba, les attributs
        associées sont stockées dans attr"""
        self.niveau += 1
        key = attr.keys ()
        for k in key :
            v = attr.get (k)
            self.list.append ((self.niveau, ba,k,v.encode ("latin-1")))
            # v.encode ("latin-1") permet la conversion des chaînes unicode (0-65535)
            # en chaînes de caractères 0-255
        self.balise = ba
        
    def endElement (self, ba) :
        """méthode appelée lorsqu'une balise de fin est rencontrée"""
        self.balise  = None
        self.niveau -= 1
        
    def characters (self,data) :
        """méthode appelée entre une balise et sa balise de fin associée"""
        self.list.append ((self.niveau, self.balise, None, data))
        
def process_file (file) :
    """parcours un fichier et retourne une liste contenant :
    (niveau, balise, attribut, valeur) ou 
    (niveau, balise, None, valeur) ou 
    (niveau, None, None, valeur)"""

    if False :
        # création d'une classe qui va parcourir le fichier XML
        p = XML.make_parser ()
        x = XML_List ()
        # on affecte au parseur une instance de la classe XML_List
        p.setContentHandler (x)
        
        # on lit le fichier file ligne par ligne,
        # chaque ligne est envoyée au parser XML 
        f = open (file, "r")
        for l in f : 
            p.feed (l)
        p.close ()
        f.close ()
        return x.get_list ()
    else :
        # autre solution : on lit le fichier
        # pour n'obtenir qu'une seule chaîne de caractères
        f  = open (file, "r")
        li = f.readlines ()
        f.close ()
        s = string.join (li)
        
        # puis on utilise une fonction qui lit la chaîne complète
        x  = XML_List ()
        XML.parseString (s, x)
        return x.get_list ()     
    

if __name__ == "__main__" :
    # choix d'un nom de fichier
    file    = "xml_example_winamp.xml"
    fs      = FS.FileSelection ("sélection d'un fichier XML", file)
    file    = fs.run ()
    
    # on appelle la fonction process_file pour récupérer les informations
    # inscrites dans le fichier XML
    li = process_file (file)

    # parmi toutes ces informations, on récupère la liste
    # des fichiers de morceaux musicaux, ces morceaux, 
    # pour le logiciel Winamp, sont associés à l'attribut Playstring
    file_list = []
    for l in li :
        if l [2] == "Playstring" : file_list.append (l [3])
    
    # on sélectionne le répertoire dans lequel vont être copiés
    # les morceaux sélectionnés    
    d       = "c:\\temp\\selection"
    fs      = FS.FileSelection ("sélection d'un répertoire destination", d, False)
    d       = fs.run ()
    
    # si le répertoire sélectionné n'existe pas, on le crée
    if not os.path.exists (d) : os.makedirs (d)

    # on copie les fichiers
    for f in file_list :
        str = f.replace ("file:C:\\x_Musique", "")
        str = str.replace ("\\", "_")
        fc  = f.replace ("file:", "")
        print "copie de ", fc, " vers ", d + "\\" + str
        shutil.copy (fc, d + "\\" + str)
        