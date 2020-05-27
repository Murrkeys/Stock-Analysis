# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:38:55 2020

@author: User1
"""

import yfinance as yf


#function to take in list,start,end and return closing data
def get_stock_data(stock,start_date,end_date):
    
    data = yf.download(stock, start=start_date, end=end_date,threads=True)
    closing_data = data['Close']
    return closing_data


    


    