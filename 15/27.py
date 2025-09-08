d = [i for i in range(17, 58 + 1)]
c = [i for i in range(29, 80 + 1)]
a = []

def f(x):
    A = x in a
    D = x in d
    C = x in c
    return D <= (((not C) and (not A)) <= (not D))
for x in range(1000):
    if f(x) == False:
        a.append(x)
print(a)
# https://youtu.be/zLkpHr-al4I?si=6t1plImnB4xEWrdO&t=2480
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 17 - 29
# ответ: 12