def div(x):
    dividers = set()
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            dividers.add(i)
            dividers.add(x//i)
    return dividers

for x in range(1204300,1204381):
    d = div(x)
    chet = [el for el in d if el%2==0 and el!=x]
    s = sum(chet)
    if s !=0 and s%10==0:
        print(x,s)