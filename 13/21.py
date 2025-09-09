from ipaddress import *

for mask in range(33):
    net = ip_network(f'191.173.145.240/{mask}', 0)
    if str(net.network_address) == '191.173.144.0':
        print(net.num_addresses)

# 512
