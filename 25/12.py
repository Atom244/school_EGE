def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i==0:
            d.append(i)
            x = x//i
        i += 1
    if x > 1:
        d.append(x)
    return set(d)

for x in range(499999,498000,-1):
    d = fact(x)
    s = sum(d)
    if s!=0 and s%10==0:
        print(x,s)