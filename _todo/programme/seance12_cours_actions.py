#coding:latin-1
import urllib, os

"""
composition du CAC 40: http://fr.wikipedia.org/wiki/CAC_40
récupérée ici: http://finance.yahoo.com/q/cp?s=^FCHI+Components
"""

import sys
sys.path.append(r"C:\xadupre\__home_\_data\program\python\pyensae\src")

# télécharge la composition du CAC 40 depuis mon site
# elle a été récupérée ici: http://finance.yahoo.com/q/cp?s=^FCHI+Components
import pyensae
pyensae.download_data('cac40_2013_11_11.txt', website = 'xd')

# télécharge tous les cours (s'ils ne l'ont pas déjà été)
import pandas
from pyensae import StockPrices
actions = pandas.read_csv("cac40_2013_11_11.txt", sep = "\t")

# on enlève les actions qui n'ont pas un historiques assez longs
stocks = { k:StockPrices(tick = k) for k,v in actions.values  if k != "SOLB.PA"}
dates = StockPrices.available_dates( stocks.values() )
stocks = { k:v for k,v in stocks.items() if len(v.missing(dates)) <= 10 }
print ("nb left", len(stocks))

# on enlève les dates pour lesquelles on a des données manquantes
dates = StockPrices.available_dates( stocks.values() )
ok    = dates[ dates["missing"] == 0 ]
print ("toutes dates ", len(dates), " left:" , len(ok))
for k in stocks : stocks[k] = stocks[k].keep_dates(ok)

# on calcule la matrice de corrélation et les rendements
ret, cor = StockPrices.covariance(stocks.values(), cov = False, ret = True)

print (ret.head())
print (cor.head())
