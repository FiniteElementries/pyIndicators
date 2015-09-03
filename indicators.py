
import database_tools as dt
import pandas as pd
import datetime
import numpy as np



def simple_moving_average(ticker, date, date_range):

    stock_data=dt.get_stock_data(ticker,date-datetime.timedelta(days=date_range*10),date)

    retVal=stock_data['Close'].tail(date_range).mean()

    return retVal

def RSI(ticker,date, date_range):

    stock_data=dt.get_stock_data(ticker,date-datetime.timedelta(days=date_range*10),date)
    stock_data=stock_data['Close'].tail(date_range+1).values

    stock_data_new=stock_data[1:date_range+1]
    stock_data_old=stock_data[0:date_range]

    difference=stock_data_new-stock_data_old

    gain=difference[difference>0].sum()/date_range
    loss=-difference[difference<0].sum()/date_range

    relative_strength=gain/loss

    retVal=100-(100/(1+relative_strength))

    return retVal

def standard_deviation(ticker,date,date_range):

    stock_data=dt.get_stock_data(ticker,date-datetime.timedelta(days=date_range*10),date)

    retVal=stock_data['Close'].tail(date_range).std()

    return retVal

def average_true_range(ticker,date,date_range):

    stock_data=dt.get_stock_data(ticker,date-datetime.timedelta(days=date_range*10),date)

    H=stock_data['High'].tail(date_range).values
    L=stock_data['Low'].tail(date_range).values
    PC=stock_data['Close'].tail(date_range+1).values[0:date_range]

    matr=pd.DataFrame()

    matr['HL']=H-L
    matr['H_PC']=abs(H-PC)
    matr['L_PC']=abs(L-PC)

    matr['max']=matr[['HL','H_PC','L_PC']].max(axis=1)

    retVal=matr['max'].mean()

    return retVal


if __name__ == '__main__':
    print simple_moving_average("GooG",datetime.date(2015,3,25),14)
    print RSI("GooG",datetime.date(2015,3,25),14)
    print standard_deviation("GooG",datetime.date(2015,3,25),14)
    print average_true_range("GooG",datetime.date(2015,3,25),14)