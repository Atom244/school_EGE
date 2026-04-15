def fact(x):
    d = []
    i = 2
    while i**2 <= x:
        while x%i==0:
            d.append(i)
            x = x // i
        i += 1
    if x > 1:
        d.append(x)
    return d

for x in range(1_324_728,1_326_000):
    d = fact(x)
    s = [el for el in d if str(el).count('5') == 1]
    if len(d) == 2 and len(s) == 2:
        print(x,max(d))