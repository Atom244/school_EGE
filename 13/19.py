from ipaddress import *

for mask in range(33):
    net = ip_network(f'173.103.25.118/{mask}', 0)
    if str(net.network_address) == '173.103.24.0':
        print(f'{net.netmask:b}'.count('0'))
# 11
