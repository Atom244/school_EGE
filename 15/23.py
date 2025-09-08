
a = set()
p = {1,3,5,7,9,11}
q = {3,6,9,12}

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (P <= (not Q)) or A

for x in range(1,100):
    if f(x) == 0:
        a.add(x)
print(a)
# 12
