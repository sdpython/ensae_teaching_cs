#-*- coding: utf-8 -*-
"""
@file
@brief This programs solves `Einstein's riddle <http://en.wikipedia.org/wiki/Zebra_Puzzle>`_ ou en
Français `Intégramme <http://fr.wikipedia.org/wiki/Int%C3%A9gramme>`_. The algorithm is based
on logic and its `clause <http://en.wikipedia.org/wiki/Clause_(logic)>`_.
"""
import copy


#: definition of all possible values (French terms)
#: colors
ttcouleur = ["jaune", "bleu", "rouge", "blanc", "vert"]
#: nationalities
ttnationalite = ["danois", "norvegien", "anglais", "allemand", "suedois"]
#: drinks
ttboisson = ["eau", "the", "lait", "cafe", "biere"]
#: smoke  brand
ttcigare = ["Dunhill", "Blend", "Pall Mall", "Prince", "Bluemaster"]
#: animal
ttanimal = ["chats", "cheval", "oiseaux", "poisson", "chiens"]

#: all possibles values
ensemble = [ttcouleur, ttnationalite, ttboisson, ttcigare, ttanimal]


def permutation(nb):
    """
    Compute all permutations of set [[ 1, 2, ..., nb ]].
    Example for 3:

    ::

        [[0, 1, 2], [0, 2, 1], [1, 0, 2],
        [1, 2, 0], [2, 0, 1], [2, 1, 0]]

    @param      nb      permutation over the set [[1..n]]
    @return             list of all possible permutations

    @warning  This method can be very long if nb is high (>10).

    This function does something very similar to `itertools.permutations <https://docs.python.org/3/library/itertools.html#itertools.permutations>`_.
    """
    per = []
    p = [i for i in range(0, nb)]
    while p[0] < nb:
        next = False
        for i in range(1, nb):
            if p[i] in p[0:i]:
                next = True
                break

        if not next:
            per.append(copy.copy(p))

        p[nb - 1] += 1
        for j in range(nb - 1, 0, -1):
            if p[j] >= nb:
                p[j] = 0
                p[j - 1] += 1

    return per


class Rule:

    """
    This class defines a constraint of the problem
    or a clause (see `http://en.wikipedia.org/wiki/Clause_(logic)`)

    There are 5 different types of clauses described by Einstein's enigma
    each of them is described by a different class. There are defined by classes:
    @ref cl RulePosition, @ref cl RuleEquivalence, @ref cl RuleVoisin,
    @ref cl RuleAvant, @ref cl RuleEnsemble.
    """

    def __init__(self):
        """
        constructor
        """
        #: name of the rule
        self.name = None
        #: set of clauses
        self.set = None

    def genere(self):
        """
        generates all possible clauses (list of lists)
        (l [0][0] et l [0][1]) ou (l [1][0] et l [1][1]),
        a clause is a triplet of
        (person, (property, category) )
        """
        return None

    def __str__(self):
        """
        display
        """
        if self.name is not None:
            if "clauses" not in self.__dict__:
                s = self.name + " \t: "
                a = self.genere()
                for al in a:
                    st = "\n       ou  " + str(al)
                    if len(st) > 260:
                        st = st[:260] + "..."
                    s += st
                    if len(s) > 1000:
                        break
                return s
            else:
                s = self.name + " \t: " + str(self.set)
                for al in self.clauses:
                    st = "\n       ou   " + str(al)
                    if len(st) > 260:
                        st = st[:260] + "..."
                    s += st
                    if len(s) > 1000:
                        break
                return s
        else:
            return None

    def combine(self, cl1, cl2):
        """
        combine two clauses, two cases :
            1. nothing in common or everything in common --> concatenation of clauses
            2. a position or a property in common --> null clause

        @param      cl1     clause 1
        @param      cl2     clause 2
        @return             the new clause

        A clause is a @ref cl Rule.
        """
        # incompatibility
        for p1 in cl1:
            for p2 in cl2:
                if p1[1][0] == p2[1][0]:  # same property
                    if p1[0] != p2[0]:  # but different positions
                        return None
                if p1[0] == p2[0]:  # same person
                    if p1[1][1] == p2[1][1] and p1[1][0] != p2[1][0]:
                        # same category but different properties
                        return None
        # compatibility
        r = copy.deepcopy(cl1)
        for c in cl2:
            if c not in r:
                r.append(c)
        return r

    def combine_cross_sets(self, set1, set2):
        """
        combines two sets of clauses
        @param      set1        set of clauses 1
        @param      set2        set of clauses 2
        @return                 combination
        """
        if len(set1) == 0:
            return copy.deepcopy(set2)
        if len(set2) == 0:
            return copy.deepcopy(set1)
        res = []
        for cl1 in set1:
            for cl2 in set2:
                r = self.combine(cl1, cl2)
                if r is not None:
                    res.append(r)
        return res


class RulePosition (Rule):

    """
    p1 at position
    """

    def __init__(self, p1, pos):
        """
        constructor
        """
        self.set = [p1]
        self.name = "position"
        self.position = pos

    def genere(self):
        """
        overrides method ``genere``
        """
        return [[(self.position, self.set[0])]]


class RuleEquivalence (Rule):

    """
    p1 equivalent to p2
    """

    def __init__(self, p1, p2):
        """
        constructor
        """
        self.set = [p1, p2]
        self.name = "equivalence"

    def genere(self):
        """
        overrides method ``genere``
        """
        l = []
        for i in range(0, 5):
            l.append([(i, self.set[0]), (i, self.set[1])])
        return l


class RuleVoisin (Rule):

    """
    p1 and p2 are neighbors
    """

    def __init__(self, p1, p2):
        """
        constructor
        """
        self.set = [p1, p2]
        self.name = "voisin"

    def genere(self):
        """
        overrides method ``genere``
        """
        l = []
        for i in range(0, 4):
            l.append([(i, self.set[0]), (i + 1, self.set[1])])
            l.append([(i + 1, self.set[0]), (i, self.set[1])])
        return l


class RuleAvant (Rule):

    """
    p1 before p2
    """

    def __init__(self, p1, p2):
        self.set = [p1, p2]
        self.name = "avant"

    def genere(self):
        """
        overrides method ``genere``
        """
        l = []
        for j in range(1, 5):
            for i in range(0, j):
                l.append([(i, self.set[0]), (j, self.set[1])])
        return l


class RuleEnsemble (Rule):

    """
    permutation of the elements of a category
    """

    def __init__(self, set, categorie):
        """
        constructor
        """
        self.set = [(s, categorie) for s in set]
        self.name = "ensemble"

    def genere(self):
        """
        overrides method ``genere``
        """
        l = []
        per = permutation(5)
        for p in per:
            tl = []
            for i in range(0, len(p)):
                tl.append((i, self.set[p[i]]))
            l.append(tl)
        return l


class Enigma:

    """
    this class solves the enigma
    """

    def __init__(self, display=True):
        """
        we describe the enigma using the classes we defined above
        @param      display     if True, use print to print some information
        """
        self.regle = []

        self.regle.append(RulePosition(self.find("lait"), 2))
        self.regle.append(RulePosition(self.find("norvegien"), 0))

        self.regle.append(
            RuleEquivalence(
                self.find("Pall Mall"),
                self.find("oiseaux")))
        self.regle.append(
            RuleEquivalence(
                self.find("anglais"),
                self.find("rouge")))
        self.regle.append(
            RuleEquivalence(
                self.find("suedois"),
                self.find("chiens")))
        self.regle.append(
            RuleEquivalence(
                self.find("danois"),
                self.find("the")))
        self.regle.append(
            RuleEquivalence(
                self.find("vert"),
                self.find("cafe")))
        self.regle.append(
            RuleEquivalence(
                self.find("jaune"),
                self.find("Dunhill")))
        self.regle.append(
            RuleEquivalence(
                self.find("biere"),
                self.find("Bluemaster")))
        self.regle.append(
            RuleEquivalence(
                self.find("allemand"),
                self.find("Prince")))

        self.regle.append(
            RuleVoisin(
                self.find("Dunhill"),
                self.find("cheval")))
        self.regle.append(
            RuleVoisin(
                self.find("norvegien"),
                self.find("bleu")))
        self.regle.append(RuleVoisin(self.find("Blend"), self.find("eau")))
        self.regle.append(RuleVoisin(self.find("Blend"), self.find("chats")))

        self.regle.append(RuleAvant(self.find("vert"), self.find("blanc")))

        self.regle.append(RuleEnsemble(ttcouleur, 0))
        self.regle.append(RuleEnsemble(ttnationalite, 1))
        self.regle.append(RuleEnsemble(ttboisson, 2))
        self.regle.append(RuleEnsemble(ttcigare, 3))
        self.regle.append(RuleEnsemble(ttanimal, 4))

        for r in self.regle:
            r.clauses = r.genere()
            r.utilise = False

        self.count = 0

    def find(self, p):
        """
        finds a clause in the different sets of clause (houses, colors, ...)

        @param      p       clause
        @return             tuple (clause, position)
        """
        for i in range(0, len(ensemble)):
            if p in ensemble[i]:
                return (p, i)
        return None

    def __str__(self):
        """
        usual
        """
        if "solution" not in self.__dict__ or self.solution is None or len(
                self.solution) == 0:
            if self.count > 0:
                s = "solution impossible apres " + \
                    str(self.count) + " iterations \n"
            else:
                s = ""
            for r in self.regle:
                s += str(r) + "\n"
            return s
        else:
            sr = ["solution, iteration " + str(self.count)]
            matrix = [list(" " * 5) for _ in range(0, 5)]
            for row in self.solution:
                i = row[0]
                j = row[1][1]
                s = row[1][0]
                matrix[i][j] = s + " " * (10 - len(s))
            for row in matrix:
                sr.append(", ".join(row))
            classic = "\n".join(sr[1:])
            html = classic.replace(",",
                                   "</td><tr>").replace("\n",
                                                        "</td></tr>\n<tr><td>")
            return sr[0] + "\n" + "\n".join([
                classic,
                "<table>",
                "<tr><td>" + html + "</td></tr>",
                "</table>"])

    def solve(self, solution=[], logf=print):  # solution = [ ]) :
        """
        Solves the enigma by eploring in deepness,
        the method is recursive

        @param      solution    [] empty at the beginning, recursively used then
        @return                 solution
        """

        self.count += 1
        if self.count % 10 == 0:
            logf(
                "*",
                self.count,
                " - properties in place : ",
                len(solution) -
                1)

        if len(solution) == 25:
            # we know the solution must contain 25 clauses,
            # if are here than the problem is solved unless some
            # incompatibility
            for r in self.regle:
                cl = r.combine_cross_sets([solution], r.clauses)
                if cl is None or len(cl) == 0:
                    # the solution is incompatible with a solution
                    return None
            self.solution = solution
            return solution

        # we are looking for the rule which generates the least possible clauses
        # in order to reduce the number of possibilities as much as possible
        # the research could be represented as a tree, we avoid creating two
        # many paths
        best = None
        rule = None

        for r in self.regle:

            cl = r.combine_cross_sets([solution], r.clauses)

            if cl is None:
                # the solution is incompatible with a solution
                return None

            # we check rule r is bringing back some results
            for c in cl:
                if len(c) > len(solution):
                    break
            else:
                cl = None

            if cl is not None and (best is None or len(best) > len(cl)):
                best = cl
                rule = r

        if best is None:
            # the solution is incompatible with a solution
            return None

        rule.utilise = True

        # we test all clauses
        for c in best:
            r = self.solve(c, logf=logf)
            if r is not None:
                # we found
                return r

        rule.utilise = False  # impossible
        return None

if __name__ == "__main__":
    en = Enigma()
    print(en)
    print("-----------------------------\n")
    en.solve()
    print("-----------------------------\n")
    print(en)
