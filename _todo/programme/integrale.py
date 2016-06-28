# coding: cp1252
import math

n = 2000
a = -2.0
b = 3.0
h = (b-a)/n

sum = 0
for i in xrange (1,n):
    x = a + h * i
    sum += h * x * math.cos (x)

print "intégrale : ", sum

import scipy.integrate as integral            # on importe le module d'intégration
def fff(x): return x * math.cos (x)           # on définit la fonction à intégrer				
sum = integral.quad (fff, a,b, args=()) [0]   # on appelle la fonction d'intégration
print "intégrale avec scipy : ", sum          # on affiche le résultat
