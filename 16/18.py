from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 18:
        return n + 3
    if n > 18 and n%3==0:
        return (n//3)*f(n//3)+n-12
    if n > 18 and n%3!=0:
        return f(n-1) + n**2 + 5


k = 0

for n in range(1,1001):
    if all([int(x)%2==0 for x in str(f(n))]):
        k += 1

print(k)
