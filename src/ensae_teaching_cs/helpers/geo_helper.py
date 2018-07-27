# -*- coding: utf-8 -*-
"""
@file
@brief Helpers about longitude, latitude.
"""
import math


def lambert93_to_WGPS(lambertE, lambertN):
    """
    Converts coordinates given in
    `Lambert 93 <https://fr.wikipedia.org/wiki/Projection_conique_conforme_de_Lambert>`_
    system, this system is used by `IGN <http://http://professionnels.ign.fr/>`_
    and their `GEOFLA <http://professionnels.ign.fr/geofla>`_ file format.

    @param      lambertE        east
    @param      lambertW        west
    @return                     longitude, latitude

    The function is inspired from
    `lam93toLatLon.py <https://gist.github.com/flire/0a305eeec77bc84a73af8ddc8f9ec043>`_.

    .. faqref::
        :tag: geo
        :title: Les fichiers GEOFLA ne contiennent pas de longitude, latitude ?

        Les coordonnées contenues dans les fichiers `GEOFLA <http://professionnels.ign.fr/geofla>`_
        ne sont pas toujours des longitudes, latitudes mais des coordonnées exprimées dans un système
        de projection conique `Lambert 93 <https://fr.wikipedia.org/wiki/Projection_conique_conforme_de_Lambert>`_.
        Il faut convertir les coordonnées avant de pouvoir tracer la carte ou changer la projection
        utilisée par :epkg:`cartopy` :
        `Lambert Conformal Projection <https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html#lambertconformal>`_.
    """
    class constantes:
        GRS80E = 0.081819191042816
        LONG_0 = 3
        XS = 700000
        YS = 12655612.0499
        n = 0.7256077650532670
        C = 11754255.4261

    delX = lambertE - constantes.XS
    delY = lambertN - constantes.YS
    gamma = math.atan(-delX / delY)
    R = math.sqrt(delX * delX + delY * delY)
    latiso = math.log(constantes.C / R) / constantes.n
    sinPhiit0 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * math.sin(1)))
    sinPhiit1 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit0))
    sinPhiit2 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit1))
    sinPhiit3 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit2))
    sinPhiit4 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit3))
    sinPhiit5 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit4))
    sinPhiit6 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit5))

    longRad = math.asin(sinPhiit6)
    latRad = gamma / constantes.n + constantes.LONG_0 / 180 * math.pi

    longitude = latRad / math.pi * 180
    latitude = longRad / math.pi * 180

    return longitude, latitude
