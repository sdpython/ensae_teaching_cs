#-*-  coding: utf-8 -*-
"""
@file
@brief implémentation du modèle d'illumination de Phong
"""
from .image_synthese_scene import Scene
from .image_synthese_base import Couleur


class ScenePhong (Scene):
    """définit une scène et utilise le modèle d'illumination de Phong
    pour construire l'image de synthèse"""

    def __init__(self, repere, alpha, x, y,
                 ka=0.1,
                 kb=0.8,
                 kc=0.3,
                 reflet=6,
                 fond=Couleur(200, 200, 200)):
        """définit la position de l'oeil, l'angle d'ouverture,
        et la taille de l'écran"""
        Scene.__init__(self, repere, alpha, x, y)
        self.ka, self.kb, self.kc = ka, kb, kc
        self.reflet = reflet
        self.fond = fond
        self.constante = float(1)

    def __str__(self):
        """affichage"""
        s = Scene.__str__(self)
        s += "ka = %1.3f   kb = %1.3f   kc = %1.3f\n" % (
            self.ka, self.kb, self.kc)
        s += "reflet " + str(self.reflet) + "\n"
        s += "couleur du fond " + str(self.fond) + "\n"
        return s

    def couleur_fond(self):
        """retourne la couleur du fond"""
        return self.fond * self.ka

    def modele_illumination(self, rayon, p, obj, source):
        """calcule la couleur pour un rayon donné, un point p, un objet obj,
        et une source de lumière source"""
        n = obj.normale(p, rayon).renorme()
        vr = rayon.direction.renorme()
        vr *= float(-1)
        vs = source.origine - p
        vs = vs.renorme()
        bi = vs + vr
        bi = bi.renorme()

        # premier terme
        cos = n.scalaire(vs)
        couleur = source.couleur.produit_terme(
            obj.couleur_point(p)) * (cos * self.kb)

        # second terme : reflet
        cos = n.scalaire(bi) ** self.reflet
        couleur += source.couleur.produit_terme(
            source.couleur) * (cos * self.kc)
        couleur = couleur.produit_terme(rayon.couleur)

        return couleur
