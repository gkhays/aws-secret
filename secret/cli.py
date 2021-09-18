import sys
import argparse
from .lib.logger import logger
from .lib.aws import get_secret
from .lib.exceptions import SecretException

# Hard-coding the key for now.
def get_client_id():
    return get_secret('cbc-client-id')

# Hard-coding the key for now.
def get_client_secret():
    return get_secret('cbc-client-secret')

def main(args=None):
    parser = argparse.ArgumentParser(description='Values in Secrets Manager')
    parser.add_argument('--secret_id', '-s', required=True,
                        help='the secret ID for which a value is desired')
    args = parser.parse_args(args)
    try:
        secret_value = get_secret(args.secret_id)
    except Exception as e:
        logger.error(e)
        logger.error('*** Failure to retrieve secret. Exiting ***')
        sys.exit(1)

    if not secret_value:
        logger.info('failed to retrieve the client ID')
        quit(1)
    
    print(f'{args.secret_id}:{secret_value}')
