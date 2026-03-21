def cc(x):
    s = ''
    while x > 0:
        s = str(x%6) + s
        x = x // 6
    return s

for n in range(1, 1000):
    b = cc(n)

    if n%3==0:
        b = b + b[:2]
    else:
        b = b + cc(n%3*10)
    r = int(b, 6)

    if r > 680:
        print(n,r)