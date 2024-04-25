import json
import pandas as pd

def lambda_handler(event, context):
    d = {'c':[1,2]}
    df = pd.DataFrame(data=d)
    print(df)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from github!')
    }
