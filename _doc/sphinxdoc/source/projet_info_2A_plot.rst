
.. _l-projinfo2a-plot:

2A - Partager un graphe via un module python
============================================

L'objectif de ce projet est de construire un module python
pour partager soit une fonction qui représente des données
avec :epkg:`matplotlib`, soit un nouveau modèle de
machine learning qui suit l'API de :epkg:`scikit-learn`.

.. contents::
    :local:

Ce projet doit être rendu le jour du dernier TD.
Il doit être effectué par groupe de 3 à 5 personnes.

Graphes
+++++++

Il faut imaginer un graphe qui permet de comprendre
l'évolution temporelle d'une valeur numérique entre deux années.

::

    def plot_geo_time_value(x, y, name, value, hue, year, ax=None, **kwargs):
        """
        Visualise l'évolution temporelle d'une donnée numérique
        géolocalisée.

        :param x: longitudes (vecteur)
        :param y: latitudes (vecteur)
        :param name: nom des lieux  (vecteur)
        :param value: valeur numérique à représenter (vecteur)
        :param hue: sens de la valeur numérique (:math:`CO_2`, Ammoniac, ...)
        :param year: année (vecteur)
        :param ax: axes
        :param kwargs: paramètres additionnels
        """

Le module peut implémenter plusieurs fonctions
pour plusieurs graphes.
C'est à vous de définir ce que vous souhaitez représenter.
On peut choisir de représenter des pourcentages plutôt
que des valeurs absolues, ce peut être un graphe sur
des données agrégées plutôt qu'une carte. Les fonctions seront
testées sur les deux jeux de données ci-dessous.

Vous trouvez un exemple qui crée un module python pour
une fonction qui crée un graphe avec :epkg:`matplotlib`
sur *github* : `td2a_plotting
<https://github.com/sdpython/td2a_plotting>`_.
La documentation peut être compilée avec :epkg:`sphinx`
et donne quelque chose comme ceci :
`td2a_plotting: simple plotting module
<http://www.xavierdupre.fr/app/td2a_plotting/helpsphinx/index.html>`_.

Modèle de machine learning
++++++++++++++++++++++++++

Il s'agit d'implémenter un modèle de machine learning
suivant l'API de :epkg:`scikit-learn` et de le partager sous
la forme d'un module. Voici un exemple qui implémente la
régression quantile : `QuantileLinearRegression
<https://github.com/sdpython/mlinsights/blob/master/mlinsights/mlmodel/quantile_regression.py>`_
(`documentation de QuantileLinearRegression
<http://www.xavierdupre.fr/app/mlinsights/helpsphinx/mlinsights/mlmodel/quantile_regression.html>`_),
et un exemple d'utilisation dans un `notebook sur la régression quantile
<http://www.xavierdupre.fr/app/mlinsights/helpsphinx/notebooks/quantile_regression.html>`_.
Le même exemple sur github `td2a_plotting
<https://github.com/sdpython/td2a_plotting>`_
pourra être utilisé pour réaliser le module.

Le modèle n'est pas nécessairement un nouveau modèle mais
aussi un assemblage de modèles existants. Quelques exemples :
`ClassifierAfterKMeans <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/mlinsights/mlmodel/classification_kmeans.html>`_,
`IntervalRegressor <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/mlinsights/mlmodel/interval_regressor.html>`_,
`PiecewiseRegressor <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/mlinsights/mlmodel/piecewise_estimator.html>`_...

Données suggérées
+++++++++++++++++

**Jeu 1 :** projets vers financés par l'`ADEME <https://www.ademe.fr/>`_

* `Deal flow des projets verts : projets notifiés et financés en 2018
  <https://data.ademe.fr/datasets/jeu-de-donnees-deal-flow-2018>`_
* `Deal flow des projets verts - Projets financés en 2019 et investissements envisagés en 2019
  <https://data.ademe.fr/datasets/jeu-de-donnees-deal-flow-2019>`_

Le notebook :ref:`dealflowespacevertrst` effectue les premiers pas avec de jeu de données.

**Jeu 2 :** données sur les émissions polluantes

* `Données sur les émissions polluantes (IREP)
  <http://www.georisques.gouv.fr/dossiers/irep/telechargement>`_

Ces données sont produites par le `BRGM <http://www.georisques.gouv.fr/>`_.
Le même lien permet de télécharger les données de plusieurs années.
Ce lien est aussi accessible via `Registre Français des émissions polluantes
<https://www.data.gouv.fr/en/datasets/registre-francais-des-emissions-polluantes/>`_.
Les fichiers ZIP incluent plusieurs fichiers dont :

``emissions.csv``

::

    Identifiant,Nom_Etablissement,Annee_Emission,Milieu,Polluant,quantite,unite
    033.00469,"Solvay Operations France, tavaux",2017,Air,ComposÃ©s organiques volatils non mÃ©thaniques (COVNM),45500,kg/an
    033.00469,"Solvay Operations France, tavaux",2017,Air,Hydrochlorofluorocarbures (HCFC),3640,kg/an
    033.00469,"Solvay Operations France, tavaux",2017,Air,Hydroflurocarbures (HFC),3910,kg/an
    033.00469,"Solvay Operations France, tavaux",2017,Air,Oxydes de soufre (SOx/SO2),173000,kg/an
    ...

``Prelevements.csv``

::

    Identifiant,Nom_Etablissement,Numero_SIRET,Adresse,Code_Postal,Commune,Departement,Region,Coordonnees_X,Coordonnees_Y,Code_APE,Libelle_APE,code_eprtr,libelle_eprtr
    068.11539,CarriÃ¨res BERNADETS - ISDI,54608016900115,,31420,AURIGNAC,HAUTE-GARONNE,OCCITANIE,481659,1802490,0812Z,"Exploitation de graviÃ¨res et sabliÃ¨res, extraction d'argiles et de kaolin",,
    061.10406,REVAGA,51058711600037,,69390,MILLERY,RHONE,AUVERGNE-RHONE-ALPES,790678,2073093,3811Z,Collecte des dÃ©chets non dangereux,,
    124.00155,SATE,42976802100025,,90150,FONTAINE,TERRITOIRE-DE-BELFORT,BOURGOGNE-FRANCHE-COMTE,949818,2305514,2751Z,Fabrication d'appareils Ã©lectromÃ©nagers,,
    ...

Le notebook :ref:`dataireprst` effectue les premiers pas avec de jeu de données.
