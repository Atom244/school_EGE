for n in range(1, 1000):
    b = str(bin(n)[2:])
    if n%2 == 0:
        b = b + '01'
    else:
        b = b + '10'

    r = int(b, 2)
    if r > 81:
        print(n, r)

# 86