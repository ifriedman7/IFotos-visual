import io
import os
import sys
import re

import boto3
from botocore.exceptions import ClientError
import requests
from requests_aws4auth import AWS4Auth
#need pip install requests-aws4auth

region = 'us-east-1' # e.g. us-west-1
service = 'eks'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)


eks = boto3.client('eks')

try:
    response = eks.list_clusters()
    print(f"List is \n{response}\n")
except ClientError as err:
    print(f"Couldn't get the list.")
    print(f"\t{err.response['Error']['Code']}:{err.response['Error']['Message']}")
