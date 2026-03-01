from ipaddress import *

net = ip_network('10.100.202.34/255.255.240.0', 0)
print(max(net.hosts()))