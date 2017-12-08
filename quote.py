import os
import json
import boto3
import uuid
import time
import logging

from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if os.getenv("AWS_SAM_LOCAL"):
    dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')
else:
    dynamodb = boto3.resource('dynamodb')

tableName = os.getenv('TABLE_NAME') or 'awscodestar-infinite-quotes-lambda-QuotesTable-1RB5F97XSMSKS'
quotestable = dynamodb.Table(tableName)

def handler(event, context):
    logger.info("Got event: {}".format(json.dumps(event)))
    httpMethod = event['requestContext']['httpMethod'] or 'GET'
    
    if httpMethod == 'GET':
        group = event['pathParameters']['group']
        
        queryParams = event.get('queryStringParameters') or {}
        
        startKey = queryParams.get('startKey')
        pageSize = int(queryParams.get('pageSize','20'))
        
        logger.info("Page size is {}".format(pageSize))
        
        try:
            if (startKey):
                queryResp = quotestable.query(
                    KeyConditionExpression = Key('group').eq(group),
                    ExclusiveStartKey = {'group': group, 'timestamp': startKey},
                    Limit = pageSize,
                    ScanIndexForward = False
                )
            else:
                queryResp = quotestable.query(
                    KeyConditionExpression = Key('group').eq(group),
                    Limit = pageSize,
                    ScanIndexForward = False
                )
        except ClientError as e:
            print("Failed to retrieve quotes for group #{}: {}".format(group, e))
            return {'statusCode': 500,
                    'body': 'Error querying database' }
        except Exception as e:
            logger.error(e)
            return {'statusCode': 500, 'body': 'Internal server error'}
        
        result = {
            'items': queryResp['Items']
        }
        
        if queryResp.get('LastEvaluatedKey'):
            result['startKey'] = queryResp['LastEvaluatedKey']['timestamp']
        
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
            logger.error("Bad response from query: {}".format(json.dumps(queryResp)))
            return {
                'statusCode': 500,
                'body': 'Unexpected error'
            }
            
    elif httpMethod == 'PUT':
        try:
            quote = json.loads(event['body'])
        except:
            return {'statusCode': 405, 'body': 'Malformed JSON input'}
        
        if 'lines' not in quote:
            return {'statusCode': 405, 'body': 'Missing "lines" in request body'}
        
        if len(quote['lines']) == 0:
            return {'statusCode': 405, 'body': 'No lines in quote'}
        
        l = 0
        for line in quote['lines']:
            if 'text' not in line:
                return {'statusCode': 405, 'body': "Line {} has no text".format(l)}
            if 'quoter' not in line:
                return {'statusCode': 405, 'body': "Line {} has no quoter".format(l)}
            l+=1
        
        quote['group'] = event['pathParameters']['group']
        quote['timestamp'] = str(time.time())

        try:
            quotestable.put_item(
                Item = quote
                )
        except ClientError as e:
            logger.error("Failed to store quote: {}".format(json.dumps(e)))
            return {'statusCode': 500, 'body': 'Internal error storing quote.  Please try again.'}
        
        print('Success!')
        return {'statusCode': 200, 'body': json.dumps(quote)}
    else:
        return {
            'body': "Invalid HTTP verb: {}".format(httpMethod),
            'statusCode': 400
        }