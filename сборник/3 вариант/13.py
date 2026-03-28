from ipaddress import *

net = ip_network('89.16.43.107/255.224.0.0', 0).hosts()

print(''.join(str(max(net)).split('.')))