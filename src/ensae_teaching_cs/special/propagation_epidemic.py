"""
@file
@brief Simple simulation of an epidemic. It makes a couple of assumption
on how the disease is transmitted and its effect on a person. The user
can specify many parameters.
"""
import random
import copy
import os
from collections import Counter
from pyquickhelper.loghelper import noLOG
from ..helpers.pygame_helper import wait_event, empty_main_loop


class Point:
    """
    Defines a point.
    """

    def __init__(self, x, y):
        """
        constructor

        @param      x       x
        @param      y       y
        """
        self.x, self.y = float(x), float(y)

    def norm(self):
        """
        return the norm l2
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, p):
        """
        addition
        """
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        """
        soustraction
        """
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        """
        multiplication by a scalar
        """
        return Point(self.x * p, self.y * p)

    def __div__(self, p):
        """
        division by a scalar
        """
        return Point(self.x / p, self.y / p)

    def __iadd__(self, p):
        """
        addition inplace
        """
        self.x += p.x
        self.y += p.y
        return self

    def __isub__(self, p):
        """
        soustraction inplace
        """
        self.x -= p.x
        self.y -= p.y
        return self

    def __imul__(self, p):
        """
        multiplication by a scalar inplace
        """
        self.x *= p
        self.y *= p
        return self

    def __idiv__(self, p):
        """
        divsion by a scalar inplace
        """
        self.x /= p
        self.y /= p
        return self


class Rect:
    """
    Defines a rectangle.
    """

    def __init__(self, a, b):
        """
        constructor

        @param      a       Point
        @param      b       Point
        """
        self.a = a
        self.b = b

    def limit(self, pos):
        """
        tells if point *pos* belongs to the area
        defined by the rectangle
        """
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

    A person moves by drawing a random gaussian vector added to
    its current acceleration.
    """
    colors = {0: (255, 255, 255), 1: (0, 255, 0),
              2: (0, 0, 0), 3: (50, 50, 200)}

    def __init__(self, position, borne_pos=None, borne_acc=None,
                 alea_acc=5, sick_vit=0.25, rayon=10, nb_day=70,
                 prob_die=0.5, prob_cont=0.5):
        """
        constructor

        @param      position        position
        @param      borne_pos       upper bound for the position (rectangle)
        @param      borne_acc       upper bound for the acceleration (rectangle)
        @param      alea_acc        sigma to draw random acceleration
        @param      sick_vit        when people are sick, they go slower, this muliplies
                                    the acceleration by a factor
        @param      rayon           radius, below that distance, a sick person is contagious for the neighbours
        @param      nb_day          number of days a person will be sick, after, the person
                                    either recovers, either dies
        @param      prob_die        probability to die at each iteration
        @param      prob_cont       probability to transmit the disease to a neighbour
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

        # memorize the day the person got sick
        self._since = 0

    def __str__(self):
        """
        usual
        """
        return str(self.__dict__)

    def distance(self, p):
        """
        return the distance between this person and another one
        """
        d = self.pos - p.pos
        return d.norm()

    def _get_new_acceleration(self):
        """
        update the acceleration by adding a random gaussian vector
        to the current acceleration, check that acceleration
        is not beyond some boundary
        """
        x = random.gauss(0, self.alea_acc)
        y = random.gauss(0, self.alea_acc)
        res = Point(x, y)
        if self.borne_acc is not None:
            r = self.borne_acc.limit(res)
            if r:
                self.acc = Point(0, 0)
                self.vit = Point(0, 0)
        return res

    def state_evolution(self, population):
        """
        update the state of the person: healthy --> sick --> cured or dead

        @param  population      sets of other persons

        The function updates the state of the persons.
        One of steps involves looking over the entire population to check
        if some sick people are close enough to transmis the disease.
        """
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
            alls = []
            for p in population:
                if p.state != 1:
                    continue
                d = self.distance(p)
                if d <= self.rayon:
                    alls.append(p)

            for k in alls:
                p = random.random()
                if p <= self.prob_cont:
                    self.state = 1
                    break
        else:
            raise Exception("impossible")

    def evolution(self, dt, population):
        """
        update the population, random acceleration

        @param      dt          time delta (only used to update the position)
        @param      population  other set of people

        The function updates the state of the person,
        draws a new acceleration and updates the position.
        """
        self.state_evolution(population)

        if self.state == 1:
            dt *= self.sick_vit
        elif self.state == 2:
            dt = 0

        self.pos += self.vit * dt
        self.vit += self.acc * dt
        self.acc = self._get_new_acceleration()
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

        Draws a population.
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
        """
        usual
        """
        return self.gens[i]

    def __iter__(self):
        """
        usual
        """
        return self.gens.__iter__()

    def __len__(self):
        """
        usual
        """
        return len(self.gens)

    def count(self):
        """
        return the distribution of healthy, sick, cured people
        """
        return Counter(map(lambda p: p.state, self))

    def evolution(self, dt=0.5):
        """
        new iteration

        @param          dt      dt
        @return                 nb1,nb2

        We walk through everybody and call
        :meth:`evolution <ensae_teaching_cs.special.propragation_epidemics.Person.evolution>`.
        """

        # on renouvelle une certaine proportion de pates (renouvellement)
        # tire au hasard
        pop = copy.deepcopy(self)
        for p in self.gens:
            p.evolution(dt, pop)
        return self.count()


def display_person(self, screen, pygame):
    """
    display a person on a pygame screen

    @param      self        Person
    @param      screen      screen
    @param      pygame      module pygame
    """
    c = Person.colors[self.state]
    pygame.draw.rect(screen, c, pygame.Rect(
        self.pos.x - 4, self.pos.y - 4, 8, 8))


def display_population(self, screen, pygame, font, back_ground):
    """
    affichage

    @param      self            Person
    @param      screen          screen
    @param      font            font (pygame)
    @param      back_ground     back ground color
    @param      pygame          module pygame
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


def pygame_simulation(pygame, first_click=False, folder=None,
                      iter=1000, cote=600, nb=(200, 20), flags=0,
                      **params):
    """
    Run a graphic simulation. The user can a pygame screen showing
    the evolution of population. A healthy person is white, green is sick,
    blue is healed, black is dead. The function can save an image for
    every iteration. They can be merged into a video with
    function @see fn make_video.

    @param      pygame          module pygame (avoids importing in this file)
    @param      first_click     starts the simulation after a first click
    @param      folder          to save the simulation, an image per simulation
    @param      iter            number of iterations to run
    @param      cote            @see cl EpidemicPopulation
    @param      nb              @see cl EpidemicPopulation
    @param      params          @see cl EpidemicPopulation
    @param      flags           see `pygame.display.set_mode <https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode>`_
    @param      fLOG            logging function

    The simulation looks like this:

    .. raw:: html

        <video autoplay="" controls="" loop="" height="400">
        <source src="http://www.xavierdupre.fr/enseignement/complements/epidemic.mp4" type="video/mp4" />
        </video>

    Pour lancer la simulation::

        from ensae_teaching_cs.special.propagation_epidemic import pygame_simulation
        import pygame
        pygame_simulation(pygame)

    """
    pygame.init()
    size = cote + 200, cote
    screen = pygame.display.set_mode(size, flags)
    font = pygame.font.Font("freesansbold.ttf", 30)
    back_ground = (128, 128, 128)

    pop = EpidemicPopulation(cote, nb)
    display_population(pop, screen, pygame, font, back_ground)
    pygame.display.flip()
    if first_click:
        wait_event(pygame)

    for i in range(0, iter):

        empty_main_loop(pygame)
        nb = pop.evolution()
        display_population(pop, screen, pygame, font, back_ground)
        pygame.display.flip()
        pygame.event.peek()
        if folder is not None:
            image = os.path.join(folder, "image_%04d.png" % i)
            pygame.image.save(screen, image)
        pygame.time.wait(50)
        if 1 not in nb or nb[1] == 0:
            break

    if first_click:
        wait_event(pygame)


def numerical_simulation(nb=(200, 20), cote=600, iter=1000, fLOG=noLOG, **params):
    """
    Run a simulation, @see cl EpidemicPopulation.

    @param      iter            number of iterations to run
    @param      cote            @see cl EpidemicPopulation
    @param      nb              @see cl EpidemicPopulation
    @param      params          @see cl EpidemicPopulation
    @param      fLOG            to display status every 10 iterations
    @return                     population count
    """
    pop = EpidemicPopulation(cote, nb, **params)

    lasti = None
    for i in range(0, iter):
        nb = pop.evolution()
        lasti = i
        if 1 not in nb or nb[1] == 0:
            break
        if i % 10 == 0:
            fLOG("iteration", i, ":", nb)

    r = pop.count()
    return r, lasti
