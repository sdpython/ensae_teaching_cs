#coding:latin-1
import urllib.request, os, os.path
def charge_discours () :
    discours = { }
    for annee in [2001, 2005, 2006, 2007, 2008, 2009, 1974, 1975,
                    1979, 1983, 1987, 1989, 1990, 1994] :
        nom = "VOEUX%02d.txt" % (annee % 100)
        if os.path.exists (nom) :
            # si le fichier existe (il a déjà été téléchargé une fois)
            with open (nom, "r") as f :
                text = f.read ()
        else :
            # si le fichier n’existe pas
            link = "http://www.xavierdupre.fr/enseignement/td_python/" + \
            "python_td_minute/data/voeux_presidents/" + nom
            url = urllib.request.urlopen (link)
            text = url.read ().decode("latin-1")
            # on enregistre les données pour éviter de les télécharger une seconde fois
            with open (nom, "w") as f :
                f.write (text)
        discours [annee] = text
    return discours

if __name__ == "__main__" :
    discours = charge_discours ()
    print ("nombre de discours ", len(discours))
