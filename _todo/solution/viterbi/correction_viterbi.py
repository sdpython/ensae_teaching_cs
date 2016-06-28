#HERMANT Bettina

#import-*-coding:cp1252-*
import numpy as np
import random

# PARTIE I 
# Question 1
def  DistanceDeLevenshtein(c1,c2) :
	d=[[0 for i in xrange(0,len(c2)+1)] for j in xrange(0,len(c1)+1)]
	for i in xrange(0,len(c1)) :
		d[i][0]=i
	for j in xrange(0,len(c2)) :
		d[0][j]=j
	for i in xrange(1,len(c1)+1) :
		for j in xrange(1,len(c2)+1) :
			if c1[i-1]==c2[j-1] :
				cout=0
			else : 
				cout=1
			d[i][j]=min(d[i-1][ j ] + 1, d[i][ j-1] + 1, d[i-1][ j-1] + cout)
	return d[len(c1)][len(c2)]
	
print DistanceDeLevenshtein("rstairnts","restaurant")
# On obtient bien une disctance de 4 pour l'exemple cité

# Question 2
def  DistanceDeLevenshtein2(c1,c2) :
	d=[[0 for i in xrange(0,len(c2)+1)] for j in xrange(0,len(c1)+1)]
	predecessor=[[(i-1,j-1) for j in xrange(0,len(c2)+1)] for i in xrange(0,len(c1)+1)]
	for i in xrange(0,len(c1)) :
		d[i][0]=i
	for j in xrange(0,len(c2)) :
		d[0][j]=j
	for i in xrange(1,len(c1)+1) :
		for j in xrange(1,len(c2)+1) :
			if c1[i-1]==c2[j-1] :
				cout=0
			else : 
				cout=1				
			e = d[i-1][ j ] + 1
			ins = d[i][j-1] + 1
			s = d[i-1][j-1] + cout
			if s < min (e,ins) :
				d [i][j] = s
				predecessor [i][j] = (i-1, j-1)
			elif e < min (s,ins) :
				d [i][ j] = e
				predecessor [i][j] = (i-1, j)
			else :
				d [i][j] = ins
				predecessor [i][j] = (i, j-1)
	print predecessor
	print i,j
	print predecessor[len(c1)][len(c2)]
	return d[len(c1)][len(c2)]
# predecessor permet d'avoir la trace des modifications effectuées sur le mot

# Question 3
#prodecessor[len(c1),(c2)] contient l'information sur la nature de la transformation donnant la dernière lettre du mot modifié

# Question 4

# PARTIE II

l1=[0.1,0.2,0.3,0.1,0.1,0.2]
l2=[0.3,0.1,0.1,0.1,0.1,0.3]
l3=[0.1,0.2,0.2,0.2,0.1,0.2]

# Question 5
def tirage(l) :
	#creation de la fonction de repartition
	m=[0 for i in xrange(0,7)]
	for i in xrange(0,6) :
		m[i+1]=m[i]+l[i]
	import random
	a=random.random()
	for i in xrange(0,6) : 
		if m[i]<a<m[i+1] :
			return i+1
print tirage(l1)

#Question 6
def simulation(l1,l2,l3) :
	l=[0,0,0]
	l[0]=tirage(l1)
	for i in xrange(0,2) :
		if l[i]==1 or l[i]==2 : l[i+1]=tirage(l1)
		if l[i]==3 or l[i]==4 : l[i+1]=tirage(l2)
		if l[i]==5 or l[i]==6 : l[i+1]=tirage(l3)
	return str(l)
	


print simulation (l1,l2,l3)

#Question 7
def sim10000() :
	sim=[simulation() for i in xrange(0,10000)]
	d={}
	for l in sim :
		d[l]=0
	for l in sim :
		d[l]+=1
	return d

# Question 8 
# P([6,6,6])=0.2*0.2*0.2=0.008

l=[l1,l2,l3]

#Question 9
def trivalues (d):
	l = [ (m,n) for (n,m) in d.iteritems () ]
	l.sort (reverse = True)
	l = [ (m,n) for (n,m) in l]
	return l

def proba() :
	p={}
	for i in xrange(1,7) :
		for j in xrange(1,7) :
			for k in xrange(1,7) :
				if j==1 or j==2 : p[i,j,k]=l[0][k-1]
				if j==3 or j==4 : p[i,j,k]=l[1][k-1]
				if j==5 or j==6 : p[i,j,k]=l[2][k-1]
				if i==1 or i==2 : p[i,j,k]*=l[0][j-1]
				if i==3 or i==4 : p[i,j,k]*=l[1][j-1]
				if i==5 or i==6 : p[i,j,k]*=l[2][j-1]		
				p[i,j,k]*=l[0][i-1]
	return trivalues (p)[0]

print proba()
# La sequence la plus probable est 313 avec une probabilite de 0.027

#PARTIE III
#Question 10
# Chaque proba ne dépend que du tirage précédent (et seulement de celui-ci). Ainsi la matrice du premier au second tirage sera la même que celle du second au troisième tirage.
a1=[l1,l1]
a2=[l2,l2]
a3=[l3,l3]
A=a1+a2+a3
print "A: \n", A

#PARTIE IV
#Question 11
#Il faut absolument que le premier tirage soit effectué avec le dé 1. On a donc S0(1)=1 et S0(2)=1 et les autres valeurs sont nulles. 
S=[[0 for j in xrange(0,6)] for i in xrange(0,4)]
for i in xrange(0,2) :
		S[0][i]=1
print "S: \n", S

#Question 12
def Sc(t,j) :
	a=max(S[t-1][i]*A[i][j] for i in xrange(0,6))
	return a           

#Question 13
for t in xrange(1,4) :
	for j in xrange(0,6) :
		S[t][j]=Sc(t,j)

print max(S[3])
print S[3].index(max(S[3]))+1
print np.array(S)
#La sequence la plus probable se termine par un 3 et pour probabilite 0.027.

#Question 14
def B(t,j) :
	l=[S[t-1][i]*A[i][j] for i in xrange(0,6)]
	a=max(l)
	b=l.index(max(l))
	return [a,b]

def seq_plus_probable(t) :
	S=[[0 for j in xrange(0,6)] for i in xrange(0,t+1)]
	R=[[0 for j in xrange(0,6)] for i in xrange(0,t-1)]
	for i in xrange(0,2) :
		S[0][i]=1
	for u in xrange(1,t+1) :
		for j in xrange(0,6) :
			S[u][j]=B(u,j)[0]
			if u>1 : R[u-2][j]=B(u,j)[1]
	print np.array(R)
	l=[]
	l+=[S[t].index(max(S[t]))+1]
	for i in xrange(t-2,-1,-1) :
		l+=[R[i][S[i+2].index(max(S[i+2]))]+1]
	l.reverse()
	return l
print seq_plus_probable(3)
# On retrouve bien que la séquence la plus probable est 3 1 3. 

#Question 15
# La première méthode est à proscrire car le nombre de lancés est trop faible pour obtenir un résultat cohérent. 
