'''
@projectName:stock analyser(nifty 50,fundamental)
@date:11/08/2022
@author:Vishwa S Appaji
'''
import pandas as pd
import numpy as np
print("**********Welcome to Stock analyser*************\n")
print("Here we do fundamental analysis of the stock\n")
html_url1="https://www.moneycontrol.com/stocks/marketinfo/pe/bse/homebody.php?indcode=0&sortcode=0"
shares=pd.read_html(html_url1)
nifty=shares[0]
nifty.drop(columns="Sr",inplace=True)
while(True):
    print("*******************************************************************************************")
    print("Press 'show' to see all 100 stocks")
    print("Enter the name of the company you are interested in: ")
    print("Or enter 108 to Quit this program")
    name = input()
    if(name=="108"):
        break
    elif(name=='show'):
        print(nifty.head(20))
    else:
        print("financial Details of the stock are:")
        for i in range(0, 100):
            if (name in (nifty.iat[i,0]).lower()):
                print(nifty.iloc[i])
                print("*******************************************************************************************")
                print("Some Famous Abbreviation are as follows:")
                print("CMP->Current Market Price\nROE->Return On Equity(Should expect more than 12%)")
                print("P/E->Price to Earnings Ratio(A high P/E could mean that a stock's price is high relative to earnings and possibly overvalued.")
                print("Conversely, a low P/E might indicate that the current stock price is low relative to earnings.")
                print("P/BV->Price to Book Value Ratio")
                print("*******************************************************************************************")

print("Thank You!!!!!!!!!!!!\nHappy Investing")