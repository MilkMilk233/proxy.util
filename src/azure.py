import os

def process_azure(server) -> str:
    # Acquire server's IP address.
    ip_address = os.popen("dig +short %s" % server["dns_address"]).read().replace("\n","")
    return ip_address