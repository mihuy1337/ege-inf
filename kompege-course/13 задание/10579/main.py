from ipaddress import *

net = ip_network('192.168.240.0/255.255.255.0', 0)
k=0
for host in net:
    bin_host = bin(int(host))[2:].zfill(32)
    print(bin_host)
    if bin_host.count('0')==bin_host.count('1'):
        k+=1
print(k)