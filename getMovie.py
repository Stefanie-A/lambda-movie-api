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
    
    # Collect all items
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


#         try:
#         if event['routekey'] == "GET /items":
#             body = table.scan()
#             body = body["Items"]
#             print("ITEMS----")
#             print(body)
#             responseBody = []
#             for items in body:
#                 responseItems = [
#                     {'Title': items['title'], 'year': items['year'], 'thumbnailuri': items[''], 'Genre': items['genre']}]
#                 responseBody.append(responseItems)
#             body = responseBody
#         elif event['routekey'] == "GET /items/{year}":
#             body = table.get_item(
#                 Key={'year': event['pathparameters']['year']})
#             body = body["Item"]
#             responseBody = [
#                 {'Title' : body['title'], 'Year': body['year'], 'Thumbnailuri': body[''], 'Genre': body['genre']}
#             ]
#     except KeyError:
#             statusCode = 400
#             body = 'Unsupported route: ' + event['routeKey']
#         body = json.dumps(body)
#         res = {
#             "statusCode": statusCode,
#             "headers": {
#                 "Content-Type": "application/json"
#             },
#             "body": body
#         }
#         return res



#    # headers = {
#     #    "Content-Type": "application/json"
#     #}

#     # try:
#     #     if event['routeKey'] == "DELETE /items/{id}":
#     #         table.delete_item(
#     #             Key={'id': event['pathParameters']['id']})
#     #         body = 'Deleted item ' + event['pathParameters']['id']
#     #     elif event['routeKey'] == "GET /items/{id}":
#     #         body = table.get_item(
#     #             Key={'id': event['pathParameters']['id']})
#     #         body = body["Item"]
#     #         responseBody = [
#     #             {'price': float(body['price']), 'id': body['id'], 'name': body['name']}]
#     #         body = responseBody
#     #     elif event['routeKey'] == "GET /items":
           
#     #     elif event['routeKey'] == "PUT /items":
#     #         requestJSON = json.loads(event['body'])
#     #         table.put_item(
#     #             Item={
#     #                 'id': requestJSON['id'],
#     #                 'price': Decimal(str(requestJSON['price'])),
#     #                 'name': requestJSON['name']
#     #             })
#     #         body = 'Put item ' + requestJSON['id']
   

    