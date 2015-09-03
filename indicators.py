
import database_tools as dt
import pandas as pd
import datetime
import numpy as np


def standard_deviation(ticker,date,periods):

    stock_data=dt.get_stock_data(ticker,date,periods)

    retVal=stock_data['Close'].std()

    return retVal

def SMA(ticker, date, periods):

    stock_data=dt.get_stock_data(ticker,date,periods)

    retVal=stock_data['Close'].mean()

    return retVal

def volatility(ticker, date, periods):

    stock_data=dt.get_stock_data(ticker,date,periods+1)
    close_data=stock_data['Close'].values

    close_data_new=close_data[1:periods+1]
    close_data_old=close_data[0:periods]

    stock_returns=np.divide(close_data_new,close_data_old)-1.0

    retVal=np.std(stock_returns)* periods **(0.5)

    return retVal

def willamsR(ticker, date, periods):
    stock_data=dt.get_stock_data(ticker,date,periods)

    highest_high=stock_data['High'].max()
    lowest_low=stock_data['Low'].min()
    today_close=stock_data['Close'][-1]

    R=(highest_high-today_close)/(highest_high-lowest_low)*(-100)
    
    return R

def EMA(ticker, date, periods):

    new_periods=periods*5
    stock_data=dt.get_stock_data(ticker,date,new_periods)

    close_array=stock_data['Close'].values
    alpha=2.0/(periods+1)

    weight=np.logspace(new_periods-1,0,new_periods,base=(1-alpha))*alpha

    weight[0]=weight[0]/alpha

    retVal=np.multiply(close_array,weight).sum()

    return retVal

def MACD_customized(ticker, date, periods):
    return 0

def bollinger_bands_customized(ticker, date, periods):
    return 0

def ADX(ticker, date, periods):
    return 0

def RSI(ticker,date, periods):

    stock_data=dt.get_stock_data(ticker,date,periods+1)
    close_data=stock_data['Close'].values

    close_data_new=close_data[1:periods+1]
    close_data_old=close_data[0:periods]

    difference=close_data_new-close_data_old

    gain=difference[difference>0].sum()/periods
    loss=-difference[difference<0].sum()/periods

    relative_strength=gain/loss

    retVal=100-(100/(1+relative_strength))

    return retVal


def average_true_range(ticker,date,periods):

    stock_data=dt.get_stock_data(ticker,date,periods+1)

    H=stock_data['High'].values[1:periods+1]
    L=stock_data['Low'].values[1:periods+1]
    PC=stock_data['Close'].values[0:periods]

    matr=pd.DataFrame()

    matr['HL']=H-L
    matr['H_PC']=abs(H-PC)
    matr['L_PC']=abs(L-PC)

    matr['max']=matr[['HL','H_PC','L_PC']].max(axis=1)

    retVal=matr['max'].mean()

    return retVal


def typical_price(ticker,date):
    return 0

def true_range(ticker,date):
    return 0

if __name__ == '__main__':
    print simple_moving_average("GooG",datetime.date(2015,3,25),14)
    print RSI("GooG",datetime.date(2015,3,25),14)
    print standard_deviation("GooG",datetime.date(2015,3,25),14)
    print average_true_range("GooG",datetime.date(2015,3,25),14)