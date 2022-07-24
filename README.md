# Portfolio-Optimization
Creating a python program to optimize budget allocation for selected stocks to gain maximum return using efficient frontier method.

Deploying the module as AWS serverless API using AWS lambda and AWS API gateway.

# Package Overview
![test](assets/overview.png)
# API-Syntax
```https://gqpev2z6wl.execute-api.ap-south-1.amazonaws.com/getEF?amount=<amount>&stocks=<Stock1>&stocks=<stock2>&stocks=<stockn>```

# API-Example
```https://gqpev2z6wl.execute-api.ap-south-1.amazonaws.com/getEF?amount=10000&stocks=GOOG&stocks=AMZN```

# API-Output
```{"1": {"price": [6902.4, 2991.12], "output_stocks": [60.0, 24.0], "remaining": 106.48, "expected return": 0.242, "risk": 0.32}, "2": {"price": [8628.0, 1246.3], "output_stocks": [75.0, 10.0], "remaining": 125.7, "expected return": 0.256, "risk": 0.33}}```

# Challenges Faced
1. Had trouble in using lambda layers for installing dependencies 
    - **Solution** - Used AWS Lambda layers with proper file structure, i.e 
     ```python ->site_lib->packages``` and installed the dependencies in a linux environment using WSL
2. Had trouble in displaying get response in browser
    - **Solution** - Changed key output to body in the return response
3. Had trouble in finding errors in the program
    - **Solution** - Used AWS cloudwatch and print (event) in lambda_function.py