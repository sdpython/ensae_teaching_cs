# coding: cp1252
# la première ligne permet d'insérer des accents dans les commentaires
import random
rejouer   = True
somme     = 0
nb_partie = 0
while rejouer :
    hasard     = rd.randint(1,20)
    nb_partie += 1

    devine = 0
    coup   = 0
    while devine != hasard :
        coup += 1
        devine = raw_input ("Entrer un nombre ?")
        devine = float (devine)     # conversion en réel
        if (devine > hasard) :
            print "Le nombre entré est trop grand."
        if (devine < hasard) :
            print "Le nombre entré est trop petit."

    somme += coup
    print "Vous avez trouvé en " , coup, " coups."
    print "Vous avez déjà joué ", somme, " coups et ", nb_partie, " parties."
    rejouer = raw_input("Voulez-vous rejouer ?")
    rejouer = rejouer == "oui" or rejouer == "o" or rejouer == "1"

moyenne = float (somme) / nb_partie  # conversion en réel, sinon la division est entière
print "Nombre de coups moyen par parties : " , moyenne