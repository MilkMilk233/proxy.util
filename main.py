from conf.credentials import *
from src.azure import process_azure
from src.aws import process_aws
from utils.oss_upload import oss_upload
from utils.aliyun_monitor import update_aliyun_monitor

def main(servers = servers) -> None:
    for server in servers:
        if server["vendor"] == "aws":
            server["address"] = process_aws(server)
        elif server["vendor"] == "azure":
            server["address"] = process_azure(server)
        elif server["vendor"] == "digitalocean":
            pass
        else:
            raise Exception("Unknown vendor: %s" % server["vendor"]) 
    oss_upload(servers)
    
if __name__ == "__main__":
    main()