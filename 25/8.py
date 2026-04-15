def div(x):
    dividers = set()
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            dividers.add(i)
            dividers.add(x//i)
    return sorted(dividers)

for x in range(190201,190261):
    d = div(x)
    chet = [el for el in d if el%2==0]
    if len(chet) == 4:
        print(chet[-1], chet[-2])
