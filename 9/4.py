k = 0
for i in open("4"):
    s = [int(x) for x in i.split()]
    pov2 = set([x for x in s if s.count(x) == 2])
    pov1 = [x for x in s if s.count(x) == 1]
    if len(pov2) == 3 and len(pov1) == 1 and sum(pov2)/len(pov2) >= sum(pov1):
        k += 1
print(k)