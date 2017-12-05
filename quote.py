import os
import json
import boto3
from botocore.exceptions import ClientError
import uuid
import datetime

if os.getenv("AWS_SAM_LOCAL"):
    dynamodb = boto3.resource('dynamodb',endpoint_url = "http://localhost:8000")
else:
    dynamodb = boto3.resource('dynamodb')

quotestable = dynamodb.Table(os.getenv('TABLE_NAME') or 'quotes')

def handler(event, context):
    print(event)
    if event['http_method']  == 'GET':
        item = {
            'id': str(uuid.uuid4()),
            'date': str(datetime.datetime.now())
        }
        
        try:
            resp = quotestable.put_item(
                Item = item
            )
        except ClientError as e:
            return {'statusCode': e.response['ResponseMetadata']['HTTPStatusCode'],
                    'body': "DynamoDB error '{}'".format(e.response['Error']['Message'])}
        
        return {
            'body': "Created new quote #{} at {}".format(item['id'], item['date'])
        }