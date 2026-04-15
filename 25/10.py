def div(x):
    dividers = set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            dividers.add(i)
            dividers.add(x//i)
    return sorted(dividers)

for x in range(500001,501000):
    d = div(x)
    m = [el for el in d if el!=8 and el%10==8 and el!=x]
    if m:
        print(x,min(m))