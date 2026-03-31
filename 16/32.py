from functools import lru_cache
from fractions import Fraction
from math import *

@lru_cache(None)
def f(n):
    if n >= 5000:
        return factorial(n) # Fraction(n)
    if 1<=n<5000:
        return 2*f(n+1)//(n+1) # можно оставить / с Fraction
for i in range(5000, 1, -1):
    f(i)
print(1000*f(7)/f(4))