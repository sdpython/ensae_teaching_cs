"""
@file
@brief      scatter plots
"""
import numpy
from matplotlib.tri import Triangulation
from matplotlib.pyplot import Normalize
from .colorsdef import colors_definition


def scatter_xy_id(xy_id, legend=None, ax=None, **options):
    """
    Creates a scatter plot with a different color for each zone id.
    The function requires `matploblib <http://matplotlib.org/>`_.

    @param      xy_id       list of 3-uple *(x, y, zone_id)*
    @param      legend      dictionary {id: legend } or None if there is not any
    @param      ax          existing graph to plot on (can be None)
    @param      options     others options: xlabel, ylabel, title, marker, figsize (if ax is None)
    @return                 fig, ax (fig is None if ax was sent to the function)

    .. plot::
        :include-source:

        import random
        def generate_gauss(x, y, sigma, N=1000):
            res = []
            for i in range(N):
                u = random.gauss(0, 1)
                a = sigma * u + x
                b = sigma * random.gauss(0, 1) + y + u
                res.append((a, b))
            return res
        nuage1 = generate_gauss(0, 0, 3)
        nuage2 = generate_gauss(3, 4, 2)
        nuage = [(a, b, 0) for a, b in nuage1] + [(a, b, 1) for a, b in nuage2]

        import matplotlib.pyplot as plt
        from ensae_teaching_cs.helpers.matplotlib_helper_xyz import scatter_xy_id
        fig, ax = scatter_xy_id(nuage, title="example with random observations",
                                legend={0: "c0", 1: "c1"})
        plt.show()

    The error ``ValueError: Unknown projection '3d'`` is raised when the line
    ``from mpl_toolkits.mplot3d import Axes3D`` is missing.
    """
    curves = {}
    for x, y, zid in xy_id:
        if zid not in curves:
            curves[zid] = []
        curves[zid].append((x, y))

    marker = options.get('marker', 'o')
    if ax is None:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=options.get('figsize', None))
    else:
        fig = None
    color = 0
    legs = []
    for k in sorted(curves):
        v = curves[k]
        f, = ax.plot([_[0] for _ in v], [_[1] for _ in v],
                     marker, color=colors_definition[color][1])
        if legend is not None:
            legs.append((f, legend.get(k, "unknown:" + str(k))))
        color += 1

    if len(legs) > 0:
        ax.legend([_[0] for _ in legs], [_[1] for _ in legs])

    if "xlabel" in options:
        ax.set_xlabel(options["xlabel"])
    if "ylabel" in options:
        ax.set_ylabel(options["ylabel"])
    if "title" in options:
        ax.set_title(options["title"])
    return fig, ax


def scatter_xyc(points, smooth=0, div=10, ax=None, **options):
    """
    Draws a 2D graph (X,Y, color), the color is chosen based on a value *f(x,y)*
    The function requires :epkg:`matploblib` and :epkg:`scipy`.

    @param      points      (x,y, z=f(x,y) )
    @param      smooth      applies n times a smoothing I * M (convolutional)
    @param      div         number of divisions for axis
    @param      options     others options: xlabel, ylabel, title, figsize (if ax is None)
    @return                 fig, ax (fig is None if ax was sent to the function)

    .. plot::
        :include-source:

        import random
        def generate_gauss(x, y, sigma, N=1000):
            res = []
            for i in range(N):
                u = random.gauss(0, 1)
                a = sigma * u + x
                b = sigma * random.gauss(0, 1) + y + u
                res.append((a, b))
            return res
        def f(a, b):
            return (a ** 2 + b ** 2) ** 0.5
        nuage1 = generate_gauss(0, 0, 3)
        nuage2 = generate_gauss(3, 4, 2)
        nuage = [(a, b, f(a, b)) for a, b in nuage1] + [(a, b, f(a, b)) for a, b in nuage2]
        import matplotlib.pyplot as plt
        plt.style.use('ggplot')
        from ensae_teaching_cs.helpers.matplotlib_helper_xyz import scatter_xyc
        fig, ax = scatter_xyc(nuage, title="example with random observations")
        plt.show()

    The error ``ValueError: Unknown projection '3d'`` is raised when the line
    ``from mpl_toolkits.mplot3d import Axes3D`` is missing.
    """
    if ax is None:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=options.get('figsize', None))
    else:
        fig = None

    x = [_[0] for _ in points]
    y = [_[1] for _ in points]
    z = [_[2] for _ in points]

    tri = Triangulation(x, y)

    plt.tricontour(tri, z, 15, linewidths=0.5, colors='k')
    plt.tricontourf(tri, z, 15, cmap=plt.cm.rainbow,
                    norm=Normalize(vmax=numpy.abs(z).max(), vmin=-numpy.abs(z).max()))
    plt.colorbar(ax=ax)
    ax.scatter(x, y, c='b', s=5, zorder=10)
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))

    if "xlabel" in options:
        ax.set_xlabel(options["xlabel"])
    if "ylabel" in options:
        ax.set_ylabel(options["ylabel"])
    if "title" in options:
        ax.set_title(options["title"])
    return fig, ax


def scatter_xyz(points, smooth=0, div=100, ax=None, **options):
    """
    Draws a 3D graph (X, Y, Z).
    The function requires :epkg:`matploblib`
    and :epkg:`scipy`.

    @param      points      (x,y, z=f(x,y) )
    @param      div         number of divisions for axis
    @param      smooth      applies n times a smoothing I * M (convolutional)
    @param      ax          existing graph to plot on (can be None)
    @param      options     others options: xlabel, ylabel, zlabel, title, elev, angle, figsize (if ax is None)
                                - elev, angle: see `view_init <http://matplotlib.org/mpl_toolkits/mplot3d/api.html>`_)
    @return                 fig, ax (fig is None if ax was sent to the function)

    If *ax is None*, axes are created like::

        fig = plt.figure(figsize=options.get('figsize', None))
        ax = fig.gca(projection='3d')

    .. plot::
        :include-source:

        import random
        def generate_gauss(x, y, sigma, N=1000):
            res = []
            for i in range(N):
                u = random.gauss(0, 1)
                a = sigma * u + x
                b = sigma * random.gauss(0, 1) + y + u
                res.append((a, b))
            return res
        def f(a, b):
            return (a ** 2 + b ** 2) ** 0.5
        nuage1 = generate_gauss(0, 0, 3)
        nuage2 = generate_gauss(3, 4, 2)
        nuage = [(a, b, f(a, b)) for a, b in nuage1] + [(a, b, f(a, b)) for a, b in nuage2]

        import matplotlib.pyplot as plt
        from ensae_teaching_cs.helpers.matplotlib_helper_xyz import scatter_xyz
        fig, ax = scatter_xyz(nuage, title="example with random observations")
        plt.show()

    The error ``ValueError: Unknown projection '3d'`` is raised when the line
    ``from mpl_toolkits.mplot3d import Axes3D`` is missing.
    """
    x = [_[0] for _ in points]
    y = [_[1] for _ in points]
    z = [_[2] for _ in points]

    if ax is None:
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        if Axes3D is None:
            raise ImportError("Unable to import mpl_toolkits.mplot3d")
        fig = plt.figure(figsize=options.get('figsize', None))
        ax = fig.gca(projection='3d')
    else:
        fig = None

    elev = options.get("elev", 50)
    angle = options.get("angle", 45)
    ax.view_init(elev, angle)

    tri = Triangulation(x, y)
    ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap='autumn')

    if "xlabel" in options:
        ax.set_xlabel(options["xlabel"])
    if "ylabel" in options:
        ax.set_ylabel(options["ylabel"])
    if "zlabel" in options:
        ax.set_ylabel(options["zlabel"])
    if "title" in options:
        ax.set_title(options["title"])
    return fig, ax
