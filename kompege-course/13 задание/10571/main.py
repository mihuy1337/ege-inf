from ipaddress import *

for mask in range(33):
    net = ip_network(f'122.21.49.91/{mask}', 0)
    if f'122.21.48.0/{mask}' == str(net):
        print(net, mask)