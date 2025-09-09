from ipaddress import *
k = 0
net = ip_network('192.168.240.0/255.255.255.0', 0)
for ip in net:
    if f'{ip:b}'.count('1') == f'{ip:b}'.count('0'):
        k += 1
print(k)
# 8
