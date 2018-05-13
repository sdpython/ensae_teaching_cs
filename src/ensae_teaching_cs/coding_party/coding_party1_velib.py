# -*- coding: utf-8 -*-
"""
@file
@brief Une solution au problème proposée :
:ref:`Reconstruction de trajectoire velib <l-codingparty1>`
"""
import os
import random
import pandas
from pyensae import download_data
from manydataapi.velib import DataCollectJCDecaux as DataVelibCollect
from pyquickhelper.loghelper import str2datetime


def get_data(whereto):
    """
    récupère les données

    @param      whereto     destination
    """
    download_data('velib_synthetique.zip', website='xdtd', whereTo=whereto)
    download_data('besancon.df.txt.zip', website='xdtd', whereTo=whereto)


def enumerate_events(df):
    """
    Construit la liste des événements (vélo réposé ou retiré).

    @param      df      DataFrame
    @return             énumère événéments (ierator) ("file", "collect_date", "name", "lat", "lng", +1 ou -1)
    """
    df = df[["file", "collect_date", "name", "lat", "lng",
             "available_bike_stands", "available_bikes"]]
    df = df.sort_values(["name", "file", "collect_date"])
    lastrow = None
    for row in df.values:
        if lastrow is not None and lastrow[2] == row[2]:
            d1 = row[-2] - lastrow[-2]  # nombre de place en plus
            d2 = row[-1] - lastrow[-1]  # nombre de vélos en plus
            if d1 != 0:
                step = d1 // abs(d1)
                for i in range(1, abs(d1) + 1):
                    yield tuple(row[:-2]) + (step,)
            elif d2 != 0:
                step = d2 // abs(d2)
                for i in range(1, abs(d2) + 1):
                    yield tuple(row[:-2]) + (step,)

        lastrow = row


class ParemetreCoutTrajet:

    """
    Regroupe l'ensembles des paramètres pour le calcul de la distance
    associé à un appariement.
    """

    def __init__(self, max_speed=50,
                 high_speed=25,
                 low_speed=5,
                 high_time=0.75,
                 low_time=0.1):
        """
        @param      max_speed       au-delà, c'est une vitesse impossible
        @param      high_speed      au-delà, c'est la vitesse d'un cycliste
        @param      low_speed       en-deça, il vaut mieux marcher
        @param      high_time       au-delà, c'est une randonnée
        @param      low_time        en-deça, pourquoi un vélo
        """
        self.max_speed = max_speed
        self.high_speed = high_speed
        self.low_speed = low_speed
        self.high_time = high_time
        self.low_time = low_time

    def __str__(self):
        """
        usuel
        """
        return str(self.values)

    @property
    def values(self):
        """
        Retourne les valeurs dans un dictionnaire.
        """
        return {k: getattr(self, k) for k in self.__dict__ if "time" in k or "speed" in k}

    def cost(self, dh, dt, v):
        """
        Retourne un coût, plus il est bas,
        plus de déplacement est probable.

        @param      dh      distance
        @param      dt      durée
        @param      v       vitesse
        @return             coût
        """
        c = 0
        if v > self.max_speed:
            c += 1e3
        if v > self.high_speed:
            c += (v - self.high_speed) ** 2 * 10
        if v < self.low_speed:
            c += (v - self.low_speed) ** 2 * 100
        dt = dt.total_seconds() / 3600
        if dt > self.high_time:
            c += (dt - self.high_time) ** 2 * 10
        if dt < self.low_time:
            c += (dt - self.low_time) ** 2 * 10
        return c


def vitesse(c, d, params):
    """
    Calcule la vitesse d'un déplacement.

    @param      c       tuple ("file", "collect_date", "name", "lat", "lng", +1 ou -1)
    @param      d       tuple ("file", "collect_date", "name", "lat", "lng", +1 ou -1)
    @param      params  ParemetreCoutTrajet
    @return             vitesse, cout

    La fonction retourne une valeur aberrante si le temps entre les deux événements est négatifs.
    C'est une configuration impossible : on ne peut reposer un vélo avant de l'avoir retiré.
    La valeur aberrante est ``1e8``.

    Il reste un cas pour lequel, je ne sais pas encore quelle valeur donner :
    il s'agit des demi-appariements : un vélo rétiré mais jamais reposé et réciproquement.
    """
    if c[0] is None or d[0] is None:
        # cas des vélos perdus
        if c[0] is None:
            if d[0] is None:
                return None
            else:
                return 0.0, 0.0   # je ne sais pas trop quoi mettre
        else:
            return 0.0, 0.0  # je ne sais pas trop quoi mettre
    else:
        lat1, lng1 = c[3], c[4]
        lat2, lng2 = d[3], d[4]
        dh = DataVelibCollect.distance_haversine(lat1, lng1, lat2, lng2)
        dt = d[1] - c[1]
        if dt.total_seconds() <= 0:
            return 1e8, 1e8  # infini
        v = dh / (dt.total_seconds() / 3600)
        cost = params.cost(dh, dt, v)
        return v, cost


def distance(positif, negatif, app, params):
    """
    Calculs une distance pour un appariement conçu ici comme
    la variance de la vitesse de chaque déplacement + la somme
    des coûts de chaque appariement retourné par la fonction @see fn vitesse.

    @param      positif     vélos pris (ou l'inverse)
    @param      negatif     vélos remis (ou l'inverse)
    @param      app         appariement (list de tuple (i,j))
    @param      params      ParemetreCoutTrajet
    @return                 tuple:
                                - vitesse moyenne (sans appariements négatifs)
                                - distance
                                - vitesse moyenne avec
                                - nombre d'appariements négatifs
    """
    val = []
    nb_max = []
    cost = 0
    for i, j in app:
        p = positif[i]
        n = negatif[j]
        v, d = vitesse(p, n, params)
        cost += d
        if v > params.max_speed:
            nb_max.append(v)
        if v is not None:
            val.append(v)

    mean = sum(val) / len(val)
    # on enlève les appariements négatifs
    cor = [v_ for v_ in val if v < 1e8]
    mean_cor = sum(cor) / len(cor)
    dev = sum((x - mean) ** 2 for x in val) / len(val)
    return mean_cor,  \
        cost + dev ** 0.5 * (1 + len(nb_max)),  \
        mean,  \
        len(val) - len(cor)


def appariement(events, iter=1000, params=ParemetreCoutTrajet(), fLOG=print):
    """
    On veut apparier les événemens -1 aux événemens +1.
    On s'attend aux colonnes suivantes:
    *"file"*, *"collect_date"*, *"name"*, *"lat"*, *"lng"*, *+1* ou *-1*.
    La fonction part des deux séries d'évéments rangés par ordre croissant,
    puis il permute deux appariements tant que cela diminue l'erreur d'appariement.

    @param      events      list d'événements produits par la fonction
                            @see fn enumerate_events
    @param      iter        nombre d'itérations
    @param      params      ParemetreCoutTrajet
    @param      fLOG        logging function
    @return                 tuple (mindist, moyenne, appariement, positif, negatif)
    """
    events = sorted(events)

    # on élimine tous les -1 du début (forcément des vélos pris avant la
    # période d'étude)
    lasti = 0
    for i, ev in enumerate(events):
        lasti = i
        if ev[-1] == 1:
            break
    i = lasti
    if i > 0:
        del events[:i]

    # pareil de l'autre côté
    for i, ev in enumerate(reversed(events)):
        if ev[-1] == -1:
            break
    if i > 0:
        del events[len(events) - i:]

    default = (None, None, None, 0, 0, 0)

    positif = [e for e in events if e[-1] > 0]
    negatif = [e for e in events if e[-1] < 0]

    # on veut autant d'événements de chaque côté
    while len(positif) > len(negatif):
        negatif.append(default)
    while len(positif) < len(negatif):
        positif.append(default)

    appariement_ = [(i, i) for i in range(0, len(positif))]
    vit, mindist, vitav, nbneg = distance(
        positif, negatif, appariement_, params)
    nbchange = 0

    for it in range(0, iter):
        if it % 10 == 0:
            fLOG("iteration ", it, ": app-", nbneg, "/", len(appariement_),
                 "min", mindist, "vitesse ", vit, " nbchange", nbchange)
            nbchange = 0
        for _ in range(0, len(appariement_)):
            i = random.randint(0, len(appariement_) - 1)
            j = random.randint(0, len(appariement_) - 1)
            if i == j:
                continue
            ki, kj = appariement_[i], appariement_[j]
            appariement_[i] = (ki[0], kj[1])
            appariement_[j] = (kj[0], ki[1])
            v, dist, vt, nbneg = distance(
                positif, negatif, appariement_, params)
            if dist < mindist:
                mindist = dist
                vit = v
                nbchange += 1
            else:
                appariement_[i], appariement_[j] = ki, kj

    moyenne = distance(positif, negatif, appariement_, params)[0]

    # def dd(a, b):
    #     try:
    #         return b - a
    #     except Exception:
    #         return None
    # for a in appariement_:
    #    fLOG(a,dd(positif [a[0]][1],negatif[a[1]][1]), vitesse(positif [a[0]], negatif[a[1]], params), positif [a[0]],"-->",negatif[a[1]])

    return mindist, moyenne, appariement_, positif, negatif


def distance_path(dfp):
    """
    Calcule la vitesse moyenne lorsque le chemin est connu.

    @param  dfp     liste des chemins
    @return         moyenne, stddev
    """
    dfp = dfp.copy()
    dfp["speed"] = dfp["dist"] / dfp["hours"]
    dfp["dist"] = dfp.apply(
        lambda r: DataVelibCollect.distance_haversine(
            r["lat0"],
            r["lng0"],
            r["lat1"],
            r["lng1"]),
        axis=1)
    mean_ = sum(dfp["speed"]) / len(dfp)
    std_ = sum((x - mean_) ** 2 for x in dfp["speed"]) / len(dfp)
    return mean_, std_ ** 0.5


if __name__ == "__main__":

    def main_velib():
        dest = r"c:\temp\codpart1"
        if not os.path.exists(dest):
            os.makedirs(dest)
        get_data(dest)

        # récupère les données
        jeu = os.path.join(dest, "besancon.df.txt")
        jeu = os.path.join(dest, "out_simul_bike_nb1_sp10_data.txt")
        df = pandas.read_csv(jeu, sep="\t", encoding="utf8")
        # conversion des dates
        df["collect_date"] = df.apply(
            lambda r: str2datetime(
                r["collect_date"]),
            axis=1)
        # print(df.head())

        # on regarde s'il existe le fichier des trajectoires
        path = jeu.replace("_data.", "_path.")
        if path != jeu and os.path.exists(path):
            dfp = pandas.read_csv(path, sep="\t")
            dfp = dfp[dfp["beginend"] == "end"]
            mean, std = distance_path(dfp)
            print("expected: vitesse moyenne ", mean, " stddev ", std)

        # on calcule les événements (1 vélo apparu, 1 vélo disparu)
        events = list(sorted(enumerate_events(df)))

        params = ParemetreCoutTrajet()
        print(params)
        mindist, moyenne, appariement_, positif, negatif = appariement(
            events, iter=200, params=params)
        print("vitesse moyenne", moyenne)

    main_velib()
