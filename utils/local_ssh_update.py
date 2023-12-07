def update_ssh(dns_addr, absolute_path, host = "AWSEC2", user = "ubuntu", port = "22"):
    return """
    Host %s\n\
    HostName %s\n\
    User %s\n\
    Port %s\n\
    IdentityFile "%s"
    """ % (host, dns_addr, user, port, absolute_path)

def update_ssh(addr_list):
    content = ""
    for i in addr_list:
        content += update_ssh(i[0], i[1])
    