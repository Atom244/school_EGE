a = set()
p = {3,6,9,12}
q = {1,2,3,4,5,6}

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (not((not A) and P)) or (not Q)

for x in range(1, 1000):
    if f(x) == 0:
        a.add(x)
print(a)
# 2
