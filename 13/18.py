from ipaddress import *

for mask in range(33):
    net = ip_network(f"122.21.49.91/{mask}", 0)
    if str(net.network_address) == '122.21.48.0':
        print(f'{net.netmask:b}'.count('1'))
# 20
