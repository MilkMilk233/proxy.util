import os
from dependencies.alibabacloud_tea_openapi import models as open_api_models
from dependencies.alibabacloud_cms20190101.client import Client as Client
from dependencies.alibabacloud_cms20190101 import models as models
from conf.credentials import aliyun_cms_conf

def update_aliyun_monitor(servers):
    config = open_api_models.Config(
        # 您的AccessKey ID,
        access_key_id=aliyun_cms_conf["access_key"],
        # 您的AccessKey Secret,
        access_key_secret=aliyun_cms_conf["secret_key"]
    )
    # 访问的域名
    config.endpoint = aliyun_cms_conf["endpoint"]
    client = Client(config)
    for server in servers:
        request = models.ModifySiteMonitorRequest(task_id = server["aliyun_cms_task_id"], address = server["ip_address"])
        response = client.modify_site_monitor(request)
        print("Response:",response)
        
        