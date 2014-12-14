# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `CVXOPT <http://cvxopt.org/>`_.

"""

def graph_style(style = 'ggplot'):
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
    