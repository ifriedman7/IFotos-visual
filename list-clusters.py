import io
import os
import sys
import re

import boto3
from botocore.exceptions import ClientError


eks = boto3.client('eks')

try:
    response = eks.list_clusters()
    print(f"List is \n{response}\n")
except ClientError as err:
    print(f"Couldn't get the list.")
    print(f"\t{err.response['Error']['Code']}:{err.response['Error']['Message']}")
