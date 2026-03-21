for n in range(1, 10000):
    b = str(bin(n)[2:])
    zeroes = 0
    ones = 0
    d = [x for x in b]
    for i in range(len(d)):
        if (i+1)%2 == 0 and d[i] == '1':
            ones += 1
        if (i+1)%2 != 0 and d[i] == '0':
            zeroes += 1
    r = abs(zeroes - ones)
    if r == 5:
        print(n, r)