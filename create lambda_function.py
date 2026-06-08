import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

def lambda_handler(event, context):

    employee_id = str(uuid.uuid4())

    body = json.loads(event['body'])

    item = {
        'employeeId': employee_id,
        'name': body['name'],
        'email': body['email'],
        'department': body['department']
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Employee Added',
            'employeeId': employee_id
        })
    }