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
    @encode

    @endFAQ
    """
    import matplotlib.pyplot as plt
    plt.style.use(style)