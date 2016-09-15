# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `Jupyter <https://jupyter.org/>`_.

"""

import os

from pyquickhelper.loghelper import fLOG
from .faq_jupyter_helper import nb_open


def notebook_path():
    """
    change matplotlib style

    @param      style       style

    .. faqref::
        :tag: jupyter
        :title: Récupérer le fichier du notebook depuis le notebook

        Voir `How to I get the current Jupyter Notebook name <http://stackoverflow.com/questions/12544056/how-to-i-get-the-current-ipython-notebook-name>`_

        Il suffit d'insérer la cellule suivante dans le notebook ::

            %%javascript
            var kernel = IPython.notebook.kernel;
            var body = document.body,
                attribs = body.attributes;
            var command = "theNotebook = os.path.join(" + "r'"+attribs['data-project'].value+"'," +
                          "r'"+attribs['data-notebook-path'].value+"'," + "r'"+attribs['data-notebook-name'].value+"')";
            kernel.execute(command);

        On peut vérifier que cela fonctionne ::

            theNotebook
    """
    pass


def r_and_notebook():
    """
    Cette fonction test si la variable ``R_HOME`` est définie et pointe sur une
    version de R présente.

    .. exref::
        :title: Utiliser R depuis un notebook
        :tag: Technique

        .. index:: R

        C'est l'objet des deux notebooks :ref:`td2acenoncesession2brst` et la :ref:`correction <td2acorrectionsession2brst>`.

    .. faqref::
        :tag: jupyter
        :title: Comment utiliser R depuis un notebook ?

        Voir notebooks :ref:`td2acenoncesession2brst`,
        :ref:`correction <td2acorrectionsession2brst>`.
    """
    if "R_HOME" not in os.environ:
        raise KeyError("R_HOME not present")

    path = os.environ["R_HOME"]
    if path is None or not os.path.exists(path):
        raise FileNotFoundError("unable to find R at {0}".format(path))

    return True


def jupyter_convert_notebooks():
    """
    .. exref::
        :title: Convertir le notebook en cours au format HTML
        :tag: Technique

        .. index:: conversion, html, rst

        C'est l'objet du notebook :ref:`notebookconvertrst`.

    .. faqref::
        :tag: jupyter
        :title: Comment convertir le notebook en cours au format HTML ?

        Voir notebook :ref:`notebookconvertrst`.

    .. faqref::
        :tag: jupyter
        :title: Comment ajouter un lien vers un fichier local pour le télécharger ?

        Voir notebook :ref:`notebookconvertrst`.
    """
    pass


def jupyter_get_variable(name, magic_command_instance):
    """
    Retrieve the value of a local variable in a notebook.

    @param      name                        variable name
    @param      magic_command_instance      instance of `Magics <http://ipython.readthedocs.io/en/stable/api/generated/IPython.core.magic.html#IPython.core.magic.Magics>`_,
                                            see `Defining your own magics <http://ipython.readthedocs.io/en/stable/config/custommagics.html?defining-custom-magics>`_
    @return                                 value

    The function raises an exception if the context does not exists
    or if the variable name does not value

    .. faqref::
        :tag: jupyter
        :title: Accéder ou modifier une variable du notebook depuis une commande magique

        Lorsqu'on écrit un notebook, toutes les variables qu'on crée sont
        en quelque sorte globales puisqu'on peut y accéder depuis chaque cellule
        mais leur périmètre est limité au notebook.
        Lorsqu'on crée un commande magique, il est possible d'accéder à ce contexte local
        via le membre ``self.shell.user_ns``. De cette façon, on peut accéder au contenu d'une
        variable, le modifier ou en ajouter une.

        ::

            class CustomMagics(Magics):

                @line_magic
                def custom_cmd(self, line):
                    context = self.shell.user_ns
                    #...
    """
    if magic_command_instance.shell is None:
        raise Exception(
            "no context, you probably execute this function outside a notebook")
    if name not in magic_command_instance.shell.user_ns:
        raise KeyError("variable {0} not found".format(name))
    return magic_command_instance.shell.user_ns[name]


def jupyter_open_notebook(filename, profile='default', fLOG=fLOG):
    """
    Calls @see fn nb_open, open a notebook with an existing server,
    if no server can be found, it starts a new one
    (and the function runs until the server is closed)

    @param      filename        notebook
    @param      profile         profile to use
    @param      fLOG            logging function
    @return                     a running server or None if not found

    .. faqref::
        :tag: jupyter
        :title: Lancer le serveur de notebooks
        :lid: i-launch_notebook-server

        On suppose que le module `Jupyter <http://jupyter.org/notebook.html>`_ a été bien installé.
        Depuis août 2015, IPython est devenu Jupyter qui n'est pas plus automatiquement
        associé à Python mais propose des notebooks pour de nombreux langages.
        Il faut installer le module *jupyter* (``pip install jupyter``).
        Plusieurs options :

        #. Utiliser la ligne de commande usuelle : ``jupyter-notebook``.
           Ce script (ou programme *jupyter-notebook.exe* sous Windows
           est inclus dans le répertoire *Scripts* du répertoire d'installation.
           Voir :ref:`l-jupyter_notebook_commandline`.
           Voir égalemnt `Travailler avec IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_,
           `Open the notebook with a different browser <http://www.xavierdupre.fr/blog/2015-08-24_nojs.html>`_
           Il est possible de créer un fichier `.bat <https://fr.wikipedia.org/wiki/.bat>`_ pour
           automatiser la ligne de commande et l'ajouter en tant qu'icône sur le bureau.

        #. Utiliser la fonction :func:`jupyter_open_notebook <ensae_teaching_cs.faq.faq_jupyter.jupyter_open_notebook>` ::

            from ensae_teaching_cs.faq import jupyter_open_notebook
            nbfile = "notebook.ipynb"
            jupyter_open_notebook(nbfile)

        #. Utiliser le raccourci proposé par la distribution choisi pour installer Python.

    .. faqref::
        :tag: jupyter
        :title: Le notebook ne répond plus

        On utilise les notebooks via un
        `navigateur web <https://fr.wikipedia.org/wiki/Navigateur_web>`_
        mais ce n'est pas lui qui exécute le code Python, c'est un serveur.
        Ce serveur tourne soit une machine distante, soit une machine locale.
        Il s'agit d'une fenêtre terminale où l'on peut voir des informations
        s'afficher à chaque qu'on ouvre, qu'on ferme, qu'on enregistre un notebook.
        Si cette fenêtre est fermée, il n'existe plus de serveur de notebook qui
        puisse exécuter le code inclus dans le notebook. Il ne se passe plus rien,
        les modifications sont perdues.
        Il faut redémarrer le serveur, qu'il soit distant ou local.
    """
    return nb_open(filename, profile, fLOG)
