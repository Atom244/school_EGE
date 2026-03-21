for n in range(1, 101):
    b = str(bin(n)[2:])
    b = str(int(b[::-1]))
    r = int(b, 2)
    if r == 13:
        print(n,r)
# 88