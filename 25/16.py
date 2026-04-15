def fact(x):
    d = []
    i = 2
    while i**2<= x:
        while x%i==0:
            d.append(i)
            x = x // i
        i += 1
    if x > 1:
        d.append(x)
    return d
for x in range(7_305_679,7_307_000):
    d = fact(x)
    if len(d) == 4 and str(sum(d))[::-1] == str(sum(d)):
        print(x,sum(d))