from ipaddress import *

for host in enumerate(ip_network('0.0.0.0/255.255.240.0', 0).hosts()):
    print(host)


