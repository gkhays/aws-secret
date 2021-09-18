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

Assume the dev (or stage or prod) role beforehand. See [assume-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html) in the AWS CLI.

```bash
usage: aws_secret
```

## References

1. [Boto3 Quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
1. [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)
1. [Boto3 Docs - AWS Secrets Manager](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/secrets-manager.html)
1. [How do I assume an IAM role using the AWS CLI?](https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-cli/)
