from ipaddress import *

net = ip_network('172.16.160.0/255.255.240.0', 0)
print(
    len([
        ip for ip in net if f'{ip:b}'.count('1')%2==0
    ])
)