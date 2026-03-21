
for n in range(1, 1000):
    bin_n = str(bin(n)[2:]) + '1'

    if bin_n.count('1') % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'

    if bin_n.count('1') % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'

    dec_r = int(bin_n, 2)
    print(dec_r)

# 172