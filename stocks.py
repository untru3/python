#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alex
#
# Created:     13/10/2012
# Copyright:   (c) Alex 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import urllib
import os





UrlBegin="http://download.finance.yahoo.com/d/quotes.csv?s="
UrlEnd="&f=nsl1op&e=.csv"
output_path = "C:/StockData/"
filename = "stocks.txt"
fullpath = output_path + filename




if not os.path.exists(output_path):
    os.makedirs(output_path)


tickercount=input("how many tickers do you want to enter? ")




stocklist=""

i=0
while (i < tickercount):
    stock=raw_input("enter ticker ")
    stocklist = stocklist + "," + stock
    i=i+1





stocklist = stocklist[1:]




URL=UrlBegin + stocklist + UrlEnd



urllib.urlretrieve(URL,fullpath)









































