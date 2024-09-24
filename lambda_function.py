import json
from database import update_table  # Import the function from database.py
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('movies-data')

def lambda_handler(event, context):
    print(event)
    try:
        if event["routeKey"] == "GET /movies":
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
        elif event["routeKey"] == "GET /movies/{year}":
            year = event['pathParameters']['year']
            result = table.scan(
                FilterExpression=Attr('year').eq(year)
            )
            data = result.get("Items", [])
            if not data:
                return {
                    'statusCode': 404,
                    'body': json.dumps({
                        'message': f'No movies found for year {year}'
                    })
                }
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Movies found',
                    'response': data
                })
            }
        elif event["routeKey"] == "DELETE /movies/{year}":
            year = event['pathParameters']['year']
            result = table.scan(
                FilterExpression=Attr('year').eq(year)
            )
            items_to_delete = result.get('Items', [])
            if not items_to_delete:
                return {
                    'statusCode': 404,
                    'body': json.dumps({
                        'message': f'No movies found for year {year}'
                    })
                }
            for item in items_to_delete:
                table.delete_item(
                    Key={
                        'id': item['id'],
                        'year': item['year']
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
