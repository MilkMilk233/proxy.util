import os

def process_azure(server) -> str:
    # Acquire server's IP address.
    ip_address = os.popen('nslookup milk.japaneast.cloudapp.azure.com').read()