# -*- coding: utf-8 -*-
"""
@file
@brief  quelques fonctions à propos de la séance 3

"""


def code_vigenere(message, cle, decode=False, binary=False):
    """
    Crypte et décrypte le code de Vigenère sachant la clé connue.

    @param      message     message à crypter ou décrypter
    @param      cle         clé du code
    @param      decode      False: crypte, True: décrypte
    @param      binary      code et décode en binaire
    @return                 le message crypté ou décrypté

    .. exref::
        :title: code de Vigenère
        :tag: Algorithme

        .. runpython::
            :showcode:

            def code_vigenere ( message, cle, decode = False) :
                message_code = ""
                for i,c in enumerate(message) :
                    d = cle[ i % len(cle) ]
                    d = ord(d) - 65
                    if decode : d = 26 - d
                    message_code += chr((ord(c)-65+d)%26+65)
                return message_code

            m = "JENESUISPASCODE"
            c = code_vigenere (m, "DOP")
            d = code_vigenere (c, "DOP", True)
            print(c, d)
    """
    if binary:
        if not isinstance(message, bytes):
            raise TypeError("message must be bytes")
        if not isinstance(cle, bytes):
            raise TypeError("cle must be bytes")

        message_code = []
        for i, c in enumerate(message):
            d = int(cle[i % len(cle)])
            if decode:
                d = 256 - d
            message_code.append((int(c) + d) % 256)
        return bytes(message_code)
    else:
        message_code = ""
        for i, c in enumerate(message):
            d = cle[i % len(cle)]
            d = ord(d) - 65
            if decode:
                d = 26 - d
            message_code += chr((ord(c) - 65 + d) % 26 + 65)
        return message_code


def DecodeVigenere(message, cle):
    return code_vigenere(message, cle, True)


def CodeVigenere(message, cle):
    return code_vigenere(message, cle)


def PGCD(m, n):
    """
    Détermine le PGCD de deux entiers.

    @param      m       premier entier
    @param      n       second entier
    @return             PGCD

    .. exref::
        :title: calcul du PGCD avec la méthode des soustractions
        :tag: Algorithme

        La fonction qui suit est l'implémentation en Python de la méthode décrite
        ici :
        `Algorithme de calcul du PGCD par soustractions successives <http://www.kartable.fr/terminale-s/mathematiques/1640/exercice/algorithme-de-calcul-du-pgcd-par-soustractions-successives,TS01505>`_.

        .. runpython::
            :showcode:

            def PGCD (m,n) :
                if m == 1 or n == 1 : return 1
                if m == n : return m
                if m < n : return PGCD (m, n-m)
                return PGCD (n, m-n)

            print(PGCD(50, 40))
    """
    if m <= 0 or n <= 0:
        raise Exception("impossible de calculer le PGCD")
    if m == 1 or n == 1:
        return 1
    if m == n:
        return m
    if m < n:
        return PGCD(m, n - m)
    return PGCD(n, m - n)


def DecodeVigenereLongueurCle(message, mot=3):
    """
    Cette fonction determine la longueur de la clé, elle
    repère les groupes de trois lettres qui se répète dans le message codé
    et suppose qu'il y a une très forte probabilité qu'un même groupe de trois
    lettres soit codé avec les mêmes trois lettres du message et les mêmes trois
    lettres de la clé.

    ::

        message  : .....DES...........DES...........DES.........DES....DES
        cle      : ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD
        code     : .....EGV.........................EGV.........EGV..........
        distance :      <----------24--------------><----8----->

    La longueur de la clé divise le *PGCD* de 24 et 8.

    @param      message     message codé
    @param      mot         longueur des séquences de lettres consécutifs dont on étudie la féquence
    @return                 longueur probable de la clé
    """
    al = "".join([chr(97 + i)
                  for i in range(0, 26)])  # l'alphabet en minuscule
    al = al.upper()

    # parcours du message pour recenser toutes les positions
    dico = {}
    for i in range(0, len(message) - 2):
        t = message[i:i + mot]
        if t in dico:
            dico[t].append(i)
        else:
            dico[t] = [i]

    # on va garder toutes les distances entre
    # entre deux occurrences du meme mot de n lettres
    dis = []
    for d in dico:
        p = dico[d]
        if len(p) > 1:
            for i in range(0, len(p) - 1):
                # print d, p [i+1] - p [i], " --- ", float (p [i+1] - p [i]) /
                # 8
                dis.append(p[i + 1] - p[i])

    # on extrait le PGCD
    if len(dis) == 0:
        raise Exception("impossible de determiner la clé")

    if len(dis) == 1:
        return dis[0]

    longueur = PGCD(dis[0], dis[1])
    for d in dis:
        longueur = PGCD(longueur, d)

    if longueur > 5:
        # si la longueur est suffisante, le resultat a des chances d'etre bon
        return longueur
    else:
        # sinon, on relance l'algorithme avec des mots plus grand
        return DecodeVigenereLongueurCle(message, mot + 1)


def DecodeVigenereCle(code, l):
    """
    Détermine la cle du message code, connaissant sa longueur,
    on suppose que la lettre E est la lettre la plus fréquente

    @param      code        message codé
    @param      l           longueur probable de la clé
    @return                 message décodé
    """
    al = "".join([chr(97 + i)
                  for i in range(0, 26)])  # l'alphabet en minuscule
    al = al.upper()
    cle = ""
    for i in range(0, l):
        nombre = [0 for a in al]
        sous = code[i:len(code):l]  # on extrait toutes les lettres
        # i, i+l, i+2l; i+3l, ...

        # on compte les lettres
        for k in sous:
            nombre[al.find(k)] += 1

        # on cherche le maximum
        p = 0
        for k in range(0, len(nombre)):
            if nombre[k] > nombre[p]:
                p = k

        # on suppose que al [p] est la lettre E code,
        # il ne reste plus qu'a trouver la lettre de la cle
        # qui a permis de coder E en al [p]
        cle += al[(p + 26 - al.find("E")) % 26]

    return cle


def CasseVigenere(message):
    """
    Appelle les deux fonctions @see fn DecodeVigenereLongueurCle et
    @see fn DecodeVigenereCle pour casser le code de Vigenère.

    @param      message     message codé
    @return                 message décodé (sans la clé)
    """
    ld = DecodeVigenereLongueurCle(message)
    cle = DecodeVigenereCle(message, ld)
    decode = DecodeVigenere(message, cle)
    return decode
