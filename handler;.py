
import json
import boto3
import os
import uuid

# Retrieve the DynamoDB table name from environment variables (configured in serverless.yml)
TABLE_NAME = os.environ.get('DYNAMODB_TABLE', 'Items')

# Initialize DynamoDB resource and Table object
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    """
    A simple Lambda function that handles API Gateway events to interact with DynamoDB.
    Supports GET to list items and POST to create a new item.
    """
    http_method = event.get("httpMethod", "")
    
    if http_method == "GET":
        return get_items()
    elif http_method == "POST":
        return create_item(event)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Unsupported method"})
        }

def get_items():
    """Retrieve all items from the DynamoDB table."""
    try:
        response = table.scan()
        items = response.get("Items", [])
        return {
            "statusCode": 200,
            "body": json.dumps(items)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

def create_item(event):
    """Create a new item in the DynamoDB table."""
    try:
        data = json.loads(event.get("body", "{}"))
        item_id = str(uuid.uuid4())
        item = {
            "id": item_id,
            "data": data.get("data", "default")
        }
        table.put_item(Item=item)
        return {
            "statusCode": 201,
            "body": json.dumps(item)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
