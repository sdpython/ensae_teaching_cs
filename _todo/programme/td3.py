# coding: cp1252
import string

def lire_separation(s):
    """divise un nombre littéral en mots"""
    s = string.replace (s, "-", " ")
    return string.split (s)

def lire_separation(s):
    """divise un nombre littéral en mots"""
    return re.compile ("[- ]").split (s)

def valeur_mot (s) :
    """convertit numériquement les nombres inclus entre 0 et 16 inclus,
    20, 30, 40, 50, 60, s est une chaîne de caractères, le résultat est entier"""
    if   s == "zéro"      : return 0
    elif s == "un"        : return 1
    elif s == "deux"      : return 2
    elif s == "trois"     : return 3
    elif s == "quatre"    : return 4
    elif s == "cinq"      : return 5
    elif s == "six"       : return 6
    elif s == "sept"      : return 7
    elif s == "huit"      : return 8
    elif s == "neuf"      : return 9
    elif s == "dix"       : return 10
    elif s == "onze"      : return 11
    elif s == "douze"     : return 12
    elif s == "treize"    : return 13
    elif s == "quatorze"  : return 14
    elif s == "quinze"    : return 15
    elif s == "seize"     : return 16
    elif s == "vingt"     : return 20
    elif s == "trente"    : return 30
    elif s == "quarante"  : return 40
    elif s == "cinquante" : return 50
    elif s == "soixante"  : return 60
    else                  : return 0
        
def valeur_mot (s) :
    """convertit numériquement les nombres inclus entre 0 et 16 inclus,
    20, 30, 40, 50, 60, s est une chaîne de caractères, le résultat est entier"""
    dico = {'cinquante': 50, 'quarante': 40, 'onze': 11, 'huit': 8, 'six': 6, \
            'quinze': 15, 'trente': 30, 'douze': 12, 'cinq': 5, 'deux': 2, \
            'quatorze': 14, 'neuf': 9, 'soixante': 60, 'quatre': 4, \
            'zéro': 0, 'treize': 13, 'trois': 3, 'seize': 16, \
            'vingt': 20, 'un': 1, 'dix': 10, 'sept': 7}
    if s not in dico : return 0
    else : return dico [s]

def lire_dizaine_liste(s):
    """convertit une liste de chaîne de caractères dont
    juxtaposition forme un nombre littéral compris entre
    0 et 99"""
    r       = 0         # contient le résultat final
    dizaine = False     # a-t-on terminé le traitement des dizaines ?
    for mot in s:
        n = valeur_mot (mot)
        if n == 20 :
            if not dizaine and r > 0 and r != 60:
                r       *= n     # cas 80
                dizaine  = True
            else : r += n
        else : r += n
    return r

def lire_dizaine(s):
    s2 = s.replace ("-", " ")
    li = string.split (s2)
    return lire_dizaine_liste (li)

def mot_valeur (x):
    """convertit un nombre compris inclus entre 0 et 16 inclus,
    20, 30, 40, 50, 60 en une chaîne de caractères"""
    if   x == 0: return "zéro"
    elif x == 1: return "un"
    elif x == 2: return "deux"
    elif x == 3: return "trois"
    elif x == 4: return "quatre"
    elif x == 5: return "cinq"
    elif x == 6: return "six"
    elif x == 7: return "sept"
    elif x == 8: return "huit"
    elif x == 9: return "neuf"
    elif x == 10: return "dix"
    elif x == 11: return "onze"
    elif x == 12: return "douze"
    elif x == 13: return "treize"
    elif x == 14: return "quatorze"
    elif x == 15: return "quinze"
    elif x == 16: return "seize"
    elif x == 20: return "vingt"
    elif x == 30: return "trente"
    elif x == 40: return "quarante"
    elif x == 50: return "cinquante"
    elif x == 60: return "soixante"
    elif x == 70: return "soixante-dix"
    elif x == 80: return "quatre-vingt"
    elif x == 90: return "quatre-vingt-dix"
    else        : return "zéro"
        
def mot_valeur (x):
    """convertit un nombre compris inclus entre 0 et 16 inclus,
    20, 30, 40, 50, 60 en une chaîne de caractères"""
    dico = {'cinquante': 50, 'quarante': 40, 'onze': 11, 'huit': 8, 'six': 6, \
            'quinze': 15, 'trente': 30, 'douze': 12, 'cinq': 5, 'deux': 2, \
            'quatorze': 14, 'neuf': 9, 'soixante': 60, 'quatre': 4, \
            'zéro': 0, 'treize': 13, 'trois': 3, 'seize': 16, \
            'vingt': 20, 'un': 1, 'dix': 10, 'sept': 7}
    inv = {}
    for k,v in dico.iteritems () : inv [v] = k
    inv [70] = "soixante-dix"
    inv [80] = "quatre-vingt"
    inv [90] = "quatre-vingt-dix"
    return inv [x]
    
def ecrit_dizaine(x):
    """convertit un nombre entre 0 et 99 sous sa forme littérale"""

    if x <= 16:
        return mot_valeur (x)

    s       = ""
    dizaine = x / 10
    unite   = x % 10
    s = mot_valeur (dizaine*10)
    s += " "
    s += mot_valeur (unite)
    return s
    
for i in xrange(0,100):
    s = ecrit_dizaine (i)
    j = lire_dizaine (s)
    if i != j :
        print "erreur ", i, " != ", j, " : ", s