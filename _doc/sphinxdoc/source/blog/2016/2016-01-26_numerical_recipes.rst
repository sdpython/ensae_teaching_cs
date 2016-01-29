

.. blogpost::
    :title: Numerical Recipes
    :keywords: Numerical Recipes, BLAS, LAPACK, Eigen, MKL, Intel MKL, Numpy
    :date: 2016-01-26
    :categories: calcul matriciel
    
    `numpy <http://www.numpy.org/>`_, 
    `scipy <http://www.scipy.org/>`_
    couvrent la plupart des besoins lorsqu'il s'agit de calcul
    matriciel. On ne se pose même plus la question de savoir comment
    c'est implémenté. Cette question revient lorsqu'on a besoin
    d'un algorithme en particulier et que celui-ci n'est pas 
    disponible dans l'environment dans lequel on programme.
    
    Il existe un livre célèbre qui reprend la plupart des besoins dans ce domaine :
    `numerical recipes <http://www2.units.it/ipl/students_area/imm2/files/Numerical_Recipes.pdf>`_,
    un petit millier de page de théorie et de code. L'usage des codes proposés 
    est soumis à quelques `restrictions <https://fr.wikipedia.org/wiki/Numerical_Recipes#Critiques>`_
    et ils ne sont pas aussi rapides que les codes des librairies
    `BLAS <http://www.netlib.org/blas/>`_,
    `LAPACK <http://www.netlib.org/lapack/>`_,
    `LINPACK <http://www.netlib.org/linpack/>`_, 
    `ATLAS <http://math-atlas.sourceforge.net/>`_,
    `Eigen <http://eigen.tuxfamily.org/index.php?title=Main_Page>`_.
    
    Il y a aussi `Intel-MKL <https://software.intel.com/en-us/intel-mkl/>`_ 
    développé par Intel qui explique le suffixe MKL ajouté à numpy 
    `numpy-mkl <https://software.intel.com/en-us/articles/numpyscipy-with-intel-mkl>`_.