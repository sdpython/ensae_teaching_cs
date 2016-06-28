# coding: cp1252
import pygame                 # pour les affichages
import math                   # pour les racines carrées


class point (object) :
    """définition d'un point : deux coordonnées et une masse"""
    __slots__ = "x","y","m"
    
    def __init__ (self, x,y,m) :
        """définit un point de la corde, de coordonnées (x,y)
        et de masse m"""
        self.x, self.y, self.m = float (x), float (y), float (m)
        
    def deplace (self, dep, dt) :
        """déplace un point"""
        self.x += dep [0] * dt
        self.y += dep [1] * dt
        
    def deplace_point (self, dep, dt) :
        """déplace un point"""
        self.x += dep.x * dt
        self.y += dep.y * dt
        
    def difference (self, p) :
        """retourne le vecteur qui relie deux points,
        retourne le couple de ses coordonnées"""
        return p.x - self.x, p.y - self.y
        
    def __str__ (self) :
        """afficher le point"""
        return "(x,y) = (%4.1f,%4.1f) masse %f" % (self.x,self.y,self.m)
        
class corde (object) :
    """définition d'une corde, une liste de points"""
    
    def __init__(self, nb, p1, p2, m, k, g, f, l) :
        """initialisation d'une corde
        @param          nb          nombre de points
        @param          p1 = x1,y1  coordoonnées du premier point (fixe)
        @param          p2 = x2,y2  coordoonnées du dernier point (fixe)
        @param          m           masse de la corde, 
                                    répartie entre tous les pointstous les points
        @param          k           raideur de l'élastique
        @param          g           intensité de l'apesanteur, 
                                    valeur positive
        @param          f           vitesse de freinage
        @param          l           longueur de la corde"""
        x1,y1           = p1[0], p1[1]
        x2,y2           = p2[0], p2[1]
        self.list       = []
        self.vitesse    = []
        for i in range (0,nb) :
            x = x1 + float (i) * (x2 - x1) / float (nb - 1)
            y = y1 + float (i) * (y2 - y1) / float (nb - 1)
            self.list.append ( point (x,y, float (m) / nb))
            self.vitesse.append (point (0,0,0))
        self.k = k * nb
        self.g = g
        self.l = float (l) / (nb-1)
        self.f = f
            
    def display (self, screen) :
        """affichage de la corde à l'aide du module pyagame"""
        self.display_courbe_theorique (screen)
        x,y     = screen.get_size ()
        color   = (0,0,0)
        for p in self.list :
            pygame.draw.circle (screen, color, (int (p.x), int (y - p.y)), int (p.m+1))
        for i in xrange (0,len (self.list)-1) :
            pygame.draw.line (screen, color, \
                            (int (self.list [i].x),      int (y - self.list [i].y)), \
                            (int (self.list [i+1].x),    int (y - self.list [i+1].y))) 
                            
    def display_courbe_theorique (self, screen) :
        
        def cosh (x) :
            """retourne le cosinus hyperbolique de x"""
            return math.cosh (x)
        
        def sinh (x) :
            """retourne le sinus hyperbolique de x"""
            return math.sinh (x)
            
        def asinh (x) :
            """retourne la réciproque du sinus hyperbolique de x"""
            t = x + math.sqrt (x*x + 1)
            return math.log (t)
        
        def acosh (x) :
            """retourne la réciproque du cosinus hyperbolique de x"""
            t = abs (x) + math.sqrt (x*x - 1)
            return math.log (t)
            
        def trouve_alpha (x2, L) :
            """détermine la valeur de alpha une seule fois"""
            if self.__dict__.has_key ("alpha") : return self.alpha
                
            def fonction (a,x2,L) :
                if a == 0.0 : return 0.0
                else : return 1.0 / a * sinh (a * x2) - L / 2

            a1      = 1.0 / x2
            a2      = 1.0 / x2
            m       = 1.0 / x2
            diff    = fonction (m, x2, L)
            while abs (diff) > 1e-3 :
                if diff > 0 : # faire décroître alpha
                    if fonction (a1, x2, L) > 0 : a1 /= 2.0
                    else : a2 = m
                else :
                    if fonction (a2, x2, L) < 0 : a2 *= 2.0
                    else : a1 = m
                m       = (a1 + a2) / 2
                diff    = fonction (m, x2, L)
            self.alpha = m
            return m
        
        p1 = self.list [0]
        p2 = self.list [ len (self.list) - 1 ]
        if p1.y != p2.y : return None # cas non prévu
        # on trace la courbe y = cosh (alpha x)
        L       = self.l * (len (self.list) - 1)
        mx      = (p1.x + p2.x) / 2
        x1      = p1.x - mx
        x2      = p2.x - mx
        alpha   = trouve_alpha (x2, L) # est solution de 1/alpha sinh (alpha x1) = L/2
        C       = - 1.0 / alpha * cosh (alpha * x2) 

        sx,sy   = screen.get_size ()
        color   = (0,0,255)
        
        ix1     = int (x1)
        ix2     = int (x2)
        x0,y0   = p1.x,p1.y
        for i in xrange (ix1, ix2+1) :
            x   = int (mx + i)
            y   = 1.0 / alpha * cosh (alpha * float (i)) + C + p1.y
            if 0 < y < sy and 0 < y0 < sy :
                pygame.draw.line (screen, color, (x0,sy-y0), (x, sy-y), 2)
            x0,y0 = x,y
        

    def force_point (self, i) :
        """calcule les forces qui s'exerce en un point, 
        retourne un couple x,y"""
        x,y = 0,0
        # poids
        y -= self.g * self.list [i].m
        # voisin de gauche
        dx, dy = self.list [i].difference (self.list [i-1])
        d = math.sqrt (dx *dx + dy *dy)
        if d > self.l :
            dx = (d - self.l) / d * dx
            dy = (d - self.l) / d * dy
            x += self.k * dx
            y += self.k * dy
        # voisin de droite
        dx, dy = self.list [i].difference (self.list [i+1])
        d = math.sqrt (dx *dx + dy *dy)
        if d > self.l :
            dx = (d - self.l) / d * dx
            dy = (d - self.l) / d * dy
            x += self.k * dx
            y += self.k * dy
        # freinage
        x += - self.f * self.vitesse [i].x
        y += - self.f * self.vitesse [i].y
            
        return x,y    
        
    def iteration (self, dt) :
        """calcule les déplacements de chaque point et les met à jour,
        on ne déplace pas les points situés aux extrémités,
        retourne la somme des vitesses et des accélérations au carré"""
        force = [ (0,0) ]
        for i in xrange (1, len (self.list)-1) :
            x,y = self.force_point (i)
            force.append ((x,y))
        force.append ((0,0))
        
        # déplacement
        for i in xrange (1, len (self.list)-1) :
            self.vitesse [i].deplace ( force [i], dt )
            self.list [i].deplace_point ( self.vitesse [i], dt ) 
            
        d = 0
        for f in force :
            d += self.vitesse [i].x ** 2 + force [i][0] **2
            d += self.vitesse [i].y ** 2 + force [i][1] **2
            
        return d
        
    def __str__ (self):
        """affiche chaque point de la corde"""
        s = ""
        l = 0
        for i in xrange (0, len (self.list)) :
            s +=  "point " + str (i) + " : " + str (self.list [i]) 
            if i < len (self.list) -1 :
                x,y     = self.list [i].difference (self.list [i+1])
                d       = math.sqrt (x*x + y*y)
                s += "\t segment : %4.0f" % d 
                s += " ( %4.0f )" % self.l
            if i != 0 and i != len (self.list)-1 : 
                x,y = self.force_point (i)
                s += "\t force en ce point (%f,%f) " % (x,y) 
            s += "\n"
            if i > 0 : 
                x,y = self.list [i].difference (self.list [i-1])
                l += math.sqrt (x*x + y*y)
        s += "longueur de la corde " + str (l) + "\n"
        s += "longueur attendue " + str ((len (self.list)-1) * self.l) + "\n"
        return s

def attendre_clic (screen,x,y):
    """dessine un rectangle rouge sur l'écran et 
    attend la pression d'un clic de souris"""
    color   = 255,0,0
    pygame.draw.line (screen, color, (10,10), (x-10,10), 2)
    pygame.draw.line (screen, color, (x-10,10), (x-10,y-10), 2)
    pygame.draw.line (screen, color, (x-10,y-10), (10,y-10), 2)
    pygame.draw.line (screen, color, (10,y-10), (10,10), 2)
    pygame.display.flip ()
    reste = True
    while reste:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP :
                reste = False
                break

if __name__ == "__main__" :
    
    pygame.init ()
    size      = width, height = x,y = 800, 500
    black     = 0, 0, 0
    white     = 255,255,255
    screen    = pygame.display.set_mode(size)
    nb        = 10
    c         = corde (nb, (100,450), (700,450), 100, 1, 0.1, 0.05, 800)
    dt        = 0.1
    print "corde initial"
    print c
    
    iter      = 0
    dep       = len (c.list) * (x*x + y*y)
    while True and dep > 1e-6 :

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                print c
                attendre_clic (screen,x,y)
    
        if iter % 10 == 0 :
            screen.fill (white)
            c.display (screen)
            pygame.display.flip ()

        iter += 1
    
        if iter == 1: attendre_clic (screen,x,y)
            
        dep = c.iteration (dt)
        #print "dep =", dep
        
        pygame.display.flip ()
    
    print c
    attendre_clic (screen,x,y)
