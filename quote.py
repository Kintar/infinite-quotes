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
            
            if (len(queryResp['Items']) == 1):
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
                    'body': 'Query returned multiple results.  That shouldn\'t happen!'
                }
            
        else:
            return {
                'statusCode': 400,
                'body': 'Missing required path parameter "quoteId"'
            }
    elif httpMethod == 'PUT':
        try:
            quote = json.loads(event['body'])
            print(quote)
        except:
            return {'statusCode': 400, 'body': 'Malformed JSON input'}
            
        if 'lines' not in quote:
            return {'statusCode': 400, 'body': 'Missing "lines" in request body'}
        
        if len(quote['lines']) == 0:
            return {'statusCode': 400, 'body': 'No lines in quote'}
        
        l = 0
        for line in quote['lines']:
            if 'text' not in line:
                return {'statusCode': 400, 'body': "Line {} has no text".format(l)}
            if 'quoter' not in line:
                return {'statusCode': 400, 'body': "Line {} has no quoter".format(l)}
            l+=1
        
        quote.quoteId = str(uuid.uuid4())
        quote.date = str(datetime.datetime.now())
        
        try:
            quotestable.put_item(
                Item = quote
                )
        except ClientError as e:
            print("Failed to store quote: {}", json.dumps(e))
            return {'statusCode': 500, 'body': 'Internal error storing quote.  Please try again.'}
        
        return {'statusCode': 200, 'body': quote}
    else:
        return {
            'body': "Invalid HTTP verb: {}".format(httpMethod),
            'statusCode': 400
        }