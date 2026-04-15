def div(x):
    dividers = set()
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            dividers.add(i)
            dividers.add(x//i)
    return dividers

for x in range(300001,301000):
    d = div(x)
    crat = [el for el in d if el%3==0 and el!=x]
    if len(crat) == 5:
        print(x,max(crat))