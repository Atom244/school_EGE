def div(n):
    dividers = set()
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            dividers.add(i)
            dividers.add(n//i)
    return sorted(dividers)

for x in range(190061,190073):
    d = sorted(set([i for i in div(x) if i%2!=0])) 
    if len(d) == 4:
        print(d[-1], d[-2])
