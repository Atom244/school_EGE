def div(x):
    dividers = set()
    for i in range(2,int(x**0.5)):
        if x%i == 0:
            dividers.add(i)
            dividers.add(x//i)
    return sorted(dividers)

for x in range(150001,151000):
    d = div(x)
    if d:
        s = sum(d)
    else:s = 0
    if s%13==10:
        print(x,s)