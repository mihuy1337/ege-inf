from ipaddress import *

net = ip_network('10.48.96.0/255.255.240.0', 0)
k=0
for addresses in net:
    addresses_bin = bin(int(addresses))[2:].zfill(32)
    if addresses_bin.count('1')>addresses_bin.count('0'):
        k+=1
print(k)