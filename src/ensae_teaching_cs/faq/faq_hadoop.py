# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions autour de Hadoop

"""

def putty_different_python():
    """
    FAQ(hadoop___La version de Python est différente dans putty)
    
    .. index:: putty, SSH, vi, nano
    
    Lorsqu'on ouvre une fenêtre `putty <http://www.putty.org/>`_,
    on crée une passerelle vers une autre machine, le plus souvent linux.
    Ce qu'on voit à l'intérieur de la fenêtre est la ligne de commande de cette machine.
    Ce n'est pas vraiment la ligne de commande mais plutôt une représentation.
    Les commandes sont envoyés à la machine distance via le protocole SSH.
    Je renvoie au :ref:`TD Map/Reduce avec PIG <td3acenoncesession6rst>`
    qui montre comment se server de putty pour envoyer des commandes vers le cluster.
    Il est aussi possible de créer sa propre fenêtre putty à l'intérieur
    d'un notebook 
    (voir `Communication with a remote Linux machine through SSH <http://www.xavierdupre.fr/app/pyensae/helpsphinx/notebooks/example_of_ssh_client_communication.html>`_).
    
    *Mais comment fait-on pour exécuter un script python sur la machine distance ?*
    
    Deux options. On l'écrit sur sa machine locale avec l'éditeur 
    dont on a l'habitude puis on transfère le fichier sur la machine distante
    pour l'exécuter avec la commande ::
    
        python <fichier.py>
        
    La seconde option consiste à ouvrir un édieur de texte à l'intérieur
    de la fenêtre putty. Tout se fait avec des raccourcis puisque
    la souris est inutilisable. On peut utiliser les éditeurs
    `vi <http://ss64.com/vi.html>`_ ou `nano <http://www.nano-editor.org/dist/v2.2/nano.html>`_.
    
    Une astuce : pour éviter de sortir de l'éditeur nano ou vi à chaque
    fois qu'on souhaite exécuter le script, il suffit d'ouvrir une seconde fenêtre
    putty. La première sert à éditer, la seconde à exécuter le script.
    
    @endFAQ
    """
    pass

