

.. _blog-optimisation-contrainte:

.. blogpost::
    :title: Optimisation avec contraintes, cvxopt, pulp, NLopt, ...
    :keywords: optimisation, contrainte, cvxopt, pulp, NLopt, picos
    :date: 2015-07-17
    :categories: optimisation, machine learning

    Mon premier réflexe pour faire de l'optimisation avec contrainte était
    de me tourner vers 
    `cvxopt <http://cvxopt.org/>`_, de trouver la fonction
    qui correspondait à mon problème puis à renseigner 
    construire les différentes matrices.
    
    Le module 
    `pulp <http://pythonhosted.org/PuLP/>`_ est plus intuitif
    dans la manière de définir le problème. On a quasiment 
    plus besoin de lire la documentation mais pour une utilisation
    occasionnelle. Je suggère la lecture de 
    ces deux articles :
    
    * `Decision Making Under Uncertainty: An Introduction to Robust Optimization (Part 1) <http://blog.yhathq.com/posts/decision-making-under-uncertainty.html>`_
    * `Decision Making Under Uncertainty: An Introduction to Robust Optimization (Part 2) <http://blog.yhathq.com/posts/decision-marking-under-uncertainty-2.html>`_
    
    Cette approche est très proche de celle proposée par 
    `cvxpy <http://www.cvxpy.org/en/latest/>`_. La logique est la même, la syntaxe de *cvxpy*
    utilise des méthodes, celle de *pulp* des opérateurs.
    
    Il exite d'autres options comme `picos <http://picos.zib.de/index.html>`_
    et encore d'autres proposées à
    `Python optimization frameworks <https://github.com/johnyf/tool_lists/blob/master/optimization.md>`_.
    Pour le non linéaire, il faut voir avec `nlopt <http://ab-initio.mit.edu/wiki/index.php/NLopt>`_.
    