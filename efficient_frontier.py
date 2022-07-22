import numpy as np

def ef(n,df) ->list:
    returns = df.pct_change() 
    values=[]
    cov_annual = df.cov()*252
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
            for e,r,w in values:
                if e>port_return and r<port_risk:
                    flag=True
                    break
            if flag:
                break
            row = [port_return,port_risk,weights]
            values.append(row)
            break
    return values

