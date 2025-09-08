from ipaddress import *
for mask in range(33):
    net1 = ip_network(f"157.127.182.76/{mask}", 0)
    net2 = ip_network(f"157.127.190.80/{mask}", 0)
    if net1 != net2: # net1 != net2   !!!!!!!!!!!!!!!!!!!!!!!!!!!!! str(net1.netmask).count('1') == str(net2.netmask).count('1') and net1 != net2 ХОТЯ ЭТО НЕНУЖНЫЕ ВЫЧИСЛЕНИЯ
        print(net1)
# 21