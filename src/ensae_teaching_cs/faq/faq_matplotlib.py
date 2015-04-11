# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `matplotlib <http://matplotlib.org/>`_.

"""


def graph_style(style='ggplot'):
    """

    change matplotlib style

    @param      style       style

    @FAQ(matplotlib___Changer le style de graphique pour ggplot)

    .. index:: ggplot

    voir `Customizing plots with style sheets <http://matplotlib.org/users/style_sheets.html>`_

    @code
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    @endcode

    @endFAQ
    """
    import matplotlib.pyplot as plt
    plt.style.use(style)


def close_all():
    """
    Close every graph with matploblib

    @FAQ(matplotlib__Plante après plusieurs graphes)

    Il peut arriver que matplotlib fasse planter python sans qu'aucune exception ne soit générée.
    L'article `matplotlib crashing Python <http://stackoverflow.com/questions/26955017/matplotlib-crashing-python>`_
    suggère la solution suivante ::

        import matplotlib.pyplot as plt
        plt.close('all')

    @endFAQ
    """
    import matplotlib.pyplot as plt
    plt.close('all')


def zoomable():
    """
    @FAQ(matplotlib___Des graphiques zoomables dans un notebook ?)

    Voir le notebook :ref:`matplotlibzoomablerst`.

    @endFAQ
    """
    pass


def graph_ggplot_with_label(x,
                            y,
                            labels,
                            bar=True,
                            title=None,
                            figsize=(6, 4),
                            style=None,
                            ax=None,
                            **kwargs):
    """
    creates a graph with matplotlib

    @param      x       x
    @param      y       y
    @param      labels  x labels
    @param      bar     boolean, True, uses bar, plot otherwise
    @param      title   if not None, sets the title
    @param      figsize only if ax is not None
    @param      style   style
    @param      ax      existing `Axes <http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes>`_ or None if it must be created
    @param      kwargs  others parameters
    @return             `Axes <http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes>`_

    @FAQ(matplotlib___Comment ajuster les labels non numériques d'un graphe ?)

    .. index:: date, matplotlib

    Lorsqu'on trace un graphique et qu'on veut ajouter des labels non numériques
    sur l'axe des abscisses (en particulier des dates), *matplotlib*
    ne fait pas apparaître tous les labels. Ainsi, si on a 50 points,
    50 abscisses et 50 labels, seuls les premiers labels apparaîtront
    comme ceci :

    .. plot::

        import matplotlib.pyplot as plt
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
        y = [1, 3, 10, 6, 3, 5, 3, 6, 4, 2, 3, 2, 11, 10, 4, 5, 2, 5, 4, 1, 1, 1, 3, 15, 5, 2, 1, 5, 3, 1, 3, 2, 4, 5, 2, 12, 12, 5, 11, 2, 19, 21, 5, 2]
        xl = ['2014-w04', '2014-w05', '2014-w06', '2014-w07', '2014-w08', '2014-w09', '2014-w10', '2014-w11', '2014-w12', '2014-w13', '2014-w14', '2014-w15', '2014-w16', '2014-w17', '2014-w18', '2014-w19', '2014-w20', '2014-w21', '2014-w22', '2014-w23', '2014-w24', '2014-w25', '2014-w27', '2014-w29', '2014-w30', '2014-w31', '2014-w32', '2014-w34', '2014-w35', '2014-w36', '2014-w38', '2014-w39', '2014-w41', '2014-w42', '2014-w43', '2014-w44', '2014-w45', '2014-w46', '2014-w47', '2014-w48', '2014-w49', '2014-w50', '2014-w51', '2014-w52']
        plt.close('all')
        plt.style.use('ggplot')
        fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(10,4))
        ax.bar( x,y )
        ax.set_xticklabels( xl )
        ax.grid(True)
        ax.set_title("commits")
        plt.show()

    Or c'est cela qu'on veut :

    .. plot::

        import matplotlib.pyplot as plt
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
        y = [1, 3, 10, 6, 3, 5, 3, 6, 4, 2, 3, 2, 11, 10, 4, 5, 2, 5, 4, 1, 1, 1, 3, 15, 5, 2, 1, 5, 3, 1, 3, 2, 4, 5, 2, 12, 12, 5, 11, 2, 19, 21, 5, 2]
        xl = ['2014-w04', '2014-w05', '2014-w06', '2014-w07', '2014-w08', '2014-w09', '2014-w10', '2014-w11', '2014-w12', '2014-w13', '2014-w14', '2014-w15', '2014-w16', '2014-w17', '2014-w18', '2014-w19', '2014-w20', '2014-w21', '2014-w22', '2014-w23', '2014-w24', '2014-w25', '2014-w27', '2014-w29', '2014-w30', '2014-w31', '2014-w32', '2014-w34', '2014-w35', '2014-w36', '2014-w38', '2014-w39', '2014-w41', '2014-w42', '2014-w43', '2014-w44', '2014-w45', '2014-w46', '2014-w47', '2014-w48', '2014-w49', '2014-w50', '2014-w51', '2014-w52']
        plt.close('all')
        plt.style.use('ggplot')
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
    (voir aussi `Custom ticks autoscaled when using imshow? <http://stackoverflow.com/questions/13409006/custom-ticks-autoscaled-when-using-imshow>`_).
    Voici un exemple de code ::

        import matplotlib.pyplot as plt
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
        y = [1, 3, 10, 6, 3, 5, 3, 6, 4, 2, 3, 2, 11, 10, 4, 5, 2, 5, 4, 1, 1, 1, 3, 15, 5, 2, 1, 5, 3, 1, 3, 2, 4, 5, 2, 12, 12, 5, 11, 2, 19, 21, 5, 2]
        xl = ['2014-w04', '2014-w05', '2014-w06', '2014-w07', '2014-w08', '2014-w09', '2014-w10', '2014-w11', '2014-w12', '2014-w13', '2014-w14', '2014-w15', '2014-w16', '2014-w17', '2014-w18', '2014-w19', '2014-w20', '2014-w21', '2014-w22', '2014-w23', '2014-w24', '2014-w25', '2014-w27', '2014-w29', '2014-w30', '2014-w31', '2014-w32', '2014-w34', '2014-w35', '2014-w36', '2014-w38', '2014-w39', '2014-w41', '2014-w42', '2014-w43', '2014-w44', '2014-w45', '2014-w46', '2014-w47', '2014-w48', '2014-w49', '2014-w50', '2014-w51', '2014-w52']
        plt.close('all')
        plt.style.use('ggplot')
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


    @endFAQ
    """
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    if ax is None:
        plt.close('all')
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 4))

    if bar:
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
    Changes the location of the legend

    @param      ax              `Axes <http://matplotlib.org/api/axes_api.html#axes>`_
    @param      new_location    new_location, see method `legend <http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.legend>`_
    @return                     ax

    @FAQ(matplotlib___Comment changer l'emplacement de la légende ?)

    On cherche ici à changer l'emplacement de la légende alors que celle-ci a déjà été
    définie par ailleurs. C'est pratique lorsque celle-ci cache une partie du graphe
    qu'on veut absolument montrer.
    On ne dispose que de l'objet *ax* de type `Axes <http://matplotlib.org/api/axes_api.html#axes>`_.
    On utilise pour cela la méthode `legend <http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.legend>`_
    et le code suivant :

    @code
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc="lower center")
    @endcode

    Les différentes options pour le nouvel emplacement sont énoncées
    dans l'aide associée à la méthode `legend <http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.legend>`_.

    @endFAQ
    """
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc=new_location)
    return ax
