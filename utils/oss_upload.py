# Update indicated content to Aliyun OSS
# Last updated: 2024/1/22

import json
import oss2
import tempfile
import os
import random
from conf.credentials import aliyun_oss_conf
from utils.base64 import convertion_to_base64

def oss_upload_win(servers):
    content = {"version": 1, "servers": []}
    for server in servers:
        item = {}
        item["id"] = "27b8a625-4f4b-4428-9f0f-8a2317%s" % ''.join((random.sample(list("123456789"),6)))
        item["remarks"] = server["remark"]
        item["server"] = server["ip_address"]
        item["password"] = server["password"]
        item["server_port"] = server["port"]
        item["method"] = server["method"]
    auth = oss2.Auth(aliyun_oss_conf['access_key'], aliyun_oss_conf['secret_key'])
    bucket = oss2.Bucket(auth, aliyun_oss_conf['endpoint'], aliyun_oss_conf['bucket_name'])
    content = json.dumps(content)
    urls = aliyun_oss_conf['url']["win"]
    temp = tempfile.TemporaryFile()
    temp.write(content.encode("ascii"))
    temp.seek(0, os.SEEK_SET)
    bucket.put_object(urls, temp)
    print("Successfully uploaded windows info to OSS!")

def oss_upload_ios(servers):
    content = ""
    for server in servers:
        content += "ss://" + convertion_to_base64(server["ip_address"]) + "\n"
    auth = oss2.Auth(aliyun_oss_conf['access_key'], aliyun_oss_conf['secret_key'])
    bucket = oss2.Bucket(auth, aliyun_oss_conf['endpoint'], aliyun_oss_conf['bucket_name'])
    temp = tempfile.TemporaryFile()
    temp.write(content.encode("ascii"))
    temp.seek(0, os.SEEK_SET)
    bucket.put_object(aliyun_oss_conf['url']['ios'], temp)
    print("Successfully uploaded iOS info to OSS!")

def oss_upload(servers):
    oss_upload_win(servers)
    oss_upload_ios(servers)