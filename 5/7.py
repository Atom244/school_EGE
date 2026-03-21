for n in range(1, 1000):
    b = str(bin(n)[2:])
    b = b + b[-1]

    if b.count('1')%2==0:
        b = b + '0'
    else:
        b = b + '1'

    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'

    r = int(b, 2)

    if r>144:
        print(n,r)
# 156