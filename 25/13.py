def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i==0:
            d.append(i)
            x = x // i
        i += 1
    if x > 1:
        d.append(x)

    return d

for x in range(5_700_001,5_705_000):
    d = fact(x)
    if d:
        m = min(d)+max(d)
    else: m = 0
    if m > 70000 and m**0.5 % 1 == 0:
        print(x,m)