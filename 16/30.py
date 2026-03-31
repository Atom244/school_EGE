from functools import lru_cache

@lru_cache(None)
def f(n):
    if n>=10000:
        return n
    if n <10000 and n%3==0:
        return n + f(n//3)
    else:
        return 2*n + f(n + 3)

for i in range(10000, 1, -1):
     if i%3!=0: f(i)
print(f(999) - f(46))