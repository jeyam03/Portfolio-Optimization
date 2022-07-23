import json
from lib import efficient_frontier
from lib import dataframe as dataframe
from lib import discrete_states

def main(amount : float,stocks : list) -> list:
    df = dataframe.getStockData(stocks)
    n=len(stocks)
    values = efficient_frontier.ef(n=n,df=df)
    return discrete_states.discreteStates(values,stocks,amount,df)

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
        price,output_stocks,remaining,risk=i
        d1 = {"price":price,"output_stocks":output_stocks,"remaining":remaining,"risk":risk}
        d[c]=d1
    return {
        'statusCode': 200,
        "output": json.dumps(d)
    }