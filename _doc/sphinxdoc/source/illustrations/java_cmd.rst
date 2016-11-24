

.. _l-java-cmd:

Ligne de commande java
======================

::

    Syntaxe : java [-options] class [args...]
               (pour l'exécution d'une classe)
       ou  java [-options] -jar jarfile [args...]
               (pour l'exécution d'un fichier JAR)
    où les options comprennent :
        -d32          utilisez le modèle de données 32 bits s'il est disponible
        -d64          utilisez le modèle de données 64 bits s'il est disponible
        -server       pour sélectionner la machine virtuelle "server"
                      La machine virtuelle par défaut est server.

        -cp <class search path of directories and zip/jar files>
        -classpath <class search path of directories and zip/jar files>
                      Liste de répertoires, d'archives JAR et
                       d'archives ZIP séparés par des ;, dans laquelle rechercher les fichiers de classe.
        -D<name>=<value>
                      définition d'une propriété système
        -verbose:[class|gc|jni]
                      activation de la sortie en mode verbose
        -version      impression de la version du produit et fin de l'opération
        -version:<value>
                      Avertissement : cette fonctionnalité est en phase d'abandon et sera enlevée
                      dans une version future.
                      exécution de la version spécifiée obligatoire
        -showversion  impression de la version du produit et poursuite de l'opération
        -jre-restrict-search | -no-jre-restrict-search
                      Avertissement : cette fonctionnalité est en phase d'abandon et sera enlevée
                      dans une version future.
                      inclusion/exclusion des environnements JRE privés de l'utilisateur dans la recherche de version
        -? -help      impression du message d'aide
        -X            impression de l'aide sur les options non standard
        -ea[:<packagename>...|:<classname>]
        -enableassertions[:<packagename>...|:<classname>]
                      activation des assertions avec la granularité spécifiée
        -da[:<packagename>...|:<classname>]
        -disableassertions[:<packagename>...|:<classname>]
                      désactivation des assertions avec la granularité spécifiée
        -esa | -enablesystemassertions
                      activation des assertions système
        -dsa | -disablesystemassertions
                      désactivation des assertions système
        -agentlib:<libname>[=<options>]
                      chargement de la bibliothèque d'agent natif <libname>, par exemple -agentlib:hprof
                      voir également, -agentlib:jdwp=help et -agentlib:hprof=help
        -agentpath:<pathname>[=<options>]
                      chargement de la bibliothèque d'agent natif via le chemin d'accès complet
        -javaagent:<jarpath>[=<options>]
                      chargement de l'agent du langage de programmation Java, voir java.lang.instrument
        -splash:<imagepath>
                      affichage de l'écran d'accueil avec l'image spécifiée

    Voir http://www.oracle.com/technetwork/java/javase/documentation/index.html pour plus de détails.
