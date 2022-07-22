from datetime import datetime, timedelta
import yfinance as yf

def discreteStates(weights, symbols, amount, df):
    sub = 1
    if datetime.now().weekday() == 5:
        sub += 1
    if datetime.now().weekday() == 6:
        sub += 2

    cur_date = (datetime.now()-timedelta(days=sub)).strftime('%Y-%m-%d')
    cur_price = df.loc[cur_date]

    price = []
    output_stocks = []
    remaining = 0

    for i in range(len(weights)):
        output_stocks.append((weights[i] * amount) // cur_price[symbols[i]])
        price.append(cur_price[symbols[i]] * output_stocks[i])
        remaining += (weights[i] * amount) % cur_price[symbols[i]]

    return [price, output_stocks, remaining]
