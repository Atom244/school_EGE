def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i == 0:
            d.append(i)
            x = x // i
        i += 1
    if x > 1: d.append(x)
    return set(d) # ДЕЛИТЕЛИ

for x in range(9_500_001, 9_509_000):
    d = fact(x)
    if d:
        f = sum(d)//len(d)
    else: f = 0
    if f != 0 and f%813==0:
        print(x,f)
