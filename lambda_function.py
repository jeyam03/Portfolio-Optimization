import json
from lib import efficient_frontier
from lib import dataframe as dataframe
from lib import discrete_states


def main(amount : float,stocks : list) -> list:
    try:
        df = dataframe.getStockData(stocks)
    except:
        return []
    n=len(stocks)
    values = efficient_frontier.ef(n=n,df=df)
    out = discrete_states.discreteStates(stocks,amount,df,values)
    #print(out)
    return out

def lambda_handler(event : dict, context=None):
    try:
        amount = event['queryStringParameters']['amount']
        stocks = event['queryStringParameters']['stocks']
    except:
        return {
            'statusCode': 400,
            'body': {
                'msg':json.dumps('Parameters error in request')
                }
        }

    stocks = stocks.split(',')
    n=len(stocks)
    try :
        amount = float(amount)
    except:
        return {
            'statusCode': 400,
            'body': {
                'msg':json.dumps('Enter Valid Amount')
            }
        }
    for i in range(n):
        stocks[i]=stocks[i].strip()
        stocks[i]=stocks[i].upper()
    out = main(float(amount),stocks)
    if out ==[]:
        return {
            'statusCode': 400,
            'body': {
                'msg':json.dumps('Invalid stock name')
            }
        }
    if out == -1:
        return {
            'statusCode': 400,
            'body': {
                'msg':json.dumps('Insufficient funds')
            }
        }
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
        "body": {"symbols":stocks,"list":d}
    }

#test
# js = {
#     "queryStringParameters": {
#     "amount": "5000",
#     "stocks": "AAPL,GOOG,AMZN,MSFT"
#     }
# }
print(lambda_handler(js,None))