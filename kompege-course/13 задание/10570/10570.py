from ipaddress import *

for mask in range(32):
    net = ip_network(f'154.201.208.17/{mask}', 0)
    if f'154.201.192.0/{mask}' == str(net):
        print(net, net.netmask)