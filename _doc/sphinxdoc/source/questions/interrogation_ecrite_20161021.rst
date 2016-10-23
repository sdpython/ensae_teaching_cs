



2016-2017 - Interrogation écrite - 21 octobre 2016
==================================================

L'évaluation de mi-parcours consiste à écrire un programme python qui reproduit un motif.
Ce dernier est accessible via un url calculé avec le code suivant :

::

    def get_code(mail):
        import hashlib
        m = hashlib.md5()
        m.update(mail)
        b = m.digest()
        return int(b[0])

    code = get_code(u"machin@ensae.fr")
    url = "http://www.xavierdupre.fr/enseignement/examens/1A_2016/enonce_%d.txt" % code
    print(url)

Votre navigateur fera apparaître un motif comme celui-ci :

::

    ***
    ***
    ***
     ***
      ***
       ***
        *** H
       ***
      ***
     ***
    ***
    ***
    ***

Voici le programme qui reproduit ce motif :

::

    for i in range(0, 3):
        print("***")
    for i in range(0, 7):
        s = " " * (4 - abs(i-3)) + "***"
        if i == 3:
            s += " H"
        print(s)
    for i in range(0, 3):
        print("***")

Les règles sont simples :

* (presque) chaque élève a un motif différent.
* Le programme ne doit pas contenir de commentaires ni de lignes blanches.
* Le programme ne doit pas contenir deux "print" consécutifs.
* Le nombre de lignes du programme doit être strictement plus court que le nombre de lignes du motif.
* La longueur de la somme des chaînes de caractères incluses dans le programme doit être
  inférieur à la longueur du motif.
  
Vous aurez l'occasion de poser toute question relative à cet énoncé à votre chargé de TD. 
Vous devrez rendre votre programme par mail à votre chargé de TD et à moi-même en pièce jointe pour le 
4 novembre. Cette évaluation est notée sur 5 points.

Plus précisèment pour cet exercice, des points seront retranchés si :

* -1 point si le programme en pièce jointe ne fonctionne pas.
* -1 point par contrainte non respectée (voir ci-dessus)
* -1 point si la sortie est différente du motif qui vous est associé.

J'accorde 10 points supplémentaires à quiconque est capable de générer les 256 motifs en 
moins de 120 lignes. La solution est disponible sur github
`ensae_teaching_cs/encrypted <https://github.com/sdpython/ensae_teaching_cs/tree/master/src/ensae_teaching_cs/encrypted>`_.
Je précise pour tous ceux qui cliquent que la couleur du cheval cryptée d'Henri IV est cryptée.
J'accorde 6 points supplémentaires à quiconque est capable de casser le code.


Détails pour ceux qui souhaiteraient casser le code
+++++++++++++++++++++++++++++++++++++++++++++++++++

Le test unitaire qui test le programme crypté - donc qui le décrypte -, est implémenté dans le fichier
`_unittests/ut_encrypted/test_exam_2016_1A.py <https://github.com/sdpython/ensae_teaching_cs/blob/master/_unittests/ut_encrypted/test_exam_2016_1A.py#L109>`_.
Certains élèves m'ont demandé s'il était possible de casser le code. La réponse est vraisembablement négative
à moins de casser le code `AES <https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard>`_ 
utilisé pour crypter le programme ou de découvrir le mot de passe qui n'est pas si compliqué que cela.
Le chiffrement est effectué par la fonction 
`encrypt_stream <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/filehelper/encryption.html?highlight=encrypt#pyquickhelper.filehelper.encryption.encrypt_stream>`_.
La fonction impose que la longueur de la clé soit un multiple de 16 octets. J'ai choisi une longueur de 16.
Enfin, j'ai ajouté une seconde version cryptée avec le code de Vigenère et une clé qui contient entre 1 et 16 caractères.
Ce module contient quelques bout de code capable de décypter le code Vigenère dans le module
:mod:`ensae_teaching_cs.td_1a.vigenere`. Celui-ci ne s'appliquera pas directement sur le fichier
crypté. Il faudra jouer avec les types 
`str <https://docs.python.org/3/library/stdtypes.html#str>`_ et 
`bytes <https://docs.python.org/3/library/functions.html#bytes>`_. 
Il faudra aussi peu-être utiliser des notions de `n-grammes <https://fr.wikipedia.org/wiki/N-gramme>`_
et de `perplexité <https://en.wikipedia.org/wiki/Perplexity>`_.



