#coding:latin-1
import sys, datetime
sys.path.append("../../../../program/python/pyensae/src")

from pyensae import download_data

print ("A",datetime.datetime.now())
download_data("SQLiteSpy.zip", website = 'xd')
print ("B",datetime.datetime.now())
download_data("td8_velib.zip", website = 'xd')
print ("C",datetime.datetime.now())

from pyensae import import_flatfile_into_database
dbf = "td8_velib2.db3"
if False :
    print ("import",datetime.datetime.now())
    import_flatfile_into_database(dbf, "td8_velib.txt")
    print ("import",datetime.datetime.now())
    import_flatfile_into_database(dbf, "stations.txt", table="stations")
    print ("import",datetime.datetime.now())
    
if False :
    import sqlite3
    conn = sqlite3.connect(dbf)
    data = conn.execute("SELECT * FROM stations")
    for d in data :
        print (d)
    conn.close()
    


