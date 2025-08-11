from ipaddress import *

counter = 0
for ip in ip_network("172.16.168.0/255.255.248.0"):
    if bin(int(ip))[2:].count("1") % 5 != 0:
        counter += 1
print(counter)