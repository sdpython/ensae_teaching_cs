# -*- coding:utf-8 -*-
import os
import sys


def import_module(name, moduleName=None, url=None, glo=globals(), loc=locals()):
    """
    Imports a module given its name, look for it on http://www.xavierdupre.fr/...,
    the file is copied at this file location.

    @param      name        name of the module
    @param      moduleName  like import name as moduleName, None for name
    @param      url         link to the website to use
    @param      glo         globals()
    @param      loc         locals()
    @return                 modules
    """
    file = "%s.py" % name
    if not os.path.exists(file):
        path = "../../../../complements_site_web"
        f2 = os.path.join(path, file)
        if os.path.exists(f2):
            print("ajout de ", f2)
            u = open(f2, "r")
            all = u.read()
            u.close()
        else:
            print("téléchargement de ", url + file)
            if url == None:
                url = "http://www.xavierdupre.fr/enseignement/tutoriel_python/graphviz/"
            url += file
            u = urllib.urlopen(url, "r")
            all = u.read()
            if "404 Not Found" in all:
                raise Exception("fichier introuvable")
            u.close()
        u = open(file, "w")
        u.write(all)
        u.close()
    temp = __import__(name, glo, loc, [], -1)
    if moduleName == None:
        moduleName = name
    glo[moduleName] = temp
    sys.modules[moduleName] = temp
    return temp


if __name__ == "__main__":
    use_graphivz2 = import_module("use_graphivz")
    use_graphivz2.check_module()
    use_graphivz.check_module()
