from ipaddress import *
k = 0
net = ip_network("184.178.54.144/255.255.255.240", 0)
for ip in net:
    bin_ip = f"{ip:b}"
    if '111' in bin_ip:
        print(bin_ip)
        k += 1
print(k)
# 16
