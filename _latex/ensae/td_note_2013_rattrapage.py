# coding:latin-1
import re


def lit_fichier(file):
    """
    0 Séance 	
    1 Référence	
    2 Entité dépositaire	
    3 Elu dépositaire	
    4 Objet	
    5 Type	
    6 Rapporteur
    """
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    lines = [_ for _ in lines if len(_) > 0]
    lines = [_.split("\t") for _ in lines][1:]
    lines = [(_[0], _[4]) for _ in lines if len(_) > 5]
    return lines


def extrait_montant(objet):
    exp = re.compile("[ (]([0-9.,]+) {0,3}euros")
    res = exp.search(objet)
    if res:
        montant = res.groups()[0]
        montant = montant.replace(".", "").replace(",", ".")
        return montant
    else:
        #print ("problème ", objet)
        return None


def extrait_assoc(objet):
    exp = re.compile("association(.*)[(]([0-9]+e)[)]")
    res = exp.search(objet)
    if res:
        return res.groups()
    else:
        #print ("problème ", objet)
        return None


def extrait_date(date):
    exp = re.compile("([0-9]{4})")
    res = exp.search(date)
    if res:
        annee = res.groups()[0]
        return annee
    else:
        print("problème ", date)
        return None


def compte_annee(lines):
    compte = {}
    for a, b, c, d in lines:
        a = d[0] if d != None else None
        compte[a] = compte.get(a, 0) + b
    return compte


if __name__ == "__main__":
    # données récupérées ici: http://opendata.paris.fr/opendata/jsp/site/Portal.jsp?document_id=154&portlet_id=102
    file = "td_note_2013_ordre_du_jour_conseil_municipal.txt"

    lines = lit_fichier(file)
    print(len(lines))
    for _ in lines[:10]:
        print(_)

    montants = []
    erreurs = []
    for line in lines:
        date = extrait_date(line[0])

        err = 0
        if date == None:
            date = line[0]
            err += 1
        else:
            date = int(date)

        text = line[1]
        montant = extrait_montant(text)
        if montant != None:
            montant = float(montant)
        else:
            err += 1

        text = text.lower()
        asso = extrait_assoc(text)
        cl = ""
        if "association" in text:
            cl += " asso"
        if "subvention" in text:
            cl += " subv"
        if "signature" in text:
            cl += " sign"

        if err > 0:
            erreurs.append((date, line[1], cl, asso))
        else:
            montants.append((date, montant, cl, asso))

    somme = sum([_[1] for _ in montants])
    print("nb montants ", len(montants), " somme ", somme)
    print("nb erreurs ", len(erreurs))

    compte = compte_annee(montants)
    for k, v in compte.items():
        print(k, "\t", v)
