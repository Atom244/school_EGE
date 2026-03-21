def cc(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x = x // 3
    return s
for n in range(1, 1000):
    b = cc(n)

    if n%3==0:
        b = '1' + b + '02'

    else:
        b = b + cc(n%3*4)

    r = int(b, 3)
    if r < 199:
        print(n, r)