from ipaddress import *

for mask in range(33):
    net = ip_network(f'173.103.25.118/{mask}', 0)
    if f'173.103.24.0/{mask}' == str(net):
        print(net, 32-mask)