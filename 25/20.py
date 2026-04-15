def prime(x):
    return x>1 and all([x%i!=0 for i in range(2,int(x**0.5)+1)])
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
for x in range(102,112):
    if prime(x):
        print(x**4, x**3)

