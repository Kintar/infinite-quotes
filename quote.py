import os
import json
import boto3
import uuid
import datetime

from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

if os.getenv("AWS_SAM_LOCAL"):
    dynamodb = boto3.resource('dynamodb',endpoint_url = "http://localhost:8000")
else:
    dynamodb = boto3.resource('dynamodb')

quotestable = dynamodb.Table(os.getenv('TABLE_NAME') or 'quotes')

def handler(event, context):
    print(json.dumps(event))
    
    httpMethod = event['requestContext']['httpMethod'] or 'GET'
    
    if httpMethod == 'GET':
        quoteId = event['pathParameters']['quoteId']
        
        if (quoteId):
            try:
                queryResp = quotestable.query(
                    KeyConditionExpression = Key('id').eq(event['pathParameters']['quoteId'])
                )
            except ClientError as e:
                print("Failed to retrieve quote #{}: {}".format(quoteId, e))
                return {'statusCode': 500,
                        'body': 'Error querying database' }
            
            if (len(queryResp['Items'] == 1)):
                return {
                    'statusCode': 200,
                    'body': json.dumps(queryResp['Items'][0])
                }
            elif (len(queryResp['Items']) == 0):
                return {
                    'statusCode': 404,
                    'body': 'Quote not found'
                }
            else:
                return {
                    'statusCode': 500,
                    'body': 'Query returned multiple responses.  That shouldn\'t happen!'
                }
            
        else:
            item = {
                'id': str(uuid.uuid4()),
                'date': str(datetime.datetime.now())
            }
            
            try:
                quotestable.put_item(
                    Item = item
                )
            except ClientError as e:
                print("Failed to store quote: {}".format(json.dumps(e.response['Error'])))
                return {'statusCode': 500,
                        'body': 'Error storing quote.  Please try again.'}
            
            return {
                'body': {
                    'quoteId' : item['id'],
                    'createdAt': item['date']
                }
            }
    else:
        return {
            'body': "Invalid HTTP verb: {}".format(httpMethod),
            'statusCode': 400
        }