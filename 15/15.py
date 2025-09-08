def f(x):
    return ((x&26 != 0) or (x & 13 != 0)) <= ((x & 29 ==0) <= (x & a != 0))

for a in range(1,100):
    if all(f(x) for x in range(1,100000)) == 1:
        print(a)
# 2
