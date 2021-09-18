import boto3
from .logger import logger

client = boto3.client('secretsmanager')

def get_secret(key):
    logger.info(f'Fetching secret for {key}...')
    response = client.get_secret_value(SecretId=key,)
    return response['SecretString']
