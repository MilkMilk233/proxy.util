# Update indicated content to Aliyun OSS
# Last updated: 2024/1/22

import json
import oss2
import tempfile
import os
import random
from ..conf.credentials import aliyun_oss_conf

def oss_upload_win(servers, aliyun_oss_conf):
    content = {"version": 1, "servers": []}
    for server in servers:
        item = {}
        item["id"] = "27b8a625-4f4b-4428-9f0f-8a2317%s" % ''.join((random.sample(list("123456789"),6)))
        item["remarks"] = server["remark"]
        item["server"] = server["address"]
    auth = oss2.Auth(server['oss']['access_key'], credentials['oss']['secret_key'])
    bucket = oss2.Bucket(auth, credentials['oss']['endpoint'], credentials['oss']['bucket_name'])
    urls = credentials['oss']['url']
    temp = tempfile.TemporaryFile()
    temp.write(content.encode("ascii"))
    temp.seek(0, os.SEEK_SET)
    bucket.put_object(credentials['oss']['url']['win'], temp)
    print("Successfully uploaded windows info to OSS!")

def oss_upload_ios(content):
    for server in servers:
        auth = oss2.Auth(credentials['oss']['access_key'], credentials['oss']['secret_key'])
        bucket = oss2.Bucket(auth, credentials['oss']['endpoint'], credentials['oss']['bucket_name'])
        temp = tempfile.TemporaryFile()
        temp.write(content.encode("ascii"))
        temp.seek(0, os.SEEK_SET)
        bucket.put_object(credentials['oss']['url']['ios'], temp)
    print("Successfully uploaded iOS info to OSS!")

def oss_upload(servers):
    pass