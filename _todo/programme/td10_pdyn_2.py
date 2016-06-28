import random
skieurs = [ random.gauss(1.75, 0.1) for i in range(0,10) ]
paires  = [ random.gauss(1.75, 0.1) for i in range(0,15) ]
skieurs.sort()
paires.sort()


p = { }
p [-1,-1] = 0
best = { }
for n,taille in enumerate(skieurs) : p[n,-1] = p[n-1,-1] + taille
for m,paire  in enumerate(paires ) : p[-1,m] = 0
for n,taille in enumerate(skieurs) :
    for m,paire in enumerate(paires) :
        p1 = p.get ( (n  ,m-1), 1e10 ) 
        p2 = p.get ( (n-1,m-1), 1e10 ) + abs(taille - paire)
        p[n,m] = min(p1,p2)
        
        if p[n,m] == p1 : best [n,m] = n,m-1
        else : best [n,m] = n-1,m-1
        
print (p[len(skieurs)-1,len(paires)-1])

chemin = [ ]
pos = len(skieurs)-1,len(paires)-1
while pos in best :
    print (pos)
    chemin.append(pos)
    pos = best[pos]
chemin.reverse()
print (chemin)