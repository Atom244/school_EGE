from ipaddress import *

net = ip_network('0.0.0.0/255.255.240.0',0)

print(net.num_addresses - 2)
# ИЛИ ТАК:
# k = 0
# for ip in net.hosts():
#     k += 1
# print(k)
