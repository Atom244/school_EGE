b = list(range(18, 52 + 1))
c = list(range(16, 41 + 1))
a = []

def f(x):
    B = x in b
    C = x in c
    A = x in a
    return (B <= A) and ((not C) or A)

for x in range(1,100):
    if f(x) == 0:
        a.append(x)
print(a)
# 52 - 16 = 36