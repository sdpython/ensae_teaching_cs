from marathon import *
import numpy as np

donnees = charge_donnees ()
mat = np.array(donnees)
print mat
print "***"



xy = np.array ( np.column_stack ( (mat[:,1], mat[:,3])), dtype=float)
xy2 = mat[ mat[:,0] == "PARIS" , :  ]

mat[ mat[:,0] == "PARIS" , 0 ] = "rr"
#print xy2
print mat

print np.zeros(3)

z = np.zeros ( mat.shape[ 0 ] )
mat = np.column_stack ( (mat, z))
print mat
