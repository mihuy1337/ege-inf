from ipaddress import *
k=0
for mask in range(33):
    net = ip_network(f'158.116.11.146/{mask}', 0)
    if f'158.116.0.0/{mask}' == str(net):
        k+=1
        print(net, k)