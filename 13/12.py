from ipaddress import *
for mask in range(33):
    net = ip_network(f"175.122.80.13/{mask}", 0)
    if net.num_addresses >= 60 and str(net.network_address) == '175.122.80.0':
        print(net)

# 7
