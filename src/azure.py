import os
import time
import sys

def process_azure(server) -> str:
    # Acquire server's IP address.
    ip_address = os.popen("nslookup %s" % server["dns_address"]).read()
    try:
        ip_address = ip_address.split('Address: ')[2].split('\n')[0]
    except:
        print('Error: Azure IP acquisition failed. (HK)')
        time.sleep(5)
        sys.exit()
    # Cut the first 1 character of ip_address
    ip_address = ip_address[1:]
    return ip_address