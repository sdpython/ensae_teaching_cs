
.. blogpost::
    :title: Ecrire du code rapide
    :keywords: optimisation
    :date: 2018-08-21
    :categories: programmation
    :lid: blog-post-optim-code-2018-08

    Le titre n'est pas très évocateur mais l'article qui suit
    `Bing.com runs on .NET Core 2.1! <https://blogs.msdn.microsoft.com/dotnet/2018/08/20/bing-com-runs-on-net-core-2-1/>`_
    explique comment un service web, en l'occurence le moteur
    de recherche `Bing <https://www.bing.com/>`_, a été
    accéléré. Et l'explication repose sur six optimisation
    d'implémentation reliés à chaque à ce qu'on appelle une
    `pull request <https://help.github.com/articles/about-pull-requests/>`_.
    Les deux suivantes qui font partie des six ne sont pas
    trop compliqués à lire en particulier la deuxième
    qui révèle que le moteur de recherche parse énormément d'urls
    à la recherche de caractères ``/``. A priori, la modification
    implique que la recherche de deux ou trois charactères et très
    souvent utilisée et que cela vaut le coup d'écrire spécifique
    dans ce cas. Le test qui choisit l'un ou l'autre cas
    apparaît d'un surcoût négligeable.

    * `Vectorize String.IndexOf(char) and String.LastIndexOf(char) <https://github.com/dotnet/coreclr/pull/16392/files>`_
    * `Improve performance of string.IndexOfAny for 2 & 3 char searches <https://github.com/dotnet/coreclr/pull/13219/files>`_
