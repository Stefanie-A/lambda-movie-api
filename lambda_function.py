import boto3
import json
import logging
from botocore.exceptions import ClientError

#tableName = 'movie-data'

def lambda_handler(event, context):  
    body = {}    
    statusCode = 200
        try:
        if event['routekey'] == "GET /items":
            body = table.scan()
            body = body["Items"]
            print("ITEMS----")
            print(body)
            responseBody = []
            for items in body:
                responseItems = [
                    {'Title': items['title'], 'year': items['year'], 'thumbnailuri': items[''], 'Genre': items['genre']}]
                responseBody.append(responseItems)
            body = responseBody
        elif event['routekey'] == "GET /items/{year}":
            body = table.get_item(
                Key={'year': event['pathparameters']['year']})
            body = body["Item"]
            responseBody = [
                {'Title' : body['title'], 'Year': body['year'], 'Thumbnailuri': body[''], 'Genre': body['genre']}
            ]
    except KeyError:
            statusCode = 400
            body = 'Unsupported route: ' + event['routeKey']
        body = json.dumps(body)
        res = {
            "statusCode": statusCode,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": body
        }
        return res



   # headers = {
    #    "Content-Type": "application/json"
    #}

    # try:
    #     if event['routeKey'] == "DELETE /items/{id}":
    #         table.delete_item(
    #             Key={'id': event['pathParameters']['id']})
    #         body = 'Deleted item ' + event['pathParameters']['id']
    #     elif event['routeKey'] == "GET /items/{id}":
    #         body = table.get_item(
    #             Key={'id': event['pathParameters']['id']})
    #         body = body["Item"]
    #         responseBody = [
    #             {'price': float(body['price']), 'id': body['id'], 'name': body['name']}]
    #         body = responseBody
    #     elif event['routeKey'] == "GET /items":
           
    #     elif event['routeKey'] == "PUT /items":
    #         requestJSON = json.loads(event['body'])
    #         table.put_item(
    #             Item={
    #                 'id': requestJSON['id'],
    #                 'price': Decimal(str(requestJSON['price'])),
    #                 'name': requestJSON['name']
    #             })
    #         body = 'Put item ' + requestJSON['id']
   

    