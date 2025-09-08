from ipaddress import *

for mask in range(33):
    net = ip_network(f"108.133.75.91/{mask}", 0)
    if str(net.network_address) == '108.133.75.64':
        print(net, net.num_addresses)

# 64
