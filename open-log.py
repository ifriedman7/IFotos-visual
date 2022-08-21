import io
import os
import sys
import uuid
import re

import boto3
from boto3.s3.transfer import S3UploadFailedError
from botocore.exceptions import ClientError

def open_log(args):
    s3 = boto3.client('s3')
    bucket_name = args[0]
    object_name = args[1]
    download_file_path = "current_log.log"
    empty_log = False

    try:
#        s3.download_file(bucket_name, object_name, download_file_path)
        with open(download_file_path, 'wb') as f:
            s3.download_fileobj(bucket_name, object_name, f)
            file_size_bytes = os.stat(download_file_path).st_size
        print(f"Successfully downloaded {object_name} as {download_file_path}. File size is {file_size_bytes} bytes.")
        if (file_size_bytes) == 0:
            empty_log = True
            print(f"But file size is 0.")
    except ClientError as err:
        print(f"Couldn't get the object {object_key} in bucket {bucket.name}.")
        print(f"\t{err.response['Error']['Code']}:{err.response['Error']['Message']}")


if __name__ == '__main__':
    open_log(sys.argv[1:])