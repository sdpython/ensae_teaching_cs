#coding:latin-1

########## Question 1 ################

nom_prenom= "illotevtelo ChMa"

i=3
valeur= ord (nom_prenom [i])
print valeur
print ord('p')

########## Question 2 ################

r=0
for i in xrange(0,len(nom_prenom)):
	r += ord( nom_prenom [i] )
print r

########## Question 3 ################

def somme_caractere (nom_prenom):
	r=0
	for i in xrange(0,len(nom_prenom)):
		r += ord( nom_prenom [i] )
	return r
	
print somme_caractere (nom_prenom)

########## Question 4 ################

s = somme_caractere(nom_prenom) % 200
url = "http://www.xavierdupre.fr/enseignement/tutoriels_data/tutoriel_%d.py" % s
print url