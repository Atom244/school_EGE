k = 0

for s in open('10910.txt'):
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x) > 1 and x != a[0]]
    if a.count(a[0]) == 1 and len(a1) > 0 and a[0] + a[5] < sum(a1):
        k += 1

print(k)