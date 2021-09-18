import boto3
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "cbc-client-id"
    region_name = "us-east-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name,
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
    
    else:
        if 'SecretString' in get_secret_value_response:
            text_secret_data = get_secret_value_response['SecretString']
            print(text_secret_data)
        else:
            binary_secret_data = get_secret_value_response['SecretBinary']

get_secret()
