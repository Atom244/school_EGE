from ipaddress import *

def ip2bin(addres):
    byte_list = addres.split(".")
    bin_ip = ""

    for byte in byte_list:
        bin_byte = bin(int(byte))[2:]
        bin_ip += bin_byte

        if len(bin_byte) < 8:
            bin_ip += "0" * (8 - len(bin_byte))
        bin_ip += " "

    return bin_ip


ip = "117.73.192.0"

print(ip2bin(ip))




# 11111111 11111111 11100000 00000000
# 11101010 10010010 11010000 11011000
# 11101010 10010010 11000000 00000000