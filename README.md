# AWS Secret

AWS Secret is a utility that can interact with secrets stored in AWS Secrets Manager.

## Requirements

- AWS credentials [configured](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration)

## Installation

### From source

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

```bash
usage: aws_secret.py [-h] --secret_id SECRET_NAME
```

Example:

```bash
AWS_DEFAULT_REGION=us-east-2 aws_secret.py -s test
```

## References

1. [Boto3 Quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
1. [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)
1. [Boto3 Docs - AWS Secrets Manager](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/secrets-manager.html)
1. [How do I assume an IAM role using the AWS CLI?](https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-cli/)
