from ipaddress import *

mask_set = set()

for mask in range(33):
    net = ip_network(f'76.155.48.2/{mask}', 0)
    if str(net.network_address) == '76.155.48.0':
        mask_set.add(net.netmask)
print(len(mask_set))