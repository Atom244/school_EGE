from math import *
for n in range(1, 300):
    for m in range(1, 300):
        l1 = []
        for x in str(n):
            if int(x)%2==0 and int(x)>0:
                l1.append(int(x))
        for x in str(m):
            if int(x)%2==0 and int(x)>0:
                l1.append(int(x))

        p1 = prod(l1)

        l2 = []
        for x in str(n):
            if int(x) % 2 != 0 and int(x)>0:
                l2.append(int(x))
        for x in str(m):
            if int(x) % 2 != 0 and int(x)>0:
                l2.append(int(x))

        p2 = prod(l2)

        r = abs(p1 - p2)
        if n == 120 and r == 29:
            print(m)