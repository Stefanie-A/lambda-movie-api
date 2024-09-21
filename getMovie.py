import json
from database import update_table  # Import the function from database.py
import boto3

dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('movies-data')
update_table(table)

def lambda_handler(event, context):
    print(event)
    try:
        if event["routeKey"] == "GET /getmovies":
            statusCode = 200
            result = update_table(table)
            response = table.scan()
            data = response['Items']
            print(data)
            return {
                'statusCode': statusCode,
                'body': json.dumps({
                    'message': result,
                    'movies': data
                })
            }
        elif event["routeKey"] == "GET /getmovies/{year}":
            result = table.get_item(
                Key={
                    'year': event['pathParameters']['year']  
                }
            )
            result = result.get("Item", {})
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Movie found',
                    'response': result
                })
            }
        else:
            raise KeyError
    except KeyError:
        statusCode = 400
        body = f'Unsupported route: {event.get("routeKey", "Unknown")}'
    except Exception as e:
         statusCode = 500
         body = str(e)
    return {
        "statusCode": statusCode,
        "body": json.dumps({"error": body})
    }
