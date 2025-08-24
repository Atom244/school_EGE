from itertools import *

k = 0

for x in permutations('ПЕСКАРЬ', 7):
    s = ''.join(x)
    if s[0] != 'Ь' and 'ЬЕ' not in s and 'ЬА' not in s and 'ЬР' not in s:
        k += 1
        print(s)
print(k)

# 2520