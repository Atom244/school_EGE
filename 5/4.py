for n in range(1, 1000):
    b = str(bin(n)[2:])

    s = sum(map(int, b)) % 2
    b = b + str(s)

    s = sum(map(int, b)) % 2
    b = b + str(s)

    r = int(b, 2)
    if r > 80:
        print(n, r)

# 86
