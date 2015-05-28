

.. blogpost::
    :title: Chargement des images avec pygame
    :keywords: pygame, os
    :date: 2015-05-28
    :categories: programmation, pygame, fichier

    Je vois chaque année des bouts de code qui ressemble à ceci ::

        sept_trefle_verticale = pygame.image.load("sept_trefle_verticale.jpg").convert()
        sept_trefle_horizontale = pygame.image.load("sept_trefle_horizontale.jpg").convert()
        sept_pique_verticale = pygame.image.load("sept_pique_verticale.jpg").convert()
        sept_pique_horizontale = pygame.image.load("sept_pique_horizontale.jpg").convert()
        sept_coeur_verticale = pygame.image.load("sept_coeur_verticale.jpg").convert()
        sept_coeur_horizontale = pygame.image.load("sept_coeur_horizontale.jpg").convert()
        sept_carreau_verticale = pygame.image.load("sept_carreau_verticale.jpg").convert()
        # ...

    Il y a quand même beaucoup plus simple pour charger des images que 
    d'écrire une ligne pour chacun d'entre elles. L'exemple suivant
    charge toutes les images du répertoire ``images``
    tout dans un dictionnaire ::

        import os
        res = {}
        for image in os.listdir("images"):
            filename = os.path.join("images", image)
            name = os.path.splitext(image)[0]
            res[name] = pygame.image.load(filename).convert()

    Plus simple et aussi plus sûr car on n'a pas l'occasion de se tromper
    sur un nom de fichier.