# coding: latin-1
####################################
# exercice 1
####################################

# question 1
def numero(jour, mois, duree=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]):
    s = 0
    for i in range(0, mois - 1):
        s += duree[i]
    s += jour - 1
    return s + 1

# question 2


def conversion_liste(li):
    res = []
    for jour, mois in s:
        res.append(numero(jour, mois))
    # pareil que
    # for i in range (0, len (s)) : res.append ( numero (s [i][0], s [i][1]))
    return res


def ecart(num):
    res = []
    for i in range(1, len(num)):
        d = num[i] - num[i - 1]
        res.append(d)
    return res


s = [(1, 1), (9, 4), (1, 5), (8, 5), (17, 5), (4, 6), (14, 7),
     (15, 8), (1, 11), (11, 11), (25, 12)]
r = conversion_liste(s)
ec = ecart(r)

# question 3
pos = ec.index(max(ec))
print "position de l'écart le plus grand ", pos
print "jour ", s[pos], " --> ", s[pos + 1]

####################################
# exercice 2
####################################

# question 4


class Date:
    def __init__(self, jour, mois):
        self.jour = jour
        self.mois = mois
        self.duree = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # question 5
    def numero(self):
        s = 0
        for i in range(0, self.mois - 1):
            s += self.duree[i]
        s += self.jour - 1
        return s + 1

    # question 6
    def difference(self, autre):
        return self.numero() - autre.numero()


def conversion_date(s):
    res = []
    for jour, mois in s:
        res.append(Date(jour, mois))
    return res


def ecart_date(date):
    ec = []
    for i in range(1, len(date)):
        ec.append(date[i].difference(date[i - 1]))
    return ec


# question 7
s = [(1, 1), (9, 4), (1, 5), (8, 5), (17, 5), (4, 6),
     (14, 7), (15, 8), (1, 11), (11, 11), (25, 12)]

r = conversion_date(s)
ec = ecart_date(r)
pos = ec.index(max(ec))
print "position de l'ecart le plus grand ", pos
print "jour ", s[pos], " --> ", s[pos + 1]

# question 8
"""
La conversion en Date est faite une fois pour les dates (1,1) et (25,12)
et 2 fois pour les autres en effet, la méthode difference effectue
la conversion en numéros des dates self et autre
la fonction ecart_date calcule date [i].difference ( date [i-1] ) et
                                         date [i+1].difference ( date [i] )
            --> la date [i] est convertie 2 fois
"""

# question 9
"""
On peut par exemple stocker la conversion en numéro
dans le constructeur comme suit :
"""


class Date:
    def __init__(self, jour, mois):
        self.jour = jour
        self.mois = mois
        self.duree = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.num = self.numero()

    # question 5
    def numero(self):
        s = 0
        for i in range(0, self.mois - 1):
            s += self.duree[i]
        s += self.jour - 1
        return s + 1

    # question 6
    def difference(self, autre):
        return self.num - autre.num


r = conversion_date(s)
ec = ecart_date(r)
pos = ec.index(max(ec))
print "position de l'écart le plus grand ", pos
print "jour ", s[pos], " --> ", s[pos + 1]
