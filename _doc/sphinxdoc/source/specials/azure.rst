

.. index:: azure, Microsoft, partenariat, azure sdk, sdk

.. _l-azurep:


Azure, Python, Programmation
============================


Pour l'année scolaire 2014-2015, des ressources Azure sont 
mises à disposition des élèves dans le cadre d'un `partenariat 
entre Microsoft et l'ENSAE <http://www.microsoft.com/france/Hub-Presse/communiques-de-presse/fiche-communique.aspx?eid=f7e7f695-fb08-4c6d-b4ec-3cde562ba429>`_.
Il existe différentes façons d'utiliser ces ressources. Les outils les plus avancés
sont proposés
`powershell <http://fr.wikipedia.org/wiki/Windows_PowerShell>`_ et 
`C# <http://fr.wikipedia.org/wiki/C_sharp>`_ même ils sont pour la plupart
adaptés au système d'exploitation Windows, moins pour Linux.
C'est pourquoi la plupart des exemples proposés le seront avec le langage 
Python qui utilise des modules portables d'un système à l'autre.
Les modules, accessible depuis le compte GitHub 
`github/Azure <https://github.com/Azure>`_, sont très jeunes et 
sont susceptibles d'évoluer dans un futur proche. 

* `azure-sdk-for-python <https://github.com/Azure/azure-sdk-for-python>`_ : accès au blob storage,
  `ServiceBus <http://azure.microsoft.com/fr-fr/services/service-bus/>`_
* `azure-documentdb-python <https://github.com/Azure/azure-documentdb-python>`_ : 
  accès au service `NoSQL <http://fr.wikipedia.org/wiki/NoSQL>`_ 
  (ou `Distributed Data Store <http://en.wikipedia.org/wiki/Distributed_data_store>`_)
* `azure-batch-apps-python <https://github.com/Azure/azure-batch-apps-python>`_ :  
  exécution de batch, création de machine virtuelles...
  
pyensae
+++++++

A ces modules est ajouté une surcouche présente dans 
`pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_.
Cette couche est minimale, elle sert à donner des exemples pour les 
usages les plus courants et à ajouter des commandes magiques dans 
les notebooks.

* `AzureClient <http://www.xavierdupre.fr/app/pyensae/helpsphinx/pyensae/remote/azure_connection.html>`_
* `commandes magiques <http://www.xavierdupre.fr/app/pyensae/helpsphinx/pyensae/remote/magic_azure.html>`_

Ce n'est pas très compliqué une fois qu'on a l'exemple mais il faut souvent
quelques essais et beaucoup de recherches pour trouver les 
exemples qui fonctionnent sur internet. 

L'exécution de job Pig est réalisé via l'API `WebHCat <http://docs.hortonworks.com/HDPDocuments/HDP1/HDP-1.2.1/bk_dataintegration/content/ch_using_hcatalog_1.html>`_ :

* `start a Pig + Jython job in HDInsight thru WebHCat <http://blogs.msdn.com/b/benjguin/archive/2014/03/21/start-a-pig-jython-job-in-hdinsight-thru-webhcat.aspx>`_
* `How to use HDInsight from Linux <http://blogs.msdn.com/b/benjguin/archive/2014/02/18/how-to-use-hdinsight-from-linux.aspx>`_
  
Documentation
+++++++++++++

* `azure-sdk-for-python <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/index.html>`_
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_


