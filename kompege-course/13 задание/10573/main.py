from ipaddress import *
a = []
for mask in range(33):
    net = ip_network(f'191.173.145.240/{mask}', 0)
    if f'191.173.144.0/{mask}'==str(net):
        print(net, net.num_addresses)
