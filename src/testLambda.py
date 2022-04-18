import json

import boto3

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    data = client.scan(TableName='appLogs')
    response = {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    return response

# return {
#     'statusCode': 200,
#     'body': json.dumps('Hello from Lambda!')
# }