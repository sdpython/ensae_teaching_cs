# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.

"""

import os
import io
import urllib.request


def entier_grande_taille():
    """

    @FAQ(Quel est l'entier le plus grand ?)
    La version 3 du langage Python a supprimé la constante ``sys.maxint``
    qui définissait l'entier le plus grand (voir
    `What's New In Python 3.0 <https://docs.python.org/3.1/whatsnew/3.0.html#integers>`_).
    De ce fait la fonction `getrandbit <https://docs.python.org/3.4/library/random.html#random.getrandbits>`_
    retourne un entier aussi grand que l'on veut.

    @code
    import random,sys
    x = random.getrandbits(2048)
    print(type(x),x)
    @endcode

    Qui affiche ::

        <class 'int'> 28821592245571075131654830983838148370214474845580101472119213042190172126736565496812698627920295650674001797895985629679099064974713574340970814696233578272198061719231359573083186306654342306192322853809386167953610349383945699523678043826057910352338185386934425139215277777285416123100069406811011284910239819101658048202284988811705076819806294753255877254609472467038968542731954915621043682174519015068283521575989003211477579416601653132293861235314484703125172048342096920580957771246615770710590596119341983358658507235612104581804871612316272382587635599344895821316316356994838247665194550292758379858074

    Les calculs en nombre réels se font toujours avec huit octets de précision.
    Au delà, il faut utiliser la librairie `gmpy2 <http://gmpy2.readthedocs.org/en/latest/>`_.
    Il est également recommandé d'utiliser cette librairie pour les grands nombres entiers
    (entre 20 et 40 chiffres). La librairie est plus rapide que l'implémentation
    du langage Python (voir `Overview of gmpy2 <https://gmpy2.readthedocs.org/en/latest/overview.html>`_).

    @endFAQ

    @FAQ(Tabulations ou espace ?)
    Il est préférable de ne pas utiliser les tabulations et de les remplacer par des espaces.
    Lorsqu'on passe d'un Editeur à un autre, les espaces ne bougent pas. Les tabulations sont plus ou moins grandes visuellement.
    L'essentiel est de ne pas mélanger.
    Dans `SciTE <http://www.scintilla.org/SciTE.html>`_, il faut aller dans le menu Options / Change Indentation Settings...
    Tous les éditeurs ont une option similaire.
    @endFAQ
    """
    pass


def difference_div():
    """
    @FAQ(Quelle est la différence entre / et // - division ?)
    Le résultat de la division avec l'opérateur ``/`` est toujours réel :
    la division de deux entiers ``1/2`` donne ``0.5``.
    Le résultat de la division avec l'opérateur ``//`` est toujours entier.
    Il correspond au quotient de la division.

    @code
    div1 = 1/2
    div2 = 4/2
    div3 = 1//2
    div4 = 1.0//2.0
    print(div1,div2,div3,div4) # affiche (0.5, 2.0, 0, 0)
    @endcode

    Le reste d'une division entière est obtenue avec l'opérateur ``%``.

    @code
    print ( 5 % 2 )  # affiche 1
    @endcode

    C'est uniquement vrai pour les version Python 3.x.
    Pour les versions 2.x, les opérateurs ``/`` et ``//`` avaient des comportements différents
    (voir `What’s New In Python 3.0 <https://docs.python.org/3/whatsnew/3.0.html#integers>`_).
    @endFAQ
    """
    div1 = 1 / 2
    div2 = 4 / 2
    div3 = 1 // 2
    div4 = 1.0 // 2.0
    return div1, div2, div3, div4


def python_path():
    """
    @FAQ(Comment éviter sys.path.append... quand on développe un module ?)
    Lorsqu'on développe un module,
    on ne veut pas l'installer. On ne veut pas qu'il soit présent dans le répertoire ``site-packages`` de la distribution
    de Python car cela introduit deux versions : celle qu'on développe et celle qu'on a installer.
    Avant, je faisais cela pour créer un petit programme utilisant mon propre module
    (et on en trouve quelque trace dans mon code) :

    @code
    import sys
    sys.path.append("c:/moncode/monmodule/src")
    import monmodule
    @endcode

    Quand je récupère un programme utilisant ce module, il me faudrait ajouter
    ces petites lignes à chaque fois et c'est barbant.
    Pour éviter cela, il est possible de dire à l'interpréteur Python d'aller chercher
    ailleurs pour trouver des modules en ajoutant le chemin à la
    `variable d'environnement <http://fr.wikipedia.org/wiki/Variable_d'environnement>`_
    `PYTHON_PATH <https://docs.python.org/3.4/using/cmdline.html#envvar-PYTHONPATH>`_.
    Sous Windows :

    @code
    set PYTHON_PATH=%PYTHON_PATH%;c:\\moncode\\monmodule\\src
    @endcode

    @endFAQ
    """
    return os.environ.get("PYTHON_PATH", "")


def test_unitaire():
    """
    @FAQ(Qu'est-ce qu'un test unitaire ?)

    Un `test unitaire <http://fr.wikipedia.org/wiki/Test_unitaire>`_
    une procédure permettant de vérifier le bon fonctionnement d'une partie précise.
    Concrètement, cela consiste à écrire une fonction qui exécute la partie de code
    à vérifier. Cette fonction retourne ``True`` si le test est valide, c'est-à-dire
    que la partie de code s'est comportée comme prévue : elle a retourné le résultat attendu.
    Elle déclenche une exception si elle le code à vérifier ne se comporte pas comme prévu.

    Par example, si on voulait écrire un test unitaire pour la fonction
    `pow <https://docs.python.org/3.4/library/functions.html#pow>`_, on pourrait
    écrire ::

        def test_pow():
            assert pow(2,1) == 2   # on vérifie que 2^1 == 0
            assert pow(2,0) == 1
            assert pow(2,-1) == 0.5
            assert pow(2,-1) == 0.5
            assert pow(0,0) == 1     # convention, on s'assure qu'elle ne change pas
            assert isinstance(pow(-2,3.4), complex)
            return True


    **A quoi ça sert ?**

    On écrit la fonction ``x_exp`` (:math:`=y x^{-n}`) comme suit ::

        def x_exp(x,y,n):
            return y / pow(x,n)

    La fonction retourne 0 si :math:`x=y=n=0`.
    Admettons maintenant qu'un dévelopeur veuille changer la convention :math:`0^0=1` en :math:`0^0=0`.
    La fonction précédente produira une erreur à cause d'une division ``0/0``.
    Un test unitaire détectera au plus tôt cette erreur.

    Les tests unitaires garantissent la qualité d'un logiciel qui est considéré comme bonne
    si 80% du code est couvert par un test unitaire. Lorsque plusieurs personnes
    travaillent sur un même programme, un dévelopeur utilisera une fonction faite par un
    autre. Il s'attend donc à ce que la fonction produise les mêmes résultats
    avec les mêmes entrées
    **même si on la modifie ultérieurement**.
    Les tests unitaires servent à s'assurer qu'il n'y a pas d'erreur
    introduite au sein des résultats intermédiaire d'une chaîne de traitement, auquel
    cas, c'est une cascade d'erreur qui est susceptible de se produite. La source
    d'une erreur est plus facile à trouver lorsque les tests unitaires sont nombreux.

    @endFAQ
    """
    assert pow(2, 1) == 2   # on vérifie que 2^1 == 0
    assert pow(2, 0) == 1
    assert pow(2, -1) == 0.5
    assert pow(2, -1) == 0.5
    assert pow(0, 0) == 1
    assert isinstance(pow(-2, 3.4), complex)
    return True


def same_variable(a, b):
    """
    Cette fonction dit si les deux objets sont en fait le même objet (True)
    ou non (False) s'ils sont différents (même s'ils contiennent la même information).

    @param      a       n'importe quel objet
    @param      b       n'importe quel objet
    @return             ``True`` ou ``False``

    @FAQ(Qu'est-ce qu'un type immuable ou immutable ?)
    Une variable de type *immuable* ne peut être modifiée. Cela concerne principalement :

        - ``int``, ``float``, ``str``, ``tuple``

    Si une variable est de type *immuable*, lorsqu'on effectue une opération,
    on créé implicitement une copie de l'objet.

    Les dictionnaires et les listes sont *modifiables* (ou *mutable*). Pour une variable
    de ce type, lorsqu'on écrit ``a = b``, ``a`` et ``b`` désigne le même objet même
    si ce sont deux noms différentes. C'est le même emplacement mémoire
    accessible paur deux moyens (deux identifiants).

    Par exemple ::

        a  = (2,3)
        b  = a
        a += (4,5)
        print( a == b ) # --> False
        print(a,b)      # --> (2, 3, 4, 5) (2, 3)

        a  = [2,3]
        b  = a
        a += [4,5]
        print( a == b ) # --> True
        print(a,b)      # --> [2, 3, 4, 5] [2, 3, 4, 5]

    Dans le premier cas, le type (``tuple``) est _immutable_, l'opérateur ``+=`` cache implicitement une copie.
    Dans le second cas, le type (``list``) est _mutable_, l'opérateur ``+=`` évite la copie
    car la variable peut être modifiée. Même si ``b=a`` est exécutée avant l'instruction suivante,
    elle n'a **pas** pour effet de conserver l'état de ``a`` avant l'ajout d'élément.
    Un autre exemple ::

        a  = [1, 2]
        b  = a
        a [0] = -1
        print(a)        # --> [-1, 2]
        print(b)        # --> [-1, 2]

    Pour copier une liste, il faut expliciter la demander ::

        a  = [1, 2]
        b  = list(a)
        a [0] = -1
        print(a)        # --> [-1, 2]
        print(b)        # --> [1, 2]

    La page `Immutable Sequence Types <https://docs.python.org/3.4/library/stdtypes.html?highlight=immutable#immutable-sequence-types>`_
    détaille un peu plus le type qui sont *mutable* et ceux qui sont *immutable*. Parmi les types standards :

        * **mutable**
            * `bool <https://docs.python.org/3.4/library/functions.html#bool>`_
            * `int <https://docs.python.org/3.4/library/functions.html#int>`_, `float <https://docs.python.org/3.4/library/functions.html#float>`_, `complex <https://docs.python.org/3.4/library/functions.html#complex>`_
            * `str <https://docs.python.org/3.4/library/functions.html#func-str>`_, `bytes <https://docs.python.org/3.4/library/functions.html#bytes>`_
            * `None <https://docs.python.org/3.4/library/constants.html?highlight=none#None>`_
            * `tuple <https://docs.python.org/3.4/library/functions.html#func-tuple>`_, `frozenset <https://docs.python.org/3.4/library/functions.html#func-frozenset>`_
        * **immutable**, par défaut tous les autres types dont :
            * `list <https://docs.python.org/3.4/library/functions.html#func-list>`_
            * `dict <https://docs.python.org/3.4/library/functions.html#func-dict>`_
            * `set <https://docs.python.org/3.4/library/functions.html#func-set>`_
            * `bytearray <https://docs.python.org/3.4/library/functions.html#bytearray>`_

    Une instance de classe est mutable. Il est possible de la rendre
    immutable par quelques astuces :

        * `__slots__ <https://docs.python.org/3.4/reference/datamodel.html?highlight=_slots__#object.__slots__>`_
        * `How to Create Immutable Classes in Python <http://www.blog.pythonlibrary.org/2014/01/17/how-to-create-immutable-classes-in-python/>`_
        * `Ways to make a class immutable in Python <http://stackoverflow.com/questions/4996815/ways-to-make-a-class-immutable-in-python>`_
        * `freeze <https://freeze.readthedocs.org/en/latest/>`_

    Enfin, pour les objects qui s'imbriquent les uns dans les autres, une liste de listes, une classe
    qui incluent des dictionnaires et des listes, on distingue une copie simple d'une copie intégrale (**deepcopy**).
    Dans le cas d'une liste de listes, la copie simple recopie uniquement la première liste ::

        import copy
        l1 = [ [0,1], [2,3] ]
        l2 = copy.copy(l1)
        l1 [0][0] = '##'
        print(l1,l2)        # --> [['##', 1], [2, 3]] [['##', 1], [2, 3]]

        l1 [0] = [10,10]
        print(l1,l2)        # --> [[10, 10], [2, 3]] [['##', 1], [2, 3]]

    La copie intégrale recopie également les objets inclus ::

        import copy
        l1 = [ [0,1], [2,3] ]
        l2 = copy.deepcopy(l1)
        l1 [0][0] = '##'
        print(l1,l2)        # --> [['##', 1], [2, 3]] [[0, 1], [2, 3]]

    Les deux fonctions s'appliquent à tout object Python : `module copy <https://docs.python.org/3.4/library/copy.html>`_.
    @endFAQ
    """
    return id(a) == id(b)


def stringio(text):
    """
    returns a StringIO object on a text

    @param      text        any text
    @return                 StringIO object

    @FAQ(A quoi sert un ``StringIO`` ?)
    La plupart du temps, lorsqu'on récupère des données, elles sont sur le disque dur
    de votre ordinateur dans un fichier texte. Lorsqu'on souhaite automatiser un processur
    qu'on répète souvent avec ce fichier, on écrit une fonction qui prend le nom du fichier en entrée.

    @code
    def processus_quotidien(nom_fichier) :
        # on compte les lignes
        nb = 0
        with open(nom_fichier,"r") as f :
            for line in f :
                nb += 1
        return nb
    @endcode

    Et puis un jour, les données ne sont plus dans un fichier mais sur Internet.
    Le plus simple dans ce cas est de recopier ces données sur disque dur et d'appeler la même fonction.
    Simple. Un autre les données qu'on doit télécharger font plusieurs gigaoctets. Tout télécharger prend
    du temps pour finir pour s'apercevoir qu'elles sont corrompues. On a perdu plusieurs heures pour rien.
    On aurait bien voulu que la fonction ``processus_quotidien`` commence à traiter les données
    dès le début du téléchargement.

    Pour cela, on a inventé la notion de **stream** ou **flux** qui sert d'interface entre la fonction
    qui traite les données et la source des données. Le flux lire les données depuis n'importe quel source
    (fichier, internet, mémoire), la fonction qui les traite n'a pas besoin d'en connaître la provenance.

    `StringIO <https://docs.python.org/3.4/library/io.html#io.StringIO>`_ est un flux qui considère
    la mémoire comme source de données.

    @code
    def processus_quotidien(data_stream):
        # on compte toujours les lignes
        nb = 0
        for line in data_stream :
            nb += 1
        return nb
    @endcode

    La fonction ``processus_quotidien`` fonctionne pour des données en mémoire
    et sur un fichier.

    @code
    fichier = __file__
    f = open(fichier,"r")
    nb = processus_quotidien(f)
    print(nb)

    text = "ligne1\nligne2"
    st = io.StringIO(text)
    nb = processus_quotidien(st)
    print(nb)
    @endcode

    @endFAQ
    """
    return io.StringIO(text)


def property_example():
    """

    @FAQ(property)

    Une `property <https://docs.python.org/3.4/library/functions.html#property>`_ est
    une écriture qui sert à transformer l'appel d'une méthode de classe
    en un attribut.

    @code

    class ClasseAvecProperty:

        def __init__(self,x,y):
            self._x, self._y = x,y

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        @property
        def norm2(self):
            return self._y**2 + self._x**2

    c = ClasseAvecProperty(1,2)
    print(c.x)
    print(c.y)

    @endcode

    ``x`` est définit comme une méthode mais elle retourne simplement l'attribut
    ``_x``. De cette façon, il est impossible de changer ``x`` en écrivant::

        c.x = 5

    Cela déclenche l'erreur::

        Traceback (most recent call last):
          File "faq_python.py", line 455, in <module>
            c.x = 5
        AttributeError: can't set attribute

    On fait cela parce que l'écriture est plus courte et que cela
    évite certaines erreurs.

    @endFAQ
    """
    pass


def enumerate_regex_search(exp, text):
    """
    Cette fonction itère sur les différentes occurences d'une expression régulière.

    @param      exp     expression régulière
    @param      text    text à parser
    @return             itérateur

    @FAQ(Comment itérer sur les résultats d'une expression régulière ?)

    On utilise la méthode `finditer <https://docs.python.org/3.4/library/re.html#re.regex.finditer>`_.

    @code
    found = exp.search(text)
    for m in exp.finditer(text):
        # ...
    @endcode

    Voir également `Petites subtilités avec les expressions régulières en Python <http://www.xavierdupre.fr/blog/2014-12-02_nojs.html>`_.

    @endFAQ
    """
    # found = exp.search(text)
    for m in exp.finditer(text):
        yield m


def download_from_url(url, filename):
    """

    .. index:: dropbox

    downloads a file given a URL and stores it as binary file

    @param      url         url
    @param      filename    local filename
    @return                 filename

    @FAQ(Télécharger un fichier depuis un notebook?)

    L'exemple suivant illustre comment télécharger puis enregister ce fichier
    sur le disque local. Il ne faut pas que ce fichier dépasse la taille de la mémoire.
    L'url donné en exemple est celui utilisé sur DropBox.

    @code
    url = "https://www.dropbox.com/[something]/[filename]?dl=1"  # dl=1 is important
    import urllib.request
    u = urllib.request.urlopen(url)
    data = u.read()
    u.close()

    with open([filename], "wb") as f :
        f.write(data)
    @endcode

    L'exemple est tiré de `Download a file from Dropbox with Python <http://www.xavierdupre.fr/blog/2015-01-20_nojs.html>`_.

    @endFAQ

    """
    u = urllib.request.urlopen(url)
    data = u.read()
    u.close()

    with open(filename, "wb") as f:
        f.write(data)
    return filename


def sortable_class(cl):
    """
    @FAQ(Classe sortable)

    Il faut prononcer *sortable* à l'anglaise. Comment rendre une classe
    *sortable* ? Pour faire simple, on veut écrire ::

        l = [ o1, o2 ]
        l.sort()

    Où ``o1`` et ``o2`` sont des objets d'une classe
    que vous avez définie ::

        class MaClasse:

            ...

    Pour que cela fonctionne, il suffit juste
    de surcharger l'opérateur ``<`` ou plus exactement
    ``__lt__``. Par exemple ::

        class MaClasse:

            def __lt__(self, autre_instance):
                if self.jenesaispas < autre.jenesaispas:
                    return True
                elif self.jenesaispas > autre.jenesaispas:
                    return False:
                else:
                    if self.jenesaispas2 < autre.jenesaispas2:
                        return True
                    else:
                        return False

    @endFAQ
    """
    pass


def list_of_installed_packages():
    """
    calls ``pip list`` to retrieve the list of packages


    @FAQ(Obtenir des informations sur les packages installés)

    Le module `pip <https://pip.pypa.io/en/stable/>`_ retourne des informations
    sur n'importe quel module installé, sa version, sa license ::

        pip show pandas

    On peut également l'obtenir depuis l'interpréteur python ::

        import pip
        pip.main(["show", "pandas"])

    Exemple ::

        Name: pandas
        Version: 0.16.0
        Summary: Powerful data structures for data analysis, time series,and statistics
        Home-page: http://pandas.pydata.org
        Author: The PyData Development Team
        Author-email: pydata@googlegroups.com
        License: BSD
        Location: c:\python34_x64\lib\site-packages
        Requires: python-dateutil, pytz, numpy

    On utilise également ``pip freeze`` pour répliquer l'environnement
    dans lequel on a développé un programme. `pip freeze <https://pip.pypa.io/en/latest/reference/pip_freeze.html>`_
    produit la liste des modules avec la version utilisée ::

        docutils==0.11
        Jinja2==2.7.2
        MarkupSafe==0.19
        Pygments==1.6
        Sphinx==1.2.2

    Ce qu'on utilise pour répliquer l'environnement de la manière suivante ::

        pip freeze > requirements.txt
        pip install -r requirements.txt

    Cette façon de faire fonctionne très bien sous Linux mais n'est pas encore
    opérationnelle sous Windows à moins d'installer le compilateur C++ utilisée pour compiler
    Python.

    @endFAQ
    """
    from pyquickhelper.pycode.pip_helper import get_packages_list
    return get_packages_list()


def information_about_package(name):
    """
    calls ``pip show`` to retrieve information about packages


    @FAQ(Récupérer la liste des modules installés)

    Le module `pip <https://pip.pypa.io/en/stable/>`_ permet d'installer
    de nouveaux modules mais aussi d'obtenir la liste des packages installés ::

        pip list

    On peut également l'obtenir depuis l'interpréteur python ::

        import pip
        pip.main(["list"])

    @endFAQ

    @FAQ(Pourquoi l'installation de pandas (ou numpy) ne marche pas sous Windows avec pip ?)

    Python est un langage très lent et c'est pourquoi la plupart des modules de calculs numériques
    incluent des parties implémentées en langage C++.
    `numpy <http://www.numpy.org/>`_,
    `pandas <http://pandas.pydata.org/>`_,
    `matplotlib <http://matplotlib.org/>`_,
    `scipy <http://www.scipy.org/>`_,
    `scikit-learn <http://scikit-learn.org/stable/>`_,
    ...

    Sous Linux, le compilateur est intégré au système et l'installation de ces modules via
    l'instruction ``pip install <module>`` met implicitement le compilateur à contribution.
    Sous Windows, il n'existe pas de compilateur C++ par défaut à moins de l'installer.
    Il faut faire attention alors d'utiliser exactement le même que celui utilisé
    pour compiler Python (voir
    `Compiling Python on Windows <https://docs.python.org/3.4/using/windows.html#compiling-python-on-windows>`_).

    C'est pour cela qu'on préfère utiliser des distributions comme
    `Anaconda <http://continuum.io/downloads#py34>`_
    qui propose par défaut
    une version de Python accompagnée des modules les plus utilisés. Elle propose également une façon
    simple d'installer des modules précompilés avec l'instruction ::

        conda install <module_compile>

    L'autre option est d'utilser le site
    `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
    qui propose des versions compilées sous Windows d'un grand nombre de modules.
    Il faut télécharger le fichier *.whl* puis l'installer avec l'instruction ``pip install <fichier.whl>``.
    La différence entre les deux ooptions tient aux environnements virtuels, voir
    `Python virtual environments <http://astropy.readthedocs.org/en/stable/development/workflow/virtual_pythons.html>`_.


    @endFAQ
    """
    from pyquickhelper.pycode.pip_helper import get_package_info
    return get_package_info(name)

if __name__ == "__main__":

    def processus_quotidien(data_stream):
        # on compte toujours les lignes
        nb = 0
        for line in data_stream:
            nb += 1
        return nb

    fichier = __file__
    f = open(fichier, "r")
    nb = processus_quotidien(f)
    print(nb)

    text = "ligne1\nligne2"
    st = io.StringIO(text)
    nb = processus_quotidien(st)
    print(nb)

    class ImmutableClass(object):
        __slots__ = ["x", "y"]

        def __init__(self, x, y):
            self.x, self.y = x, y

        def __str__(self):
            return "{},{}".format(self.x, self.y)

    i1 = ImmutableClass(1, 2)
    i2 = i1
    i2.x = -1
    print(i1, i2)

    import copy
    l1 = [[0, 1], [2, 3]]
    l2 = copy.copy(l1)
    l1[0][0] = -1
    print(l1, l2)

    l1[0] = [10, 10]
    print(l1, l2)

    import copy
    l1 = [[0, 1], [2, 3]]
    l2 = copy.deepcopy(l1)
    l1[0][0] = -1
    print(l1, l2)

    a = []
    b = a
    b += [2]
    print(a)

    class ClasseAvecProperty:

        def __init__(self, x, y):
            self._x, self._y = x, y

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        @property
        def norm2(self):
            return self._y ** 2 + self._x ** 2

    c = ClasseAvecProperty(1, 2)
    print(c.x)
    print(c.y)
    c.x = 5


def get_month_name(date):
    """
    returns the month name for a give date

    @param      date        datatime
    @return                 month name

    @FAQ(Récupérer le nom du mois à partir d'une date)

    ::

        import datetime
        dt = datetime.datetime(2016, 1, 1)
        print(dt.strftime("%B"))


    @endFAQ
    """
    return date.strftime("%B")


def get_day_name(date):
    """
    returns the day name for a give date

    @param      date        datatime
    @return                 month name

    @FAQ(Récupérer le nom du jour à partir d'une date)

    ::

        import datetime
        dt = datetime.datetime(2016, 1, 1)
        print(dt.strftime("%A"))

    @endFAQ
    """
    return date.strftime("%A")
