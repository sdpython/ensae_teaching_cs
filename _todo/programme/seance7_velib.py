#coding:latin-1
import sys
sys.path.append(r"pyensae\src")

import numpy, datetime
from matplotlib.mlab import csv2rec
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.ticker import Formatter


import sys, datetime
sys.path.append(r"python\pyensae\src")
import pyensae
file = pyensae.download_data("velib_vanves.zip", website = "xd")
file = file[0]



import pandas
df = pandas.read_table(file, header = False, sep = "\t", decimal = ",",
    parse_dates = ["last_update"],
    date_parser=lambda s : datetime.datetime.strptime (s, "%d/%m/%Y %H:%M"))
print (len(df))  

print ("min_date", df["last_update"].min())
print ("max_date", df["last_update"].max())


print ("max velo", df["available_bikes"].max())
print ("max_place", df["available_bike_stands"].max())

#print(df.describe())

print ("pas de v�lo", len(df [ df["available_bikes"]==0 ]) / len(df) )
print ("pas de place", len(df [ df["available_bike_stands"]==0 ]) / len(df) )

add = df["available_bikes"] + df["available_bike_stands"]
print (add.max())

####################### dessin

if False :
    df = df.set_index("last_update")
    import matplotlib.pyplot as plt
    ts = df.ix[:,"available_bikes"]
    ts.plot()
    plt.show()

    
ts = df.ix[:,"available_bikes"]    
print(df[:10])
df2 = df.ix[:, ["last_update","available_bikes"]]
df2["weekday"] = df2['last_update'].map(lambda d: str(d.weekday()) + "-" + d.strftime("%H:%M"))
df2["weekno"] = df2['last_update'].map(lambda d: d.isocalendar()[1])
print (df2[:10])

sp = "available_bikes weekday weekno".split()
sem = df2.ix[:,sp]
piv = sem.pivot ('weekday', "weekno", "available_bikes")
#print (sem.head())
#print (piv.head())

thispiv = piv

################# exercice 1 (ou part de df2)

# on somme la s�rie compl�te 12 fois mais d�cal� � chaque fois
nbperiod = 12
mat = numpy.matrix ( [0.0] * (len( df2 ) - nbperiod+1) ).transpose()
for i in range(0,nbperiod) :
    r = df2.ix[i:len(df2)-nbperiod+i,'available_bikes']
    m = numpy.matrix(list(r)).transpose()
    mat += m
mat /= 1.0 * nbperiod

# on �limine les premi�res et derni�res valeurs
df2 = df2[nbperiod/2:-nbperiod/2+1]
df2["lisse"] = mat

# on r�p�te la m�me manipulation pour superposer les semaines
sp = "lisse weekday weekno".split()
sem = df2.ix[:,sp]
piv = sem.pivot ('weekday', "weekno", "lisse")
#piv.plot()
#plt.show()

################# exercice 2

print (thispiv.head())
#thispiv.to_csv("dd.txt", sep="\t")


beg = "4-16:00"
piv = thispiv 
piv.ix[beg:,31] = numpy.NaN
mx = numpy.array(piv.values)
print (mx)
print (piv.index)

for i,k in enumerate(piv.index) :
    if k >= beg and numpy.isnan(piv.ix[k,31]):
        ave_week = numpy.average( mx[~numpy.isnan(mx[:,2]),2]) 
        ave_hour = numpy.average( mx[i, ~numpy.isnan(mx[i,:])] ) 
        piv.ix[k,31] = (ave_week*ave_hour)**0.5
    
piv.plot()
plt.show()


