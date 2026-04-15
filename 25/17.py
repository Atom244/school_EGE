def div(x):
    dividers = set()
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            dividers.add(i)
            dividers.add(x//i)
    return dividers

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

for x in range(5_000_001, 5_900_000):
    if x%2 != 0:
        d = sorted(fact(x))
        h = set(d)
        nech = [el for el in h if el%2!=0]
        if len(d) == 2 and len(nech) == 2 and len(div(d[-1]-d[-2])) == 0:
            print(x,max(d))
