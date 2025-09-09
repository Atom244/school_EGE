from ipaddress import *

mask_set = set()

for mask in range(33):
    net = ip_network(f'158.116.11.146/{mask}', 0)
    if str(net.network_address) == '158.116.0.0':
        mask_set.add(net.netmask)
print(len(mask_set))
