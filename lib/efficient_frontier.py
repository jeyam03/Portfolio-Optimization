import numpy as np


class store:
    def __init__(self,ex,er,ew):
        self.ex = ex
        self.er = er
        self.ew = ew

def ef(n,df) ->list:
    returns = df.pct_change() 
    values=[]
    cov_annual = returns.cov()*252
    annualized_returns = (1+returns.mean())**252 -1 #Returns with compounding effect
    np.random.seed(25)

    n_port = 10000
    for _ in range(n_port):
        flag=False
        while True:
            weights = np.random.rand(n)
            weights = weights/sum(weights)
            port_return = np.dot(weights,annualized_returns)
            port_risk = np.sqrt(np.dot(weights.T,np.dot(cov_annual,weights)))
            for i in values:
                if i.ex>port_return and i.er<port_risk:
                    flag=True
                    break
            if flag:
                break
            obj=store(port_return,port_risk,weights)
            values.append(obj)
            break
    return values

# Test code
# import pandas as pd
# import yfinance as yf
# from datetime import datetime, timedelta
# w = [0.1, 0.6, 0.3]
# s = ['AAPL', 'GOOG', 'AMZN']
# amt = 10000
# cur_date = (datetime.now()).strftime('%Y-%m-%d')
# # st_date = (datetime.now()-timedelta(days=100)).strftime('%Y-%m-%d')
# st_date = datetime(2020, 1, 2)

# df = pd.DataFrame()
# for symbol in s:
#     data = yf.download(symbol, start=st_date, end=cur_date)['Adj Close']
#     df[symbol] = data

# values = ef(3,df)
# for i in values:
#     print(i.ex,i.er,i.ew)