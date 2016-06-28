# coding: cp1252
"""module contenant une boîte de dialogue permettant 
de sélectionner un fichier ou un répertoire,
il utilise l'interface Tkinter"""
import Tkinter as Tk
import os.path
import os

class FileSelection (object) :
    """classe permettant de sélectionner un fichier 
    ou un répertoire à travers une boîte de dialogue"""
    
    def __init__ (self, titre = "Sélection de fichier", \
                    chemin = None, file = True, exist= True) :
        """initialise la classe
        @param      titre           titre de la fenêtre
        @param      chemin          fichier ou répertoire par défaut
        @param      file            True : fichier, False : répertoire
        @param      exist           True : le répertoire ou le fichier 
                                           sélectionné doit exister"""
        self.titre  = titre
        self.chemin = chemin
        self.file   = file
        self.exist  = exist
        
        if self.chemin == None :  self.chemin = os.getcwd ()
            
    def get_list (self) :
        """retourne la liste des fichiers et des répertoires (2 listes), 
        répertoires seulement et [] si self.file == False"""
        if os.path.isdir (self.chemin) :
            list    = os.listdir (self.chemin)
        else : 
            ch,fi   = os.path.split (self.chemin)
            list    = os.listdir (ch)
        
        lifile  = []
        lidir   = []
        for l in list :
            if os.path.isdir (self.chemin + "\\" + l) : 
                lidir.append (l)
            elif self.file : 
                lifile.append (l)
                
        lidir.sort ()
        lifile.sort ()
        return lidir, lifile
        
    def run (self) :
        """lance la boîte de dialogue et retourne la chaîne sélectionnée"""
        top         = Tk.Toplevel ()
        top.wm_title (self.titre)

        fli     = Tk.Frame (top)
        scrollbar = Tk.Scrollbar (fli)
        li      = Tk.Listbox (fli, width = 120, height = 15, \
                               yscrollcommand = scrollbar.set)
        scrollbar.config (command = li.yview)
        ch      = Tk.Entry (top, width = 120)
        f       = Tk.Frame (top)
        prec    = Tk.Button (f, text = "Précédent")
        suiv    = Tk.Button (f, text = "Entre")
        annul   = Tk.Button (f, text = "Annuler")        
        ok      = Tk.Button (f, text = "Ok")        
        
        prec.grid (column = 0, row = 0)
        suiv.grid (column = 1, row = 0)
        annul.grid (column = 3, row = 0)
        ok.grid (column = 4, row = 0)
        li.pack (side = Tk.LEFT)
        scrollbar.pack(side = Tk.RIGHT, fill = Tk.Y)
        fli.pack ()
        ch.pack ()
        f.pack ()

        def update_chemin () :
            """mise à jour du chemin dans la boîte de dialogue"""
            s = ch.get ()
            ch.delete (0, len (s))
            ch.insert (0, self.chemin)

        def update_list () :
            """mise à jour de la liste des fichiers et répertoires 
            à partir de la chaîne dans la boîte de dialogue"""
            self.chemin     = ch.get ()
            lidir, lifile   = self.get_list ()
            li.delete (0, Tk.END)
            if len (lidir) > 0 : 
                for l in lidir : li.insert (Tk.END, "+ "+ l)
            if len (lifile) > 0 : 
                for l in lifile : li.insert (Tk.END, "  "+ l)
                    
        def precedent () :
            """passe au répertoire précédent"""
            if os.path.isdir (self.chemin) :
                ch, last    = os.path.split (self.chemin)
                self.chemin = ch
            else :
                ch, last    = os.path.split (self.chemin)
                ch, last    = os.path.split (ch)
                self.chemin = ch
            update_chemin ()
            update_list ()
        
        def suivant () :
            """rentre dans un répertoire"""
            sel = ch.get ()
            if os.path.isdir (sel) :
                self.chemin = sel
                update_chemin ()
                update_list ()
            
        def update_sel () :
            """mise à jour de la chaîne de caractères 
            dans la boîte de dialogue à partir de la ligne
            sélectionnée dans la liste"""
            li.after (200, update_sel)
            sel = li.curselection ()
            if len (sel) == 1 :
                t = li.get (sel [0])
                c = self.chemin + "\\" +  t [2:len (t)]
                c = c.replace ("\\\\", "\\")
                s = ch.get ()
                ch.delete (0, len (s))
                ch.insert (0, c)
                
        def annuler () :
            """annule la recherche"""
            self.resultat = False
            top.destroy ()
            top.quit ()
        
        def accepter () :
            """accepte le résultat"""
            self.resultat    = True
            self.chemin = ch.get ()
            top.destroy ()
            top.quit ()
            
        prec.config (command = precedent)
        suiv.config (command = suivant)
        annul.config (command = annuler)
        ok.config (command = accepter)
                
        update_chemin ()
        update_list ()
        update_sel ()
        ch.focus_set ()
        top.mainloop ()
        
        if self.resultat : return self.chemin
        else : return None
            
            
if __name__ == "__main__" :
    root = Tk.Tk ()
    
    def run () :
        r = FileSelection ("sélection d'un fichier", "c:\\")
        s = r.run ()
        print "fichier sélectionné ", s
        
    Tk.Button (text = "fenêtre", command = run).pack ()
    Tk.Button (text = "fermer", command = root.destroy).pack ()
    root.mainloop ()
    