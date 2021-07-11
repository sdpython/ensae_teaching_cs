# coding: utf-8
"""
@file
@brief Shapefiles data.
"""
import os
import pandas
from pyquickhelper.filehelper import get_url_content_timeout, unzip_files


def data_shape_files(name, cache=".", load=True):
    """
    Downloads shape files.

    :param name: name of the shape file (see below)
    :param cache: cache folder
    :param load: loads the shape files, the function relies on
        :epkg:`geopandas`
    :return: shape files

    List of availables shape files:
    * `'depfr2018'`: see `Contours des départements français issus d'OpenStreetMap
      <https://www.data.gouv.fr/en/datasets/contours-des-departements-francais-issus-d-openstreetmap/>`_
    """
    if name == 'depfr2018':
        url = 'https://github.com/sdpython/data/raw/master/shapefiles/france_departements/departements-20180101-shp.zip'
        dest = os.path.join(cache, 'departements-20180101-shp.zip')
        if not os.path.exists(dest):
            get_url_content_timeout(url, output=dest, encoding=None)
        res = unzip_files(dest, where_to=cache)
        shp = [name for name in res if name.endswith('.shp')]
        if len(shp) == 0:
            raise FileNotFoundError(  # pragma: no cover
                "Unable to find shp file in '{}'.".format(cache))
        import geopandas
        df = geopandas.read_file(shp[0])
        df['centroid'] = df['geometry'].apply(lambda r: r.centroid)
        df['DEPLONG'] = df['centroid'].apply(lambda r: r.x)
        df['DEPLAT'] = df['centroid'].apply(lambda r: r.y)
        return df
    raise ValueError(
        "Unpexpected value for shape files: '{}'.".format(name))


def load_french_departments():
    """
    Loads a dataframe with the list of French
    departments and the center of each.
    """
    this = os.path.abspath(os.path.dirname(__file__))
    name = os.path.join(this, "data_shp", "departement_french_2018.csv")
    return pandas.read_csv(name)
