# coding:latin-1
import discours
import re
textes = discours.charge_discours()
accent = {'à': 'a', 'â': 'a',  'ä': 'a',
                    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
                    'î': 'i', 'ï': 'i',
                    'ù': 'u', 'û': 'u', 'ü': 'u',
                    'ô': 'o', 'ö': 'o',
          }


def somme_textes(textes, subset=None):
    t = ""
    if subset != None:
        for v in subset:
            t += textes[v]
    else:
        for v in textes.values():
            t += v
    return t


def pas_daccent(mot):
    res = ""
    for c in mot:
        c = c.lower()
        res += accent.get(c, c)
    return res


def compte_mots(mots):
    d = {}
    for mot in mots:
        if mot in d:
            d[mot] += 1
        else:
            d[mot] = 1
    return d


def mot_tries(d):
    l = [(n, m) for m, n in d.iteritems()]
    l.sort(reverse=True)
    return l


def decoupe_mot(texte):
    return texte.split()


def decoupe_mot2(texte):
    exp = re.compile("\\w{2,}", re.IGNORECASE)
    return exp.findall(texte)


def trouver_expression(texte):
    exp = re.compile("((in)?securite.*?[.])", re.IGNORECASE)
    return exp.findall(texte)

somme = somme_textes(textes)
somme = pas_daccent(somme)


res = mot_tries(compte_mots(decoupe_mot(somme)))
for h in res[:25]:
    print h
print "*"
res = mot_tries(compte_mots(decoupe_mot2(somme)))
for h in res[:25]:
    print h

textes = discours.charge_discours()
for t in textes:
    textes[t] = pas_daccent(textes[t])
for t in textes:
    for _ in trouver_expression(textes[t]):
        print t, _
