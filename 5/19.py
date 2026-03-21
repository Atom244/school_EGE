for n in range(100, 1000):
    s = str(n)
    a = int(s[0])**2 + int(s[1])**2
    b = int(s[1])**2 + int(s[2])**2
    if a > b:
        r = int(str(a) + str(b))
    else:
        r = int(str(b) + str(a))
    if r == 9010:
        print(n)