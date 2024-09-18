import boto3

dynamoDB = boto3.resource('dynamodb')
table = dynamodb.Table('movie-data')

def update_table(table):
    table.put_item(
            Item={
                'title': 'Perfect find',
                'year': '2018',
                'thumbnailuri': '',
                'genre': 'comedy'
                }
        )
        table.put_item(
            Item={
                'title': 'gifted',
                'year': '2017',
                'thumbnailuri': '',
                'genre': 'Drama'
            }
        )
        table.put_item(    
            Item3={
                'title': 'players',
                'year': '2024',
                'thumbnailuri': '',
                'genre': 'Romance'
            }
        )