from datetime import datetime, timedelta


def discreteStates(symbols, amount, df,values):
    n=len(symbols)
    sub = 1
    if datetime.now().weekday() == 5:
        sub += 1
    if datetime.now().weekday() == 6:
        sub += 2

    cur_date = (datetime.now()-timedelta(days=sub)).strftime('%Y-%m-%d')
    cur_price = df.loc[cur_date]
    out=[]
    dic={}
    for i in values:
        dic[round(i.er,2)]=i.ew
        
    for j in dic:
        price = []
        output_stocks = []
        remaining = 0
        weights=dic[j]
        for i in range(n):
            output_stocks.append((weights[i] * amount) // cur_price[symbols[i]])
            price.append(cur_price[symbols[i]] * output_stocks[i])
            remaining += (weights[i] * amount) % cur_price[symbols[i]]

        out.append([price, output_stocks, remaining,j])
    return out

# Test code
# import pandas as pd
# import yfinance as yf
#import efficient_frontier
# s = ['AAPL', 'GOOG', 'AMZN',"MSFT"]
# amt = 10000
# cur_date = (datetime.now()).strftime('%Y-%m-%d')
# # st_date = (datetime.now()-timedelta(days=100)).strftime('%Y-%m-%d')
# st_date = datetime(2020, 1, 2)

# df = pd.DataFrame()
# for symbol in s:
#     data = yf.download(symbol, start=st_date, end=cur_date)['Adj Close']
#     df[symbol] = data

# values = efficient_frontier.ef(4,df)
# out = discreteStates(s, amt, df,values)
# print(out[0])

