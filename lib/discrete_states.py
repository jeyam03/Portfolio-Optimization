from datetime import datetime, timedelta


def discreteStates(symbols, amount, df,values):
    cur_date = df.tail(1).index[0]
    #print(cur_date)
    cur_price = df.loc[cur_date]
    #print(cur_price)
    n=len(symbols)
    if sum(cur_price)>amount:
        return -1
    out=[]
    dic={}
    for i in values:
        if round(i.er,2) not in dic:
            dic[round(i.er,2)]=[i.ew,i.ex]
        else:
            if i.ex>dic[round(i.er,2)][1]:
                dic[round(i.er,2)]=[i.ew,i.ex]        
    for j in dic:
        price = []
        output_stocks = []
        remaining = 0
        weights=dic[j][0]
        ex=round(dic[j][1],3)
        for i in range(n):
            output_stocks.append((weights[i] * amount) // cur_price[symbols[i]])
            price.append(cur_price[symbols[i]] * output_stocks[i])
            remaining += (weights[i] * amount) % cur_price[symbols[i]]

        out.append([price, output_stocks, remaining,ex,j])
    return out

# Test code
# import pandas as pd
# import yfinance as yf
# import efficient_frontier
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
# print(out)

