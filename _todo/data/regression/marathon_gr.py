# coding:latin-1
import marathon
# cette première ligne suppose que le programme de la la première question
# a été enregistrée dans un fichier marathon.py
# il n'y a alors pas besoin de le recopier ici
import matplotlib
import matplotlib.pyplot as plt


def dessin(donnees, titre="titre"):
    x = [d[0] for d in donnees]
    y = [d[1] for d in donnees]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'o')
    ax.set_title(titre)
    plt.show()

if __name__ == "__main__":
    matrice = marathon.charge_donnees()
    mat = [(m[1], m[3]) for m in matrice]
    dessin(mat)
