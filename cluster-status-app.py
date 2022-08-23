from flask import Flask, request, render_template

"""    With Flask as webapp
"""

import datetime
import time
import urllib.parse
import urllib.request
import urllib.error
import json
import io
import os
import sys
import re

From dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError
import requests
from requests_aws4auth import AWS4Auth
#need pip install requests-aws4auth
# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

@app.route('/')
def cluster_status():
    load_dotenv()
    region = 'us-east-1' # e.g. us-west-1
    service = 'eks'
    credentials = boto3.Session().get_credentials()
    with open('env.txt', 'w', encoding="utf-8") as f:
        f.write(f"{os.environ}" + "\n")
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
    eks = boto3.client('eks')

    try:
        response = eks.list_clusters()
        cluster_list = response['clusters']
        print(f"List is \n{cluster_list}\n")
    except ClientError as err:
        print(f"Couldn't get the list.")
        print(f"\t{err.response['Error']['Code']}:{err.response['Error']['Message']}")
    if 'ike-eks-cluster' in cluster_list:
        print(f"Cluster is up.")
        cluster_up = True
    else:
        print(f"Cluster is down.")
        cluster_up = False
    return render_template('index.html', cluster_up)
if __name__ == '__main__':
    app.run(debug=True)
