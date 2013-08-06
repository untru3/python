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



name=str
ticketcount=0

UrlBegin="http://download.finance.yahoo.com/d/quotes.csv?s="
UrlEnd="&f=nsl1op&e=.csv"
output_path = "C:/Code/StockData/stocks.txt"


#ticketcount=input("how many tickers do you want to enter? ")
#print ticketcount




ticker1=raw_input("Enter ticker symbol: ")
ticker2=raw_input("Enter ticker symbol: ")

print ticker1 + ticker2


URL=UrlBegin + ticker1 + "," + ticker2 + UrlEnd
print URL

urllib.urlretrieve(URL,output_path)


#outfile = open(output_path)
#outfile.write("hello this is a test")
#outfile.close()






































