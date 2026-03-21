from ipaddress import *

net = ip_network("23.78.143.87/255.255.240.0", 0)

def find_fw_zeroes(x):
    n = 0
    for el in x:
        if el != '1':
            n += 1
        else:
            break
    return n


k = 0
for ip in net:
    ipb = f"{ip:b}"
    b1 = find_fw_zeroes(ipb[:8])
    b2 = find_fw_zeroes(ipb[8:16])
    b3 = find_fw_zeroes(ipb[16:24])
    b4 = find_fw_zeroes(ipb[24:32])
    if b1+b2+b3+b4 > 6:
        k += 1



print(k)
