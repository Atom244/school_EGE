def div(x):
    dividers = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            dividers.add(i)
            dividers.add(x//i)
    return dividers

for x in range(250201,251000):
    d = div(x)
    if d:
        s = max(d)+min(d)
    else: s = 0
    if s%123==17:
        print(x,s)