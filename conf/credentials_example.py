aliyun_oss_conf = {
        "access_key": "xxxxxxxxxxxxxxxxxxxxxxxx",
        "secret_key": "xxxxxxxxxxxxxxxxxxxxxxxx",
        "endpoint": "https://oss-cn-shenzhen.aliyuncs.com",
        "bucket_name": "xxxxxx",
        "url": {
            "ios": "static/xxx",
            "win": "static/xxx"
        }
    }

aliyun_cms_conf = {
        "access_key": "xxxxxxxxxxxxxxxxxxxxx",
        "secret_key": "xxxxxxxxxxxxxxxxxxxxx",
        "endpoint": "metrics.cn-shenzhen.aliyuncs.com",
}

servers = [
        {
            "vendor": "azure",
            "dns_address": "xxxxxxxxxx.xxxxxxxx.cloudapp.azure.com",
            "remark": "Azure-xx",
            "aliyun_cms_task_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "port": "xxxx",
            "password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "method": "chacha20-ietf-poly1305"
        },
        {
            "vendor": "azure",
            "dns_address": "xxxx.xxxxxxxx.cloudapp.azure.com",
            "remark": "Azure-xx",
            "aliyun_cms_task_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "port": "xxxx",
            "password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "method": "chacha20-ietf-poly1305"
        }
    ]