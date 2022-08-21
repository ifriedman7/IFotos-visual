import io
import os
import sys
import re

import boto3
from boto3.s3.transfer import S3UploadFailedError
from botocore.exceptions import ClientError


    s3 = boto3.client('s3')

    try:
        response = s3.list_clusters()
        print(f"List is \n{response}\n")
    except ClientError as err:
        print(f"Couldn't get the list.")
        print(f"\t{err.response['Error']['Code']}:{err.response['Error']['Message']}")
