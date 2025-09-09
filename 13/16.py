from ipaddress import *

for mask in range(33):
    net = ip_network(f"118.193.30.139/{mask}", 0)
    if str(net.network_address) == '118.193.24.0':
        print(net.netmask)
# 248