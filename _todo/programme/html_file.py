# coding: cp1252
import os
import os.path
import PIL.Image
        
class html_file (object) :
    """cette classe propose quelques méthodes pour écrire un fichier HTML simplement"""
    
    header = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<HTML>
<HEAD>
</HEAD>
<BODY >"""

    foot = """</BODY>
</HTML>        
    """
    
    def __init__ (self, file) :
        """construction d'un fichier HTML"""
        self.file = file
        
    def open (self) :
        """ouverture du fichier"""
        self.f = open (self.file, "w")
        self.f.write (self.header)
        
    def close (self) :
        """fermeture du fichier"""
        self.f.close ()
        
    def text (self, s) :
        """écrit du texte dans un fichier HTML"""
        s = s.replace ("\n", "<BR>")
        self.f.write (s)
        
    def text_line (self) :
        """passe une ligne dans un fichier HTML"""
        self.f.write ("<BR>")
        
    def table_begin (self, nc) :
        """commence une table, nc est le nombre de colonnes"""
        self.f.write ("""<TABLE cellSpaceing="1" """)
        self.f.write ("""cellPadding="1" border="1">\n  <TR>\n    <TD>""")
        
    def table_end (self) :
        """termine une table"""
        self.f.write ("""    </TD>\n  </TR>\n</TABLE>\n""")
        
    def table_next (self) :
        """passe à la colonne suivante"""
        self.f.write ("""    </TD>\n    <TD>""")
        
    def table_next_line (self) :
        """passe à la ligne suivante"""
        self.f.write ("""    </TD>\n  </TR>\n  <TR>\n    <TD>""")
        
    def relative_path (self, url) :
        """trouve le chemin relatif par rapport au fichier"""
        pr = os.path.commonprefix ( [ self.file, url ] )
        if pr != None :
            d = os.path.dirname (self.file)
            if pr.count (d) == 1 :
                pr = d + "\\"
            url = url [ len (pr) : len (url) ]
        return url

    def clean_url (self, url) :
        """enlève les espaces et redresse les barres"""
        url = url.replace (" ", "\%20")
        url = url.replace ("\\", "/")
        return url
        
    def add_link (self, url, caption, isfile) :
        """ajoute un lien dans le fichier html, 
        url est l'adresse, caption est l'intitulé du lien, 
        si isfile vaut True, cherche un chemin relatif par rapport à self.file"""
        if isfile : url = self.relative_path (url)
        url = self.clean_url (url) 
        s   = """<A HREF="%s">%s</A>""" % (url, caption)
        self.f.write (s)
        
    def add_image (self, image, size = None, zoom = None) :
        """ajoute une image dans le fichier html,
        celle-ci est enregistrée avec un numéro, offre la possibilité de zoomer 
        ou de modifier la taille"""
        if not self.__dict__.has_key ("num_image") : self.num_image = 0
        name, ext = os.path.splitext (self.file)
        name      = name + str (self.num_image) + ".png"
        image.save (name)
        self.add_image_link (name, size, zoom)
        self.num_image += 1
        
    def add_image_link (self, url, size = None, zoom = None) :
        """ajoute une image dans le fichier html,
        cette image n'est pas recopiée, il est possible de spécifier une taille, 
        ou de multiplier cette taille"""
        
        if size == None :
            im      = PIL.Image.open (url)
            size    = im.size
        if zoom != None :
            size = (int (size [0] * zoom), int (size [1] * zoom))

        url = self.relative_path (url)
        url = self.clean_url (url) 
            
        s = """<IMG width=%d height=%d border=0 SRC="%s" alt="%s">""" \
                        % (size [0], size [1], url, url)
        self.f.write (s)

        
if __name__ == "__main__" :
    
    print "écriture du fichier ",file
    file = "c:\\temp\\essai.html"
    
    html = html_file (file)
    html.open ()
    html.text ("""première ligne d'un fichier HTML,
    seconde ligne""")
    html.table_begin (2)
    html.text ("1")
    html.table_next ()
    html.text ("2")
    html.table_next_line ()
    html.text("3")
    html.table_next ()
    html.text ("4")
    html.table_end ()
    html.add_link ("c:\\temp\\cours.py", "cours.py", True)
    html.text_line ()
    im = PIL.Image.new ("RGB", (100,100), color = (100,100,100))
    html.add_image (im)
    html.add_image (im, zoom = 2)
    html.close ()
    
    print "fin"

