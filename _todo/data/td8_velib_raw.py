import sys, os
sys.path.append(r"D:\Dupre\_data\program\python\pyensae\src")

import pyensae
from time import strftime, strptime
import datetime
from pyensae.sql.database_main import Database

tbl = "stations.txt"
if not os.path.exists (tbl) :

    sql = """SELECT DISTINCT address, contract_name,lat,lng,name,number FROM snap 
             ORDER BY name"""
    db = Database(__file__.replace(".py",".db3"))
    db.connect()
    db.export_view_into_flat_file (sql, tbl, header = True, encoding = "utf8")
    db.close()

tbl = "tb8_velib.txt"
if True or not os.path.exists(tbl):
    
    dt = datetime.datetime.strptime ("2013-09-13 11:26:37.738913", "%Y-%m-%d %H:%M:%S.%f") 
    print (dt, type(dt), dt.hour)


    sql = """SELECT collect_date, 
                --strftime('%Y-%m-%d %H:%M:%S', last_update) AS 
                last_update, 
                available_bike_stands, available_bikes, number
                , hour(last_update) AS heure
                , minute(last_update) AS minute
                FROM  snap 
                --LIMIT 100
            """
    db = Database(__file__.replace(".py",".db3"))
    db.connect()
    db.add_function( "hour", 1, lambda d : datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S').hour)
    db.add_function( "minute", 1, lambda d : datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S').minute)
    db.export_view_into_flat_file (sql, tbl, header = True, encoding = "utf8")
    db.close()
