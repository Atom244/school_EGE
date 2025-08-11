from ipaddress import *

def fullnet2bin(addres):
    item_lst = addres.split("/")
    full_bin = []
    for item in item_lst:
        try:
            full_bin.append(ip2bin(item))
        except:
            full_bin.append("x (maybe it is problem, or you want to find it)")
    for bin_addres in full_bin:
        print(bin_addres)

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


fullnet2bin("255.255.255.0/117.73.192.0/117.73.192.0")
