#python3 -m pip install s3cmd
#python3 -m pip install boto3
import io
import os
import sys
import uuid
import re
import subprocess

import boto3
from boto3.s3.transfer import S3UploadFailedError
from botocore.exceptions import ClientError

def get_logs(args):
#    bucket_name = f'ike-bucket-small-{uuid.uuid4()}'   #generate a random name
    bucket_name = args[0]
#    bucket = s3_resource.Bucket(bucket_name)
    bucket = boto3.resource('s3').Bucket(bucket_name)
    log_pattern = '.*log$'
    bucket_size_cmd = '/usr/local/bin/s3cmd du -H s3://' + bucket_name
    du_result = subprocess.run((bucket_size_cmd.split()), stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(f'\nCurrent size of {bucket_name} is {du_result.split()[0]}.')
    try:
        for o in bucket.objects.all():
            if (re.search(log_pattern, o.key)): 
                print(f"\t{o.key}\t{o.last_modified}")
    except ClientError as err:
        print(f"Couldn't list the objects in bucket {bucket.name}.")
        print(f"\t{err.response['Error']['Code']}:{err.response['Error']['Message']}")


if __name__ == '__main__':
#    get_logs(boto3.resource('s3'))
    get_logs(sys.argv[1:])