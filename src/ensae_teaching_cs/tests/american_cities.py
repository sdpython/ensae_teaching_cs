"""
@file
@brief Function to test others functionalities
"""
import os
import pandas
from pyquickhelper.loghelper import fLOG
from ..faq.faq_matplotlib import graph_cities
from ..special import tsp_kruskal_algorithm, distance_haversine


def american_cities(df_or_filename, nb_cities=-1, img=None, fLOG=fLOG):
    """
    compute the TSP for american cities

    @param      df_or_filename  dataframe
    @param      nb_cities       number of cities to keep
    @param      img             image to produce
    @param      fLOG            logging function
    @return                     dataframe (results)
    """
    def haversine(p1, p2):
        return distance_haversine(p1[0], p1[1], p2[0], p2[1])

    if isinstance(df_or_filename, str):
        df = pandas.read_csv(df_or_filename)
    else:
        df = df_or_filename
    df["Longitude"] = -df["Longitude"]
    df = df[df.Latitude < 52]
    df = df[df.Longitude > -130].copy()
    fLOG(df.columns)
    df = df.dropna()

    if nb_cities > 0:
        df = df[:nb_cities].copy()

    fLOG(df.shape)
    points = [(row[1], row[2], row[3])
              for row in df.itertuples(index=False)]
    fLOG("number of cities:", len(points))
    trip = tsp_kruskal_algorithm(
        points, distance=haversine, fLOG=fLOG, max_iter=10)

    # trip
    dftrip = pandas.DataFrame(
        trip, columns=["Latitude", "Longitude", "City"])

    # graph
    for i in range(0, dftrip.shape[0]):
        if i % 10 != 0:
            dftrip.loc[i, "City"] = ""

    if img is not None:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(32, 32))
        ax = graph_cities(dftrip, ax=ax, markersize=3, linked=True, fLOG=fLOG,
                          fontcolor="red", fontsize='16', loop=True)
        assert ax is not None
        fig.savefig(img)
        assert os.path.exists(img)
        plt.close('all')
        fLOG("end")
    return dftrip
