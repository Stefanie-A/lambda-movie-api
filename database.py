import boto3

dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('movies-data')

def update_table(table):
    table.put_item(
            Item={
                'id': '1',
                'title': 'Perfect find',
                'year': '2018',
                'thumbnailuri': '',
                'genre': 'comedy'
                }
        )
    table.put_item(
            Item={
                'id': '2',
                'title': 'gifted',
                'year': '2017',
                'thumbnailuri': '',
                'genre': 'Drama'
            }
        )
    table.put_item(    
            Item={
                'id': '3',
                'title': 'players',
                'year': '2024',
                'thumbnailuri': '',
                'genre': 'Romance'
            }
        )
        
    return {"message": "successfully updated"}