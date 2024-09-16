import boto3
import logging
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    dynamoDB = boto3.resource('dynamoDB')
    table = dynamodb.Table('movie')
    table.put_item(
        Item1={
            'title': 'Perfect find'
            'year': '2018'
            'genre': 'comedy'
        }
        Item2={
            'title': 'gifted'
            'year': '2017'
            'genre': 'Drama'
        }
        Item3={
            'title': 'players'
            'year': '2024'
            'genre': 'Romance'
        }
    )


    