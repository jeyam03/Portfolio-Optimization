from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd

def discreteStates(weights, symbols, amount, df):
    cur_date = (datetime.now()-timedelta(days=2)).strftime('%Y-%m-%d')
    cur_price = df.loc[cur_date]

    price = []
    output_stocks = []
    remaining = 0

    for i in range(len(weights)):
        price.append(weights[i] * amount)
        output_stocks.append(price[i] // cur_price[symbols[i]])
        remaining += price[i] % cur_price[symbols[i]]
    print(price)
    print(output_stocks)
    print(remaining)

w = [0.1, 0.6, 0.3]
s = ['AAPL', 'GOOG', 'AMZN']
amt = 10000
cur_date = (datetime.now()-timedelta(days=2)).strftime('%Y-%m-%d')

df = pd.DataFrame()
for symbol in s:
    data = yf.download(symbol, start=cur_date, end=cur_date)['Adj Close']
    df[symbol] = data

discreteStates(w, s, amt, df)
