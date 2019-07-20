import os
import requests


def fetch_url(event, context):
    response = requests.get(os.environ['URL'])

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': response.headers.get('Content-Type'),
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true'
        },
        'body': response.text
    }