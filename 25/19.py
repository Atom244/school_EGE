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
for x in range(2_700_001,2_800_000):
    if x%100 == 34:
        d = fact(x)
        povt = [x for x in d if d.count(x)>=5]
        if povt:
            print(x,min(povt))
