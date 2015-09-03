import pandas.io.data as web
import datetime
import os.path
import os
import pandas as pd

import contextlib
import sys
import cStringIO

from timeit import default_timer
import time

@contextlib.contextmanager
def elapsed_timer():
    start = default_timer()
    elapser = lambda: default_timer() - start
    yield lambda: elapser()
    end = default_timer()
    elapser = lambda: end-start
         
ram_stock={}

def read_stock_list():
    dire=os.getcwd()
    ListFile=dire + '\\miscs\\ticker_list.stock'
    
    lst=pd.read_csv(ListFile).ix[:,0].tolist()

    return lst

def reset_ram_stock():
    ram_stock={}

def get_stock_data(ticker, date, period):
    ''' download stock data
    string: ticker
    Datetime: date_start
    Datetime: date_end

    return panda dataframe
    '''
    ticker=ticker.upper()

    if ticker in ram_stock:
        temp_stock=ram_stock[ticker].copy()
        retVal=temp_stock[(date+datetime.timedelta(days=-(period*2+7))):date].tail(n=period)
        
        if(len(retVal.index)==period and retVal.index[-1].date()==date):
            return retVal

    date_end=(date+datetime.timedelta(days=1000)).strftime("%Y-%m-%d")
    date_start=(date+datetime.timedelta(days=-1000)).strftime("%Y-%m-%d")

    ticker=ticker.upper()

    data=web.DataReader(ticker,'yahoo',date_start,date_end)

   # data.index=pd.to_datetime(data.index)

    ram_stock[ticker]=data.copy()

    retVal=data[(date+datetime.timedelta(days=-(period*2+7))):date].tail(n=period)
        
    if(len(retVal.index)==period and retVal.index[-1].date()==date.date()):
        return retVal
    else:
        print("Warning stock data not extracted properly!")
        return retVal

if __name__ == '__main__':
    get_stock_data('goog',datetime.date(2015,5,1),5)
    print get_stock_data('goog',datetime.date(2015,5,1),5)
    print get_stock_data('goog',datetime.date(2015,5,4),5)
    print get_stock_data('goog',datetime.date(2015,4,1),5)



