import os

def update_aliyun_monitor(servers):
    for i in servers:
        os.system("aliyun cms ModifySiteMonitor --TaskId %s --Address %s" % (i["aliyun_cms_task_id"],i["address"]))