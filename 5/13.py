for n in range(1, 1000):
    b = str(bin(n)[2:])
    s = sum(map(int, b))

    if s %2==0:
        b = b + '0'
        b = '10' + b[2:]
    else:
        b = b + '1'
        b = '11' + b[2:]
    r = int(b, 2)
    if r < 35:
        print(n,r)