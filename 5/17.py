for n in range(1000, 10000):
    s = str(n)
    a = int(s[0]) * int(s[1])
    b = int(s[2]) * int(s[3])

    if a>b:
        r = str(b) + str(a)
    else:
        r = str(a) + str(b)
    if r=='1214':
        print(n)