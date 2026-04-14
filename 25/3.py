def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i == 0:
            d.append(i)
            x = x // i
        i += 1
    if x > 1: d.append(x)
    return d

for i in range(6651221,6660000):
    p = fact(i)
    if len(p) == 2 and str(p[0]).count('2')==1 and str(p[1]).count('2')==1:
        print(i, max(p))

