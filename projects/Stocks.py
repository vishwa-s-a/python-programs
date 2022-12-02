'''
@projectName:stock analyser(nifty 50,fundamental)
@date:11/08/2022
@author:Vishwa S Appaji
'''
import pandas as pd
import numpy as np
print("**********Welcome to Stock analyser*************\n")
print("Here we do fundamental analysis of the stock\n")
print("The companies in nifty 50 are: \n")
html_url1="https://www.moneyworks4me.com/best-index/nse-stocks/top-nifty50-companies-list"
shares=pd.read_html(html_url1)
nifty=shares[0]
nifty.drop(columns='DeciZen',inplace=True)
nifty.drop(columns='More Info',inplace=True)
nifty.drop(columns='Price Change',inplace=True)
#print(nifty.columns)
nifty.drop(columns="Unnamed: 0",inplace=True)
print(nifty)
def swap(name):
    if (name[6] == " "):
        return name[0:4]
    elif (name[5] == " "):
        return name[0:3]
    elif (name[7] == " "):
        return name[0:5]
    elif (name[8] == " "):
        return name[0:6]
    elif (name[9] == " "):
        return name[0:7]
while(True):
    print("*******************************************************************************************")
    print("Enter the name of the company you are interested in, using index associated press the number")
    print("Or enter 108 to Quit this program")
    option=int(input())
    if(option==108):
        break
    else:
        nameH=nifty.iat[option,3]
        nifty.iat[option,3]=swap(nameH)
        nameL=nifty.iat[option,4]
        nifty.iat[option,4]=swap(nameL)
        print("financial Details of the stock are:")
        print(nifty.iloc[option])
        print("*******************************************************************************************")
        print("Some Famous Abbreviation are as follows:")
        print("CMP->Current Market Price\nROE->Return On Equity(Should expect more than 12%)")
        print("P/E->Price to Earnings Ratio(A high P/E could mean that a stock's price is high relative to earnings and possibly overvalued.)")
        print("Conversely, a low P/E might indicate that the current stock price is low relative to earnings.")
        print("P/BV->Price to Book Value Ratio")
        print("*******************************************************************************************")
        if(nifty.iat[option,7]<=1):
            print("A low P/BV indicates that the stock is trading at a discount to the company's book value and vice versa.")
        elif(1<nifty.iat[option,7]<3):
            print("Stock is trading at a reasonable price, can go for it")
        else:
            print("Stock is overpriced and traded at much higher price than its book value, due to various factors")




print("Thank You!!!!!!!!!!!!\nHappy Investing")