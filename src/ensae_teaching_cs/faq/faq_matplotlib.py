# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `matplotlib <http://matplotlib.org/>`_.
"""
import numpy


def graph_style(style='ggplot'):
    """
    Changes :epkg:`matplotlib` style.

    @param      style       style

    .. faqref::
        :tag: matplotlib
        :title: Changer le style de graphique pour ggplot

        .. index:: ggplot

        Voir `Customizing plots with style sheets <http://matplotlib.org/users/style_sheets.html>`_

        ::

            import matplotlib.pyplot as plt
            plt.style.use('ggplot')
    """
    import matplotlib.pyplot as plt
    plt.style.use(style)


def close_all():
    """
    Closes every graph with :epkg:`matplotlib`.

    .. faqref::
        :tag: matplotlib
        :title: Plante après plusieurs graphes

        Il peut arriver que matplotlib fasse planter python sans qu'aucune exception ne soit générée.
        L'article `matplotlib crashing Python <http://stackoverflow.com/questions/26955017/matplotlib-crashing-python>`_
        suggère la solution suivante ::

            import matplotlib.pyplot as plt
            plt.close('all')

        Voir `close <http://matplotlib.org/api/pyplot_api.html?highlight=close#matplotlib.pyplot.close>`_.
    """
    import matplotlib.pyplot as plt
    plt.close('all')


def graph_with_label(x, y, labels, barplot=True, title=None, figsize=(6, 4), style=None,
                     ax=None, **kwargs):
    """
    Creates a graph with :epkg:`matplotlib`.

    @param      x       x
    @param      y       y
    @param      labels  x labels
    @param      barplot boolean, True, uses bar, plot otherwise
    @param      title   if not None, sets the title
    @param      figsize only if ax is not None
    @param      style   style
    @param      ax      existing :epkg:`Axes` or None if it must be created
    @param      kwargs  others parameters
    @return             :epkg:`Axes`

    .. faqref::
        :tag: matplotlib
        :title: Comment ajuster les labels non numériques d'un graphe ?

        .. index:: date, matplotlib

        Lorsqu'on trace un graphique et qu'on veut ajouter des labels non numériques
        sur l'axe des abscisses (en particulier des dates), *matplotlib*
        ne fait pas apparaître tous les labels. Ainsi, si on a 50 points,
        50 abscisses et 50 labels, seuls les premiers labels apparaîtront
        comme ceci :

        .. plot::

            import matplotlib.pyplot as plt
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
            y = [1, 3, 10, 6, 3, 5, 3, 6, 4, 2, 3, 2, 11, 10, 4, 5, 2, 5, 4, 1, 1, 1, 3, 15, 5, 2, 1, 5, 3, 1, 3,
                 2, 4, 5, 2, 12, 12, 5, 11, 2, 19, 21, 5, 2]
            xl = ['2014-w04', '2014-w05', '2014-w06', '2014-w07', '2014-w08', '2014-w09',
                  '2014-w10', '2014-w11',
                  '2014-w12', '2014-w13', '2014-w14', '2014-w15', '2014-w16',
                  '2014-w17', '2014-w18', '2014-w19', '2014-w20', '2014-w21', '2014-w22', '2014-w23',
                  '2014-w24', '2014-w25', '2014-w27',
                  '2014-w29', '2014-w30', '2014-w31', '2014-w32', '2014-w34', '2014-w35', '2014-w36',
                  '2014-w38', '2014-w39', '2014-w41',
                  '2014-w42', '2014-w43', '2014-w44', '2014-w45', '2014-w46', '2014-w47', '2014-w48',
                  '2014-w49', '2014-w50', '2014-w51', '2014-w52']
            plt.close('all')
            fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(10,4))
            ax.bar( x,y )
            ax.set_xticklabels( xl )
            ax.grid(True)
            ax.set_title("commits")
            plt.show()

        Or c'est cela qu'on veut :

        .. plot::

            import matplotlib.pyplot as plt
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
            y = [1, 3, 10, 6, 3, 5, 3, 6, 4, 2, 3, 2, 11, 10, 4, 5, 2, 5, 4, 1, 1, 1, 3, 15, 5, 2, 1, 5,
                 3, 1, 3, 2, 4, 5, 2, 12, 12, 5, 11, 2, 19, 21, 5, 2]
            xl = ['2014-w04', '2014-w05', '2014-w06', '2014-w07', '2014-w08', '2014-w09',
                  '2014-w10', '2014-w11', '2014-w12', '2014-w13', '2014-w14',
                  '2014-w15', '2014-w16', '2014-w17', '2014-w18', '2014-w19',
                  '2014-w20', '2014-w21', '2014-w22', '2014-w23', '2014-w24', '2014-w25',
                  '2014-w27', '2014-w29', '2014-w30', '2014-w31', '2014-w32', '2014-w34',
                  '2014-w35', '2014-w36', '2014-w38', '2014-w39', '2014-w41',
                  '2014-w42', '2014-w43', '2014-w44', '2014-w45', '2014-w46', '2014-w47',
                  '2014-w48', '2014-w49', '2014-w50', '2014-w51', '2014-w52']
            plt.close('all')
            fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(10,4))
            ax.bar( x,y )
            tig = ax.get_xticks()
            labs = [ ]
            for t in tig:
                if t in x: labs.append(xl[x.index(t)])
                else: labs.append("")
            ax.set_xticklabels( labs )
            ax.grid(True)
            ax.set_title("commits")
            plt.show()

        Pour cela il faut d'abord utiliser la méthode
        `get_xticks <http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.get_xticks>`_
        pour récupérer d'abord les graduations et n'afficher les labels que
        pour celles-ci
        (voir aussi `Custom ticks autoscaled when using imshow?
        <http://stackoverflow.com/questions/13409006/custom-ticks-autoscaled-when-using-imshow>`_).
        Voici un exemple de code ::

            import matplotlib.pyplot as plt
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
            y = [1, 3, 10, 6, 3, 5, 3, 6, 4, 2, 3, 2, 11, 10, 4, 5, 2, 5, 4, 1, 1, 1, 3, 15, 5, 2, 1, 5, 3, 1, 3, 2,
                 4, 5, 2, 12, 12, 5, 11, 2, 19, 21, 5, 2]
            xl = ['2014-w04', '2014-w05', '2014-w06', '2014-w07', '2014-w08', '2014-w09', '2014-w10', '2014-w11', '2014-w12', '2014-w13',
                  '2014-w14', '2014-w15', '2014-w16', '2014-w17', '2014-w18', '2014-w19', '2014-w20', '2014-w21',
                  '2014-w22', '2014-w23', '2014-w24', '2014-w25',
                  '2014-w27', '2014-w29', '2014-w30', '2014-w31', '2014-w32', '2014-w34', '2014-w35', '2014-w36',
                  '2014-w38', '2014-w39', '2014-w41', '2014-w42',
                  '2014-w43', '2014-w44', '2014-w45', '2014-w46', '2014-w47', '2014-w48', '2014-w49',
                  '2014-w50', '2014-w51', '2014-w52']
            plt.close('all')
            fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(10,4))
            ax.bar( x,y )
            tig = ax.get_xticks()
            labs = [ ]
            for t in tig:
                if t in x:
                    labs.append(xl[x.index(t)])
                else:
                    # une graduation peut être en dehors des labels proposés
                    labs.append("")
            ax.set_xticklabels( labs )
            ax.grid(True)
            ax.set_title("commits")
            plt.show()
    """
    import matplotlib.pyplot as plt
    if ax is None:
        _, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 4))

    if barplot:
        if style is None:
            ax.bar(x, y, **kwargs)
        else:
            ax.bar(x, y, style=style, **kwargs)
    else:
        if style is None:
            ax.plot(x, y, **kwargs)
        else:
            ax.plot(x, y, style=style, **kwargs)
    tig = ax.get_xticks()
    xl = labels
    labs = []
    for t in tig:
        if t in x:
            labs.append(xl[x.index(t)])
        else:
            labs.append("")
    ax.set_xticklabels(labs)
    ax.grid(True)
    if title is not None:
        ax.set_title(title)
    return ax


def change_legend_location(ax, new_location="lower center"):
    """
    Changes the location of the legend.

    @param      ax              :epkg:`Axes`
    @param      new_location    new_location, see method :epkg:`legend`
    @return                     ax

    .. faqref::
        :tag: matplotlib
        :title: Comment changer l'emplacement de la légende ?

        On cherche ici à changer l'emplacement de la légende alors que celle-ci a déjà été
        définie par ailleurs. C'est pratique lorsque celle-ci cache une partie du graphe
        qu'on veut absolument montrer.
        On ne dispose que de l'objet *ax* de type :epkg:`Axes`.
        On utilise pour cela la méthode :epkg:`legend`
        et le code suivant :

        ::

            handles, labels = ax.get_legend_handles_labels()
            ax.legend(handles, labels, loc="lower center")

        Les différentes options pour le nouvel emplacement sont énoncées
        dans l'aide associée à la méthode :epkg:`legend`.
    """
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc=new_location)
    return ax


def avoid_overlapping_dates(fig, **options):
    """
    Avoids overlapping dates by calling method
    :epkg:`autofmt_xdate`.

    .. faqref::
        :tag: matplotlib
        :title: Comment éviter les dates qui se superposent ?

        La méthode :epkg:`autofmt_xdate`
        permet d'éviter les problèmes de dates
        qui se superposent.

        ::

            fig, ax = plt.subplots(...)
            # ...
            fig.autofmt_xdate()
    """
    fig.autofmt_xdate(**options)


def graph_cities_default_lands():
    """
    Returns the default list of elements which can be added to a map.
    See `Features <https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/feature_interface.html#cartopy.feature.GSHHSFeature>`_.

    .. runpython::
        :showcode:

        from ensae_teaching_cs.faq.faq_matplotlib import graph_cities_default_lands
        print(graph_cities_default_lands())
    """
    return ["BORDERS", "COASTLINE", "LAKES", "LAND", "OCEAN", "RIVERS"]


def graph_cities(df, names=("Longitude", "Latitude", "City"), ax=None, linked=False,
                 fLOG=None, loop=False, many=False,
                 draw_coastlines=True, draw_countries=True,
                 fill_continents=True, draw_parallels=True,
                 draw_meridians=True, draw_map_boundary=True,
                 **params):
    """
    Plots the cities on a map with :epkg:`cartopy`.
    Only not empty names are displayed on the graph.

    @param      df                  dataframe
    @param      names               names of the column Latitude, Longitude, City
    @param      ax                  existing ax
    @param      linked              draw lines between points
    @param      loop                add a final line to link the first point to the final one
    @param      fLOG                logging function
    @param      params              see below
    @param      many                change the return
    @param      draw_coastlines     draw coast lines
    @param      draw_countries      draw borders
    @param      draw_map_boundary   draw boundaries
    @param      draw_meridians      draw meridians
    @param      draw_parallels      draw parallels
    @param      fill_continents     fill continents
    @return                         *ax* or *fig, ax, m* if *many* is True

    Additional parameters:

    * projection: see `projections <https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html>`_,
      only used is *ax* is None
    * bounds: something like ``[lon1, lon2, lat1, lat2]``
    * landscape: a list of strings about what needs to be on the map,
      see @see fn graph_cities_default_lands.
    * style, markersize, fontname, fontcolor, fontsize, fontweight, fontvalign

    If the function returns the following error
    ``'AxesSubplot' object has no attribute 'add_feature'``,
    it means no projection was added to the axis.
    The function currently creates the following way:

    ::

        import cartopy.crs as ccrs
        import matplotlib.pyplot as plt
        projection = params.pop('projection', ccrs.PlateCarree())
        fig = plt.figure(**params)
        ax = fig.add_subplot(1, 1, 1, projection)
    """
    bounds = params.pop("bounds", None)
    landscape = params.pop("landscape", graph_cities_default_lands())

    style = params.pop('style', 'ro')
    markersize = params.pop('markersize', 6)
    fontname = params.pop('fontname', 'Arial')
    fontsize = str(params.pop('fontsize', '16'))
    fontcolor = params.pop('fontcolor', 'black')
    fontweight = params.pop('fontweight', 'normal')
    fontvalign = params.pop('fontvalign', 'bottom')

    xx = list(df[names[0]])
    yy = list(df[names[1]])

    if ax is None:
        import cartopy.crs as ccrs
        import matplotlib.pyplot as plt
        projection = params.pop(  # pylint: disable=E0110
            'projection', ccrs.PlateCarree())  # pylint: disable=E0110
        fig = plt.figure(**params)
        ax = fig.add_subplot(1, 1, 1, projection=projection)
    else:
        fig = None

    import cartopy.feature as cfeature
    for land in landscape:
        attr = getattr(cfeature, land)
        ax.add_feature(attr)

    if linked and "-" not in style:
        style += "-"
    ax.plot(df[names[0]], df[names[1]], style, markersize=markersize)
    ax.set_title('France')

    minx, maxx = min(xx), max(xx)
    miny, maxy = min(yy), max(yy)
    avex, avey = numpy.mean(xx), numpy.mean(yy)
    if fLOG:
        mes = "[graph_cities] Lon:[{0}, {1}] x Lat:[{2}, {3}] - mean={4}, {5} - linked={6}"
        fLOG(mes.format(minx, maxx, miny, maxy, avex, avey, linked))
    if bounds:
        dx = (maxx - minx) / 10
        dy = (maxy - miny) / 10
        minx -= dx
        maxx += dx
        miny -= dy
        maxy += dy
        ax.set_extent(bounds)
    else:
        ax.set_extent([minx, maxx, miny, maxy])
        if fLOG:
            fLOG("[graph_cities] ", [minx, maxx, miny, maxy])

    view = df[list(names)]
    for x, y, t in view.itertuples(index=False):
        if t is None or len(t) == 0:
            continue
        ax.text(x, y, t,
                fontname=fontname, size=fontsize,
                color=fontcolor, weight=fontweight,
                verticalalignment=fontvalign)
    return fig, ax
