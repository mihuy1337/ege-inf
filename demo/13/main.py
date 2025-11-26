from ipaddress import *

for ip in ip_network('191.128.66.83/255.192.0.0', 0).hosts():
    print(ip)