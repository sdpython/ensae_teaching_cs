import pandas
df = pandas.read_csv("matrix_distance_7398.txt", sep="\t")
print (df.head())

vil = { }
for row in df.values :
    vil [row[0]] = 0
    vil [row[1]] = 1
vil = list(vil.keys())
print (len(vil))

dist = { }
for row in df.values :
    a = row[0]
    b = row[1]
    dist[a,b] = dist[b,a] = row[2]
print (len(dist))


d = { }
d['Charleville-Mezieres'] = 0
for v in vil : d[v] = 1e10
for v,w in dist :
    if v == 'Charleville-Mezieres': 
        d[w] = dist[v,w]

for i in range(0,len(d)) :        
    for v,w in dist :
        d2 = d[v] + dist[v,w]
        if d2 < d[w] :
            d[w] = d2
        
print (d['Bordeaux'])        