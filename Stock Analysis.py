# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:38:55 2020

@author: User1
"""

import pandas as pd
import Stock_Download_MK as sd
import yfinance as yf
import numpy as np

# %% Initial Data Download

#List for S&P 500 Companies
s_and_p = ['MMM','ABT','ABBV','ACN','ATVI','AYI','ADBE','AMD','AAP','AES',
		'AMG','AFL','A','APD','AKAM','ALK','ALB','ARE','ALXN','ALGN','ALLE',
		'ADS','LNT','ALL','GOOGL','GOOG','MO','AMZN','AEE','AAL','AEP',
		'AXP','AIG','AMT','AWK','AMP','ABC','AME','AMGN','APH','ADI',
		'ANSS','ANTM','AON','AOS','APA','AIV','AAPL','AMAT','APTV','ADM','ARNC',
		'AJG','AIZ','T','ADSK','ADP','AZO','AVB','AVY','BLL','BAC','BK',
		'BAX','BDX','BRK-B','BBY','BIIB','BLK','HRB','BA','BWA','BXP','BSX',
		'BHF','BMY','AVGO','CHRW','CA','COG','CDNS','CPB','COF','CAH','CBOE',
		'KMX','CCL','CAT','CBS','CNC','CNP','CTL','CERN','CF','SCHW',
		'CHTR','CHK','CVX','CMG','CB','CHD','CI','XEC','CINF','CTAS','CSCO','C','CFG',
		'CTXS','CLX','CME','CMS','KO','CTSH','CL','CMCSA','CMA','CAG','CXO','COP',
		'ED','STZ','COO','GLW','COST','COTY','CCI','CSX','CMI','CVS','DHI',
		'DHR','DRI','DVA','DE','DAL','XRAY','DVN','DLR','DFS','DISCA','DISCK','DISH',
		'DG','DLTR','D','DOV','DTE','DRE','DUK','DXC','ETFC','EMN','ETN',
		'EBAY','ECL','EIX','EW','EA','EMR','ETR','EOG','EQT','EFX','EQIX','EQR',
		'ESS','EL','ES','RE','EXC','EXPE','EXPD','EXR','XOM','FFIV','FB','FAST',
		'FRT','FDX','FIS','FITB','FE','FISV','FLIR','FLS','FLR','FMC','FL','F','FTV',
		'FBHS','BEN','FCX','GPS','GRMN','IT','GD','GE','GIS','GM','GPC','GILD',
		'GPN','GS','GT','GWW','HAL','HBI','HOG','HIG','HAS','HCA','HP','HSIC',
		'HSY','HES','HPE','HLT','HOLX','HD','HON','HRL','HST','HPQ','HUM','HBAN','HII',
		'IDXX','INFO','ITW','ILMN','IR','INTC','ICE','IBM','INCY','IP','IPG','IFF','INTU',
		'ISRG','IVZ','IQV','IRM','JEC','JBHT','SJM','JNJ','JCI','JPM','JNPR','KSU','K','KEY',
		'KMB','KIM','KMI','KLAC','KSS','KHC','KR','LB','LH','LRCX','LEG','LEN',
		'LLY','LNC','LKQ','LMT','L','LOW','LYB','MTB','MAC','M','MRO','MPC','MAR','MMC','MLM',
		'MAS','MA','MAT','MKC','MCD','MCK','MDT','MRK','MET','MTD','MGM','MCHP','MU',
		'MSFT','MAA','MHK','TAP','MDLZ','MNST','MCO','MS','MOS','MSI','MYL','NDAQ',
		'NOV','NAVI','NTAP','NFLX','NWL','NFX','NEM','NWSA','NWS','NEE','NLSN','NKE','NI',
		'NBL','JWN','NSC','NTRS','NOC','NCLH','NRG','NUE','NVDA','ORLY','OXY','OMC','OKE',
		'ORCL','PCAR','PKG','PH','PDCO','PAYX','PYPL','PNR','PBCT','PEP','PKI','PRGO','PFE',
		'PCG','PM','PSX','PNW','PXD','PNC','RL','PPG','PPL','PX','PFG','PG','PGR',
		'PLD','PRU','PEG','PSA','PHM','PVH','QRVO','PWR','QCOM','DGX','RRC','RJF','RTN','O',
		'REG','REGN','RF','RSG','RMD','RHI','ROK','COL','ROP','ROST','RCL','CRM','SBAC',
		'SCG','SLB','STX','SEE','SRE','SHW','SIG','SPG','SWKS','SLG','SNA','SO','LUV',
		'SPGI','SWK','SBUX','STT','SRCL','SYK','STI','SYF','SNPS','SYY','TROW','TPR',
		'TGT','TEL','FTI','TXN','TXT','TMO','TIF','TJX','TSCO','TDG','TRV',
		'TRIP','FOXA','FOX','TSN','UDR','ULTA','USB','UAA','UA','UNP','UAL','UNH','UPS','URI',
		'UTX','UHS','UNM','VFC','VLO','VAR','VTR','VRSN','VRSK','VZ','VRTX','V','VNO',
		'VMC','WMT','WBA','DIS','WM','WAT','WEC','WFC','WDC','WU','WRK','WY','WHR','WMB',
		'WLTW','WYNN','XEL','XRX','XLNX','XYL','YUM','ZBH','ZION','ZTS']

#Create list for blue chip stocks as well  

blue_chip = ['ABBV','BABA','JNJ','MCD','DUK','DG','NVS','KO','MMM','AXP','VZ',
             'PG','V','WMT','KHC','WFC','PEP','GOOGL','AMZN','AAPL',
             'BAC','COST','DIS','GS','HD','MSFT','NKE','SBUX']

dow = ['MMM','AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DD','XOM','GE',
       'GS','HD','IBM','INTC','JNJ','JPM','MCD','MRK','MSFT','NKE','PFE','PG',
       'TRV','RTX','UNH','VZ','V','WMT'] 
  
closing_data = sd.get_stock_data(s_and_p,"2019-01-01","2020-05-19")

# %% Set up Data Frame

#Change to pandas dataframe
stock = pd.DataFrame(closing_data)
#stock = stock_temp.dropna(axis=0)
# Print out the first row to confirm the data format, check index and column name
print(stock.shape)
print(stock.index)
print(stock.columns)
print(stock.head(1))

# %% Analysis

#Find average from 1/1/2019 to 1/31/2020
baseline_avg = stock.loc['2019-01-01':'2020-01-31'].mean(axis=0)
#print(baseline_avg)

#Find average from 3/1/2020 to 5/13/2020
covid_avg = stock.loc['2020-05-01':'2020-05-19'].mean(axis=0)
#print(covid_avg)
#Find minimum from 3/1/2020 to 5/13/2020
covid_min = stock.loc['2020-03-01':'2020-05-19'].min(axis=0)
#print(covid_min)

#Find maximum from 1/1/2019 to 1/31/2020
baseline_max = stock.loc['2019-01-01':'2020-01-31'].max(axis=0)
#print(baseline_max)
#Find the largest differences using the information above (Top 10)

average_diff = baseline_avg - covid_avg
average_perc = average_diff/baseline_avg
minmax_diff = baseline_max - covid_min
maxavg_diff = baseline_max - covid_avg
#trend = stock.apply(lambda x : trenddetector(14,x),axis=0)

#print(average_diff.sort_values(ascending=False))
#print(minmax_diff.sort_values(ascending=False).head(20))
#print(maxavg_diff.sort_values(ascending=False).head(20))

check_temp = average_diff[average_diff>0].sort_values(ascending=False).head(20)

stock_temp = stock[check_temp.index.values]

trend = stock_temp.apply(lambda x : trenddetector(7,x),axis=0)

check = check_temp[trend<0]

print(check)
# %% Find stocks with decreasing trend over last months

def trenddetector(data_points,array,order=1):
    data = array.tail(data_points)
    list_of_index = list(range(0,data_points,1))
    result = np.polyfit(list_of_index, list(data), order)
    slope = result[-2]
    return float(slope)

# %% Print out information

def print_stock_info (array):
    stk_list = list(array.index.values)
    
    for i in range(0,len(stk_list)-1):
        stock = stk_list[i]
        tick = yf.Ticker(stock)
        if 'shortName' in tick.info:
            print(tick.info['shortName'])
        if 'sector' in tick.info:
            print(tick.info['sector'])
    return

print_stock_info(check)


# %% Future Modeling

#For stocks chosen in analysis section : SPG MAR MTB AZO ALGN EXPE 
stock_list = ['SPG','MAR','MTB','AZO','ALGN','EXPE']
#Take growth rate from baseline year, apply to x timeframe looking forward

#Simple return to baseline number
baseline_filter  = baseline_avg[baseline_avg.index.isin(stock_list)]
print(baseline_filter)
covid_filter  = covid_avg[covid_avg.index.isin(stock_list)]
print(covid_filter)
#Model out different projections for $$$ investment

dollar = 5000
invest_in_each = dollar/len(stock_list)
stocks_bought = invest_in_each/covid_filter
model_increase = stocks_bought*baseline_filter
stock_increase = model_increase - invest_in_each

print(stock_increase)


    