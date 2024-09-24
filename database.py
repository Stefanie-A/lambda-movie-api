import boto3

dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('movies-data')

def update_table(table):
    table.put_item(
            Item={
                'id': '1',
                'title': 'Only murders in the building',
                'year': '2024',
                'thumbnailuri': 's3://movie-buck/omtib',
                'genre': 'comedy'
                }
        )
    table.put_item(
            Item={
                'id': '2',
                'title': 'gifted',
                'year': '2017',
                'thumbnailuri': 's3://movie-buck/movie',
                'genre': 'Drama'
            }
        )
    table.put_item(    
            Item={
                'id': '3',
                'title': 'players',
                'year': '2024',
                'thumbnailuri': 's3://movie-buck/movie',
                'genre': 'Romance'
            }
        )
    table.put_item(    
            Item={
                'id': '4',
                'title': 'Uglies',
                'year': '2024',
                'thumbnailuri': 's3://movie-buck/uglies',
                'genre': 'Romance'
            }
        )
    table.put_item(    
            Item={
                'id': '5',
                'title': 'The union',
                'year': '2024',
                'thumbnailuri': 's3://movie-buck/movie',
                'genre': 'Action'
            }
        )
    table.put_item(    
            Item={
                'id': '6',
                'title': 'Family switch',
                'year': '2024',
                'thumbnailuri': 's3://movie-buck/movie',
                'genre': 'Comedy'
            }
        )
    table.put_item(    
            Item={
                'id': '7',
                'title': 'Love again',
                'year': '2023',
                'thumbnailuri': 's3://movie-buck/movie',
                'genre': 'Romance'
            }
        )
    table.put_item(    
            Item={
                'id': '8',
                'title': 'A perfect pairing',
                'year': '2022',
                'thumbnailuri': 's3://movie-buck/movie',
                'genre': 'Romance'
            }
        )
    table.put_item(    
        Item={
            'id': '9',
            'title': 'Mowgli',
            'year': '2018',
            'thumbnailuri': 's3://movie-buck/movie',
            'genre': 'Adventure'
            }
        )
    table.put_item(    
        Item={
            'id': '10',
            'title': 'Leo',
            'year': '2023',
            'thumbnailuri': 's3://movie-buck/movie',
            'genre': 'Comedy'
            }
        )
    
    return {"message": "successfully updated"}