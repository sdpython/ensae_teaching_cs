

.. _question_2014:

Questions TD 2014
=================

.. _question_1A_2014_1:


Question à propos de trie
+++++++++++++++++++++++++

**question**

Il s'agit de reproduire à l'aide de dictionnaires un trie.
Voici le code que vous avez donné et qui effectivement fonctionne à merveille ::

    def build_trie(mots) :
        trie = { }
        for m in mots :
            r = trie
            for c in m :
                if c not in r : r[c] = { }
                r = r[c]
        return trie

Cependant, je ne comprends pas très bien comment il fait pour tourner ! 
A quel moment est ce que l'on modifie le dictionnaire ``trie`` défini 
initialement comme ``{}`` ? Pour moi, pour chaque ``m`` dans ``mots``, 
on ne fait que créer une copie nommée ``r`` de trie, 
c'est à dire au début ``{}``, puis on réalise des opérations 
sur ce ``r`` que l'on modifie en cours de route, et à la fin de ces opérations, 
on passe au mot suivant en créant une nouvelle copie ``r`` de ``trie``, 
à savoir toujours ``{}`` !

**réponse**

Il existe un bon moyen de visualiser l'exécution, c'est le site
`Python Tutor <http://pythontutor.com/>`_. En recopiant, l'exemple suivant,
on peut suivre pas à pas l'exécution ::

    def build_trie(mots) :
        trie = { }
        for m in mots :
            r = trie
            for c in m :
                if c not in r : r[c] = { }
                r = r[c]
        return trie
    mots = [ "aaa", "aba", "aab", "baa", "bbb", "bba", "bab" ]
    trie = build_trie(mots)
    print(trie)

A chaque nouveau mot, les premiers caractères vont probablement faire déjà partie du
trie, les derniers vont être ajoutés au bout d'une branche existante. La question
est comment trouver cette branche. Cette branche peut avoir une longueur
variable.

.. image:: wiki_trie2.png

Pour trouver cette branche, le mécanisme qu'on utilise est très proche
de celui qu'on uilise pour se déplacer dans une 
`liste chaînée <http://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e>`_.

Dans une liste chaînée, il n'y a pas d'indice pour un élément. Chaque élément
pointe sur le suivant (il est conseillé d'utiliser 
`Python Tutor <http://pythontutor.com/>`_ pour visualiser l'exécution) ::

    class liste_chainee :

        def __init__ (self, value):
            self.value = value
            self.next = None
            
        def attache(self, element):
            self.next = element
            
        def atteindre_la_fin(self):
            position_courante = self
            if position_courante.next is not None:
                position_courante = position_courante.next
            return position_courante
            
    e0 = liste_chainee (0)
    e1 = liste_chainee (1)
    e2 = liste_chainee (2)
    e0.attache(e1)
    e1.attache(e2)
            
    fin = e0.atteindre_la_fin()
    print(fin.value)
        
Cet exemple est plus simple car pour se déplacer du début à la fin, il n'y 
qu'une seule *direction* : soit on est à la fin, soit il faut continuer
car il y a un élément suivant (``next`` n'est pas ``None``).

Toutefois, le programme précédent montre qu'il faut utiliser une 
variable ``position_courante`` qui mémorise la position
à laquelle on se trouve lorsqu'on parcours la liste.
Pour avancer, on exécute simplement ::
    
    position_courante = position_courante.next
    
La position courante devient la suivante. Dans le cas du trie, cette
instruction change car l'élément suivant dépend du caractère ``c`` ::

    r = r[c]
    
Le premier code comprend deux éléments :

    * le fait de se promener le long d'un chemin ::
    
        r = trie  # initialisation
        r = r[c]  # on avance d'un cran
        
    * le fait d'ajouter un caractère au trie ::
    
        r[c] = { }
        
Le caractère ``c`` a été ajouté au trie en tant que clé d'un dictionnaire,
lui-même valeur d'un dictionnaire associé à une clé égale
au caractère précédent dans le mot qu'on est en train d'ajouter.

**suite**

Lorsque l'on crée un dictionnaire, appelons le "a", puis que l'on en crée 
une autre copie, que l'on appelle "b", et que l'on modifie b, 
alors a se retrouve modifié ! Le dictionnaire ``b`` est en fait plus qu'une copie, 
mais une deuxième entité qui code le même objet, 
et je crois que c'est ca que je n'avais pas compris.

Par ailleurs, ce qui est surprenant, c'est que ceci ne fonctionne 
qu'avec les dictionnaires ! Lorsque l'on execute ceci ::

    a=[]
    b=a
    b = b+[2]
    print(a)

Alors la sortie est ``[]``. Quand on execute ceci ::

    a={}
    b=a
    b[1]=1
    print(a)

La réponse est ``{1 : 1}``.

**réponse**

Ceci est une propriété des listes et des dictionnaires qui sont des objets **mutable** en Python.
Je renvoie à la page `Qu’est-ce qu’un type immuable ou immutable ? <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/all_FAQ.html#qu-est-ce-qu-un-type-immuable-ou-immutable>`_
pour comprendre ce que sont ces deux propriétés en particulier.

Les listes sont **mutable**. Donc si on écrit ``b = a``, on crée un second identifiant pour accéder 
à la même liste. Voici pourquoi écrire ``a[0]=1`` a le même effet que ``b[0]=1``. 
Toutefois, dans le cas où ``b`` désigne une copie de la liste ``a``, ces deux instructions
n'auront pas les mêmes conséquences. Pour comprendre le résultat, il faut se demander
dans quel cas, on ne fait de copie, dans quel autre une copie a été créée.

L'instruction ``b=a`` ne crée pas de copie. L'instuction ``b=b+[2]`` construit 
la concaténation de deux listes, c'est donc une nouvelle liste qu'on affecte à ``b``.
Dans l'exemple suivant, ce n'est plus le cas même si le code paraît équivalent ::

    a=[]
    b=a
    b += [2]  # --> il n'y a plus de copie implicite
    print(a)  # --> affiche [2]
    
Le même exemple pour être écrit avec des dictionnaires car ils sont aussi **mutable**.

