p = list(range(17, 54 + 1))
q = list(range(37, 83 + 1))
a = []

def f(x):
    P = x in p
    Q = x in q
    A = x in a
    return P <= ((Q and (not A)) <= (not P))

for x in range(1,100):
    if f(x) == 0:
        a.append(x)
print(a)
# 54 - 37 = 17