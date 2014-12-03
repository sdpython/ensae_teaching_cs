# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `IPython <http://ipython.org/>`_.

"""

def notebook_path():
    """

    change matplotlib style

    @param      style       style

    @FAQ(ipython___Récupérer le fichier du notebook depuis le notebook)

    Voir `How to I get the current IPython Notebook name <http://stackoverflow.com/questions/12544056/how-to-i-get-the-current-ipython-notebook-name>`_

    Il suffit d'insérer la cellule suivante dans le notebook ::

        %%javascript
        var kernel = IPython.notebook.kernel;
        var body = document.body,
            attribs = body.attributes;
        var command = "theNotebook = os.path.join(" + "r'"+attribs['data-project'].value+"'," + "r'"+attribs['data-notebook-path'].value+"'," + "r'"+attribs['data-notebook-name'].value+"')";
        kernel.execute(command);

    On peut vérifier que cela fonctionne ::

        theNotebook

    @endFAQ
    """
    pass