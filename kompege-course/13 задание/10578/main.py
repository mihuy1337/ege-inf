from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'10.96.180.231/{mask}', 0)
    net2 = ip_network(f'10.96.140.180/{mask}', 0)
    if net1 != net2:
        print(32 - mask)