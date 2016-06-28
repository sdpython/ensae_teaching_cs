# coding: cp1252
import random
import math

n  = 10000
hn = dict ()

for i in xrange (1,n):
    x  = random.gauss (0,1)
    xx = round (x, 1)
    if xx not in hn:					# si h [xx] n'existe pas encore
        hn [xx] = 0
    hn [xx] += 1

# affichage de l'histogramme
for w in hn:
    print w, "    \t", float (hn [w]) / float (n)


n  = 10000
hb = dict ()
k  = 400
for i in xrange (1,n):
    if (i % 500 == 0) :	     # comme le programme est assez lent,
        print i              # cela permet de suivre l'avancement
    s = 0
    for j in xrange (1,k):
        a  = random.randint (0,1)
        s += a
    x  = float (s - k/2) / math.sqrt (float (k * 0.25))
    xx = round (x, 1)

    if xx not in hb:
        hb [xx] = 0
    hb [xx] += 1

# affichage de l'histogramme
for w in hb:
    print w, "    \t", float (hb [w]) / float (n)


x1 = hn.keys ()
x1.sort ()
y = [ hn [a] for a in x1 ]
x2 = hb.keys ()
x2.sort ()
z = [ hb [a] for a in x2 ]

import biggles
p = biggles.FramedPlot()
p.title = "Histogramme"
p.xlabel = "x"
p.ylabel = "y"
p.add( biggles.Curve(x1, y, color="red") )
p.add( biggles.Curve(x2, z, color="blue") )
p.show()

