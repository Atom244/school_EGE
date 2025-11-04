f = open('160.txt')
k = 0
for s in f:
    l = sorted([int(x) for x in s.split()])
    if l[3] < l[0] + l[1] + l[2] and l[0] + l[3] == l[1] + l[2]:
        k += 1

print(k)