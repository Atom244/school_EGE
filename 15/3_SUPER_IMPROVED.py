def f(x):
    return ((x%84 != 0) or (x%90 != 0)) <= (x%a != 0)

for a in range(1,10000):
    if all(f(x) == 1 for x in range(1,10000)):
        print(a)
'''
ПОИСК ЧИСЛА ПОД УСЛОВИЕ
'''
# 1260
