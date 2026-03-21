for n in range(1, 1000):
    b = str(bin(n*2)[2:])

    b = b + str(sum(map(int, b))%2)
    b = b + str(sum(map(int, b)) % 2)
    r = int(b, 2)
    if r > 1017:
        print(n,r)
