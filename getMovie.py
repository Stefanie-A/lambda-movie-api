import json
from database import update_table  # Import the function from database.py
import boto3
from boto3.dynamodb.conditions import key

dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('movies-data')

def lambda_handler(event, context):
    update_table(table)
    print(event)
    try:
        if event["routeKey"] == "GET /getmovies":
            statusCode = 200
            response = table.scan()
            data = response['Items']
            print(data)
            return {
                'statusCode': statusCode,
                'body': json.dumps({
                    'message': data
                })
            }
        elif event["routeKey"] == "GET /getmovies/{year}":
            year = event['pathParameters']['year']
            result = table.query(
                KeyConditionExpression=Key('year').eq(year)
            )
            data = result.get("Items", [])
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Movies found',
                    'response': data
                })
            }
        elif event["routeKey"] == "DELETE /deletemovies/{year}":
            year = event['pathParameters']['year']
            result = table.query(
                KeyConditionExpression=Key('year').eq(year)
            )
            items_to_delete = result.get('Items', [])
            for item in items_to_delete:
                table.delete_item(
                    Key={
                        'year': item['year'],  
                    }
                )
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': f'All movies from year {year} deleted successfully'
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
