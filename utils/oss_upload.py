# Update indicated content to Aliyun OSS
# Last updated: 2023/12/7

import json
import oss2
import tempfile
import os
import sys

def get_credentials():
    with open("../conf/credentials.json", "r") as f:
        credentials = json.load(f)
    return credentials

def oss_upload_win(content):
    try:
        credentials = get_credentials()
        auth = oss2.Auth(credentials['oss']['access_key'], credentials['oss']['secret_key'])
        bucket = oss2.Bucket(auth, credentials['oss']['endpoint'], credentials['oss']['bucket_name'])
        urls = credentials['oss']['url']
        temp = tempfile.TemporaryFile()
        temp.write(content.encode("ascii"))
        temp.seek(0, os.SEEK_SET)
        bucket.put_object(credentials['oss']['url']['win'], temp)
    except:
        input("Error: OSS upload (windows info) failed! Press any key to exit...")
        sys.exit()
    print("Successfully uploaded windows info to OSS!")

def oss_upload_ios(content):
    try:
        credentials = get_credentials()
        auth = oss2.Auth(credentials['oss']['access_key'], credentials['oss']['secret_key'])
        bucket = oss2.Bucket(auth, credentials['oss']['endpoint'], credentials['oss']['bucket_name'])
        temp = tempfile.TemporaryFile()
        temp.write(content.encode("ascii"))
        temp.seek(0, os.SEEK_SET)
        bucket.put_object(credentials['oss']['url']['ios'], temp)
    except:
        input("Error: OSS upload (ios info) failed! Press any key to exit...")
        sys.exit()
    print("Successfully uploaded ios info to OSS!")