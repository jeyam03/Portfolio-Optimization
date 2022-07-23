from datetime import datetime
import yfinance as yf
import pandas as pd

def getStockData(symbols):
    start_date = "2020-01-02"
    end_date = (datetime.now()).strftime('%Y-%m-%d')
    df = pd.DataFrame()

    for symbol in symbols:
        data = yf.download(symbol, start=start_date, end=end_date)['Adj Close']
        df[symbol] = data

    return df

# getStockData(['AAPL'])