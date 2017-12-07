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
        group = event['pathParameters']['group']
        
        queryParams = event['requestContext'].get('queryStringParameters') or {}
        
        startKey = queryParams.get('startKey')
        pageSize = int(queryParams.get('pageSize','20'))
        
        try:
            if (startKey):
                queryResp = quotestable.query(
                    KeyConditionExpression = Key('group').eq(group),
                    ExclusiveStartKey = startKey,
                    Limit = pageSize
                )
            else:
                queryResp = quotestable.query(
                    KeyConditionExpression = Key('group').eq(group),
                    Limit = pageSize
                )
        except ClientError as e:
            print("Failed to retrieve quotes for group #{}: {}".format(group, e))
            return {'statusCode': 500,
                    'body': 'Error querying database' }
        except Exception as e:
            print(e)
            return {'statusCode': 500, 'body': 'Internal server error'}
        
        result = {
            'items': json.dumps(queryResp['Items']),
            'startKey': json.dumps(queryResp['LastEvaluatedKey'])
        }
        
        if queryResp.get['LastEvaluatedKey']:
            result['startKey'] = json.dumps(queryResp['LastEvaluatedKey'])
        
        count = len(queryResp['Items'])
        if (count == 0):
            return {
                'statusCode': 404,
                'body': 'No data found'
            }
        elif (len(queryResp['Items']) > 0):
            return {
                'statusCode': 200,
                'body': json.dumps(result)
            }
        else:
            print(queryResp)
            return {
                'statusCode': 500,
                'body': 'Unexpected error'
            }
            
    elif httpMethod == 'PUT':
        try:
            quote = json.loads(event['body'])
            quote['group'] = event['pathParameters']['group']
            quote['dateTime'] = str(datetime.datetime.now())
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
        
        try:
            quotestable.put_item(
                Item = quote
                )
        except ClientError as e:
            print("Failed to store quote: {}", json.dumps(e))
            return {'statusCode': 500, 'body': 'Internal error storing quote.  Please try again.'}
        
        print('Success!')
        return {'statusCode': 200, 'body': json.dumps(quote)}
    else:
        return {
            'body': "Invalid HTTP verb: {}".format(httpMethod),
            'statusCode': 400
        }