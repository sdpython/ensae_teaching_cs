"""
@file
@brief simple simulation of an epidemic
"""
import random
import copy
from pyquickhelper.loghelper import noLOG
from ..helpers.pygame_helper import wait_event


class Point:
    """
    defines a point
    """

    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point(self.x * p, self.y * p)

    def __div__(self, p):
        return Point(self.x / p, self.y / p)

    def __iadd__(self, p):
        self.x += p.x
        self.y += p.y
        return self

    def __isub__(self, p):
        self.x -= p.x
        self.y -= p.y
        return self

    def __imul__(self, p):
        self.x *= p
        self.y *= p
        return self

    def __idiv__(self, p):
        self.x /= p
        self.y /= p
        return self


class Rect:
    """
    defines a rectangle
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def limit(self, pos):
        r = False
        if pos.x < self.a.x:
            pos.x = self.a.x
            r = True
        if pos.y < self.a.y:
            pos.y = self.a.y
            r = True
        if pos.x > self.b.x:
            pos.x = self.b.x
            r = True
        if pos.y > self.b.x:
            pos.y = self.b.y
            r = True
        return r


class Person:
    """
    defines a person for the simulation

    colors

    * 0: sain
    * 1: malade
    * 2: mort
    * 3: gueris
    """
    colors = {0: (255, 255, 255), 1: (0, 255, 0),
              2: (0, 0, 0), 3: (50, 50, 200)}

    def __init__(self, position, borne_pos=None, borne_acc=None,
                 alea_acc=5, sick_vit=0.25, rayon=10, nb_day=70,
                 prob_die=0.5, prob_cont=0.5):
        """
        constructor

        @param      position        position
        @param      borne_pos       l
        @param      borne_acc       l
        @param      alea_acc        l
        @param      sick_vit        l
        @param      rayon           l
        @param      nb_day          l
        @param      prob_die        l
        @param      prob_cont       l
        """
        self.pos = position
        self.vit = Point(0, 0)
        self.acc = Point(0, 0)
        self.state = 0
        self.alea_acc = alea_acc
        self.borne_pos = borne_pos
        self.borne_acc = borne_acc

        self.sick_vit = sick_vit
        self.rayon = rayon
        self.nb_day = nb_day
        self.prob_die = prob_die
        self.prob_cont = prob_cont

        self._since = 0

    def __str__(self):
        return str(self.__dict__)

    def distance(self, p):
        d = self.pos - p.pos
        return d.norm()

    def _get_new_acceleration(self, population):
        x = random.gauss(0, self.alea_acc)
        y = random.gauss(0, self.alea_acc)
        # print x,y
        #res = self.acc + Point (x,y)
        res = Point(x, y)
        if self.borne_acc is not None:
            r = self.borne_acc.limit(res)
            if r:
                self.acc = Point(0, 0)
                self.vit = Point(0, 0)
        return res

    def state_evolution(self, population):
        if self.state in [2, 3]:
            return
        elif self.state == 1:
            if self._since < self.nb_day:
                self._since += 1
            else:
                k = random.random()
                if k < self.prob_die:
                    self.state = 2
                else:
                    self.state = 3
                    self._since = 0
        elif self.state == 0:
            all = []
            for p in population:
                if p.state != 1:
                    continue
                d = self.distance(p)
                if d <= self.rayon:
                    all.append(p)

            for k in all:
                p = random.random()
                if p <= self.prob_cont:
                    self.state = 1
                    break
        else:
            raise Exception("impossible")

    def evolution(self, dt, population):
        """
        update the population, random acceleration
        """
        self.state_evolution(population)

        if self.state == 1:
            dt *= self.sick_vit
        elif self.state == 2:
            dt = 0

        self.pos += self.vit * dt
        self.vit += self.acc * dt
        self.acc = self._get_new_acceleration(population)
        if self.borne_pos is not None:
            r = self.borne_pos.limit(self.pos)
            if r:
                self.acc = Point(0, 0)
                self.vit = Point(0, 0)


class EpidemicPopulation:
    """
    defines a population
    """

    def __init__(self, cote=500, nb=(100, 1), **params):
        """
        constructeur

        @param      cote        size of the zone person move
        @param      nb          tuple number of people (healthy, sick)
        @param      params      others parameters

        On tire au hasard les gens

        """
        if cote is None:
            pass
        else:
            self.cote = cote
            self.gens = []
            for i in range(0, nb[0]):
                p = Person(Point(random.randint(0, cote), random.randint(0, cote)),
                           Rect(Point(0, 0), Point(cote, cote)),
                           **params)
                self.gens.append(p)
            for i in range(0, nb[1]):
                p = Person(Point(random.randint(0, cote), random.randint(0, cote)),
                           Rect(Point(0, 0), Point(cote, cote)),
                           **params)
                p.state = 1
                self.gens.append(p)

    def __getitem__(self, i):
        return self.gens[i]

    def __iter__(self):
        return self.gens.__iter__()

    def __len__(self):
        return len(self.gens)

    def count(self):
        """
        return the distribution of healthy, sick, cured people
        """
        d = {}
        for p in self:
            s = p.state
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return d

    def evolution(self, dt=0.5):
        """
        iteration

        @param          dt      dt
        @return                 nb1,nb2
        """

        # on renouvelle une certaine proportion de pates (renouvellement)
        # tire au hasard
        pop = copy.deepcopy(self)
        for p in self.gens:
            p.evolution(dt, pop)
        return self.count()


def display_person(self, screen, pygame):
    c = Person.colors[self.state]
    pygame.draw.rect(screen, c, pygame.Rect(
        self.pos.x - 4, self.pos.y - 4, 8, 8))


def display_population(self, screen, pygame, font, back_ground):
    """
    affichage

    @param      screen      screen
    """
    screen.fill(back_ground)
    for p in self.gens:
        display_person(p, screen, pygame)
    c = self.count()
    text = "vie: %d" % c.get(0, 0)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (self.cote, 100))
    text = "malade: %d" % c.get(1, 0)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (self.cote, 135))
    text = "mort: %d" % c.get(2, 0)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (self.cote, 170))
    text = "gueris: %d" % c.get(3, 0)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (self.cote, 205))


def pygame_simulation(pygame):

    nb = (200, 20)
    iter = 1000
    cote = 600

    pygame.init()
    size = cote + 200, cote
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font("freesansbold.ttf", 30)
    back_ground = (128, 128, 128)

    pop = EpidemicPopulation(cote, nb)

    display_population(pop, screen, pygame, font, back_ground)
    pygame.display.flip()
    wait_event(pygame)
    print(pop.count())

    for i in range(0, iter):
        nb = pop.evolution()
        if i % 10 == 0:
            print("iteration ", i, " pop ", nb)
        display_population(pop, screen, pygame, font, back_ground)
        pygame.display.flip()
        #pygame.image.save (screen, "c:/temp/epidemie_%03d.jpg" %i)
        pygame.event.peek()
        pygame.time.wait(50)
        if 1 not in nb or nb[1] == 0:
            break

    print(pop.count())
    wait_event()


def simulation(nb=(200, 20), cote=600, iter=1000, fLOG=noLOG, **params):
    """
    run a simulation, @see cl EpidemicPopulation
    """
    pop = EpidemicPopulation(cote, nb, **params)

    for i in range(0, iter):
        nb = pop.evolution()
        if 1 not in nb or nb[1] == 0:
            break
        if i % 10 == 0:
            fLOG("iteration", i, ":", nb)

    r = pop.count()
    return r, i


def numeric_simulation():

    cote = 600

    for val in [0.01 * i for i in range(0, 101)]:
        print("val\t", val * 10, "\t",)
        values = simulation(nb=(100 - int(val * 100), int(val * 100)),
                            cote=cote, display=False)
        print(values)
