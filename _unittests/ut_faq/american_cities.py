import os
import pandas
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from src.ensae_teaching_cs.faq.faq_matplotlib import graph_cities
from src.ensae_teaching_cs.special import tsp_kruskal_algorithm, distance_haversine


def american_cities(nb_cities, fLOG, temp):
    def haversine(p1, p2):
        return distance_haversine(p1[0], p1[1], p2[0], p2[1])
        
    fix_tkinter_issues_virtualenv()
    import matplotlib.pyplot as plt

    data = os.path.join(temp, "..", "data", "american_cities.txt")
    df = pandas.read_csv(data)
    df["Longitude"] = -df["Longitude"]
    df = df[df.Latitude < 52]
    df = df[df.Longitude > -130].copy()
    fLOG(df.columns)
    df = df.dropna()

    if nb_cities > 0:
        df = df[:nb_cities].copy()

    fLOG(df.shape)
    # df["City"] = df["City"].apply(lambda v: filter.get(v, ""))
    points = [(row[1], row[2], row[3])
              for row in df.itertuples(index=False)]
    fLOG("number of cities:", len(points))
    trip = tsp_kruskal_algorithm(
        points, distance=haversine, fLOG=fLOG, max_iter=10)

    # trip
    dftrip = pandas.DataFrame(
        trip, columns=["Latitude", "Longitude", "City"])
    save = os.path.join(temp, "trip.txt")
    dftrip.to_csv(save, sep="\t", index=False)

    # graph
    for i in range(0, dftrip.shape[0]):
        if i % 10 != 0:
            dftrip.ix[i, "City"] = ""
    fig, ax = plt.subplots(figsize=(32, 32))
    ax = graph_cities(dftrip, ax=ax, markersize=3, linked=True, fLOG=fLOG,
                      fontcolor="red", fontsize='16', loop=True)
    assert ax is not None
    img = os.path.join(temp, "img.png")
    fig.savefig(img)
    assert os.path.exists(img)
    plt.close('all')
    fLOG("end")
