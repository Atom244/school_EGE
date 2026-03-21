for n in range(1, 128):
    b = str(bin(n)[2:]).zfill(8)
    b = b.replace('1', '2').replace('0', '1'). replace('2', '0')

    r = int(b, 2)
    r = r + 1
    if r == 153:
        print(n, r)

# 103