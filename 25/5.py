def div(x):
    dividers = set()
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            dividers.add(i)
            dividers.add(x//i)
    return sorted(dividers)

for x in range(154026,154044):
    d = div(x)
    if len(d) == 4:
        print(d[-2], d[-1])