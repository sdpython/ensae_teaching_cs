

.. blogpost::
    :title: Deep learning and other readings
    :keywords: machine learning, dask, OSM, Open Street Map
    :date: 2015-12-22
    :categories: deep learning
    
    I came accross the following article 
    `Evaluation of Deep Learning Toolkits <https://github.com/zer0n/deepframeworks/blob/master/README.md>`_
    which studies a short list of libraries for deep learning: Caffe, CNTK, TensorFlow, Theano, Torch,
    and various angles: modeling capability, interfaces, model deployment, performance, architecture, ecosystem, cross-platform.
    It gives a nice overview and helps choosing the library which fits your needs. Once your deep models has been trained,
    how to use it? This question should be the first one to be answered.

    As machine learning and big data become more and more popular, people look for ways
    to simplify the implementation of complex chains of processings. Python is quite popular so here is one suggestion
    in that language for deep learning:
    `Blocks and Fuel: Frameworks for deep learning <http://arxiv.org/abs/1506.00619>`_
    *(Bart van Merriënboer, Dzmitry Bahdanau, Vincent Dumoulin, Dmitriy Serdyuk, David Warde-Farley, Jan Chorowski, Yoshua Bengio)*.
    It introduces `Fuel <https://fuel.readthedocs.org/en/latest/>`_ which models pipelines of data processing.

    Finally, a nice tutorial on machine learning with Python:
    `PyData Seattle 2015 Scikit-learn Tutorial <https://github.com/jakevdp/sklearn_pydata2015>`_.
    The author's blog is nice too: `Pythonic Perambulations <https://jakevdp.github.io/>`_.
    See `Out-of-Core Dataframes in Python: Dask and OpenStreetMap <https://jakevdp.github.io/blog/2015/08/14/out-of-core-dataframes-in-python/>`_.
    Some modules are hidden in his blog posts such as 
    `gatspy <http://www.astroml.org/gatspy/>`_ which plots timeseries in many ways or 
    `supersmoother <https://github.com/jakevdp/supersmoother>`_ to smooth timeseries or 
    `line_profiler <https://github.com/rkern/line_profiler>`_ in
    `Optimizing Python in the Real World: NumPy, Numba, and the NUFFT <https://jakevdp.github.io/blog/2015/02/24/optimizing-python-with-numpy-and-numba/>`_.
    Two other readings to conclude:
    `Why Python is Slow: Looking Under the Hood <https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/>`_ and
    `Frequentism and Bayesianism: A Practical Introduction <https://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/>`_
    still from the same source.
    
    **Addition (01/06/16)**: see also `Comparative Study of Caffe, Neon, Theano, and Torch for Deep Learning <http://arxiv.org/pdf/1511.06435v2.pdf>`_

    Source: `XD Blogs <http://www.xavierdupre.fr/blog/2015-12-22_nojs.html>`_.