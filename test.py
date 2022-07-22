from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd

w = [0.1, 0.6, 0.3]
s = ['AAPL', 'GOOG', 'AMZN']
amt = 10000
cur_date = (datetime.now()).strftime('%Y-%m-%d')
# st_date = (datetime.now()-timedelta(days=100)).strftime('%Y-%m-%d')
st_date = datetime(2020, 1, 2)

df = pd.DataFrame()
for symbol in s:
    data = yf.download(symbol, start=st_date, end=cur_date)['Adj Close']
    df[symbol] = data

print(df.head())
print()

# discreteStates(w, s, amt, df)