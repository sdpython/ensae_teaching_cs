# coding: cp1252
"""recherche de mot-clés dans des pages HTML, 
ce programme ne peut lire pour l'instant que le format HTML 2.0
et pas HTML 4.01, format utilisé par la plupart des sites."""

import urllib               # accéder une adresse internet
import urlparse             # manipuler les adresses internet
import re                   # expression à chercher
import html_parser_script   # classe de parser HTML modifiée pour éviter les scripts

class HTML_explore (html_parser_script.HTMLParserScript) :
    """parcour un fichier HTML"""
    
    def __init__ (self, list, text, url, niveau, niveau_max) :
        html_parser_script.HTMLParserScript.__init__(self)
        self.list           = list
        self.niveau         = niveau
        self.niveau_max     = niveau_max
        self.url            = url
        self.text           = text
        
    def cherche (self,url) :
        """recherche un url dans la liste"""
        for n,u in self.list :
            if u == url : return True
        return False
        
    def diese (self,adr) :
        """simplifie les liens avec le symboles #"""
        p = adr.find ("#")
        if p == -1 : return adr
        else : return adr [0 : p]

    def handle_starttag (self, tag,attr) :
        """nouveau tag ou balise"""
        if self.niveau >= self.niveau_max : return
        self.tag = tag
        if self.tag == "a" or self.tag == "area" :
            for i,j in attr :
                if (i == "aref" or i == "href") and len (j) > 0 and j [0] != "#" :
                    adr = self.diese (j)
                    if len (adr) > 4 and (adr [0:4] == "http" or adr == "ftp") :
                        if not self.cherche (adr) :
                            self.list.append ((self.niveau, adr))
                    elif len (adr) > 5 and adr [0:6] != "mailto" :
                        adr = urlparse.urljoin (self.url, adr)
                        if not self.cherche (adr) :
                            self.list.append ((self.niveau, adr))
        
    def handle_endtag (self, tag) :
        """fin d'un tag ou balise"""
        pass
        
    def handle_data (self, data) :
        """texte compris entre le début et la fin d'un tag"""
        d = data.replace ("\n", "")
        if len (d) > 3 :
            self.text.append (data)
        
        
def process_file (url, exp, niveau_max = 5, nbmax = -1) :
    """parcours un fichier HTML et retourne la liste des url
    qui contiennent l'expression, la liste des 
    adresses qui n'ont pas pu être atteinte ainsi que le nombre d'adresses
    explorées, cette fonction n'explore pas plus de 
    nbmax pages sauf si nbmax == -1"""
    
    res     = []
    error   = []

    # création d'une classe qui va parcourir le fichier XML
    adr     = [(0, url)]
    text    = []
    errfile = 0
    nb      = 0
    
    for niv,url in adr :

        nb     += 1
        if nb > nbmax and nbmax >= 0 : break
        whole   = ""
        print "open %d/%d" % (nb,len (adr)), 
        print " found = ", len (res), " -- ", niv, " : ", url

        try :
            f       = urllib.urlopen (url)
            d       = f.read ()
            whole  += d
        except Exception, exc:
            print "    exception lecture ", exc, "\t -- ", url
            error.append (url)
            continue 
            
        try :
            text    = []
            p       = HTML_explore (adr, text, url, niv+1, niveau_max)
            # on lit le fichier file ligne par ligne,
            # chaque ligne est envoyée au parser XML 
            p.feed (whole)
            p.close ()
            
            t = ""
            for s in text : t += s + " "
            t = t.replace ("\n", " ")
            t = t.replace ("\r", " ")
            if exp.match (t) : res.append (url)
                
        except Exception, exc:
            print "    exception html ", exc, exc.__class__, "\t -- ", url
            error.append (url)
            f = open ("c:\\temp\\html_err" + str (errfile) + ".html", "w")
            f.write (whole)
            f.close ()
            errfile += 1
            continue 
    
    return res, error, len (adr)
        
    

if __name__ == "__main__" :
    # choix d'un nom de fichier
    url         = "http://www.lemonde.fr/"
    # on appelle la fonction process_file pour récupérer les informations
    # inscrites dans le fichier XML
    s               = ".*Bush.*"
    ex              = re.compile (s, re.IGNORECASE)
    li,error,nb     = process_file (url, ex, 3, -10)
    
    print "--------------------------------------------------------------------"
    print "--------------------------------------------------------------------"
    print "nombre d'adresses explorées :\t", nb
    print "nombre d'adresses sélectionnées :\t", len (li)
    print "nombre d'adresses non ouvertes ou mal lues :\t", len (error)
    print "--------------------------------------------------------------------"
    print "--------------------------------------------------------------------"
    if len (li) > 0 :
        print "url contenant l'expression ", s
        for l in li :
            print " --------- " , l

    if len (error) > 0 :
        print "url n'ayant pas pu être ouverts ou mal lus "
        for l in error :
            print " --- erreur ", l
