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
    return {'statusCode': 200, 'body':'Nothing to see here yet...'}