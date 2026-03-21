for n in range(100, 1000):
    s = str(n)

    a = int(s[0]) * int(s[1])
    b = int(s[1]) * int(s[2])

    if a < b:
        r = str(b) + str(a)
    else:
        r = str(a) + str(b)
    if r == '240':
        print(n)
