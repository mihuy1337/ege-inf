from ipaddress import *
m = []
for ip in ip_network('192.168.63.0/255.255.255.128', 0):
    b = ''.join([bin(int(byte))[2:].zfill(8) for byte in str(ip).split('.')])
    if b.count('0')%5!=0:
        m.append(b)
print(m)
print(len(m))
