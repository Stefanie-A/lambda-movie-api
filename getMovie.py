import json
from database import update_table  # Import the function from database.py
import boto3

dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('movies-data')

def lambda_handler(event, context):
    # Call the update_table function and update the items in the table
    result = update_table(table)    
    # Initialize the response with the first scan of the table
    response = table.scan()
    data = response['Items']
    
    # Paginate through the data if needed
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    
    # Return the collected data along with the result of update_table
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Lambda!',
            'result': result,
            'response': data  # Correct variable name here
        })
    }


    