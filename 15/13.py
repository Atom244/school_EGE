def f(x):
    return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)) == 1:
        print(a)
# 7
