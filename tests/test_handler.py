import json
from handler import lambda_handler

def test_get_items():
    # Simulate an API Gateway GET event
    event = {"httpMethod": "GET"}
    response = lambda_handler(event, None)
    # Check for a 200 OK response
    assert response["statusCode"] == 200
    # The body should be a JSON list (even if empty)
    items = json.loads(response["body"])
    assert isinstance(items, list)

def test_create_item():
    # Simulate an API Gateway POST event with a sample payload
    payload = {"data": "Hello, Serverless!"}
    event = {
        "httpMethod": "POST",
        "body": json.dumps(payload)
    }
    response = lambda_handler(event, None)
    assert response["statusCode"] == 201
    item = json.loads(response["body"])
    assert "id" in item
    assert item["data"] == "Hello, Serverless!"
