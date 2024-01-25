import os

def update_aliyun_monitor(servers):
    for i in servers:
        # if the i has the key "aliyun_cms_task_id", then update the monitor
        if "aliyun_cms_task_id" in i:
            os.system("aliyun cms ModifySiteMonitor --TaskId %s --Address %s" % (i["aliyun_cms_task_id"],i["ip_address"]))