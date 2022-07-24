import json
from lib import efficient_frontier
from lib import dataframe as dataframe
from lib import discrete_states


def main(amount : float,stocks : list) -> list:
    df = dataframe.getStockData(stocks)
    n=len(stocks)
    values = efficient_frontier.ef(n=n,df=df)
    out = discrete_states.discreteStates(stocks,amount,df,values)
    #print(out)
    return out

def lambda_handler(event : dict, context):
    amount = event['queryStringParameters']['amount']
    stocks = event['queryStringParameters']['stocks']
    stocks = stocks.split(',')
    n=len(stocks)
    for i in range(n):
        stocks[i]=stocks[i].strip()
        stocks[i]=stocks[i].upper()
    out = main(float(amount),stocks)
    d={}
    c=1
    for i in out:
        price,output_stocks,remaining,exr,risk=i
        price = [round(i,2) for i in price]
        remaining = round(remaining,2)
        d1 = {"price":price,"output_stocks":output_stocks,"remaining":remaining,"expected return":exr,"risk":risk}
        d[c]=d1
        c+=1
    return {
        'statusCode': 200,
        "body": d
    }

#test
# js = {
#     "queryStringParameters": {
#     "amount": "10000",
#     "stocks": "AAPL,GOOG,AMZN,MSFT"
#     }
# }
# print(lambda_handler(js,None))