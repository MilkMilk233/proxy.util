import sys
from conf.credentials import *
from src.azure import process_azure
from src.aws import process_aws
from utils.oss_upload import oss_upload
from utils.aliyun_monitor import update_aliyun_monitor

def main(servers = servers) -> None:
    for server in servers:
        if server["vendor"] == "aws":
            server["ip_address"] = process_aws(server)
        elif server["vendor"] == "azure":
            server["ip_address"] = process_azure(server)
        elif server["vendor"] == "digitalocean":
            pass
        else:
            raise Exception("Unknown vendor: %s" % server["vendor"]) 
    oss_upload(servers)
    update_aliyun_monitor(servers)
    
if __name__ == "__main__":
    main()
    sys.exit(0)