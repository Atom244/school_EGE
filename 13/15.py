from ipaddress import *

net = ip_network("10.8.248.131/255.255.224.0",0)
print(net)
# 10.8.224.0
# F  A  D  E