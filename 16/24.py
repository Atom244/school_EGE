def f(n):
    if n <= 1:
        return n
    if n >1 and n%3==0:
        return n + f(n/3)
    if n >1 and n%3!=0:
        return n + f(n+3)
for k in range(1,10000):
    try:
        if f(k) > 100:
            print(k)
    except:
        pass