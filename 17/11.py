a = [int(x) for x in open('17-380.txt')]
ans = []
max_25 = max([x for x in a if abs(x)%100==25])
for i in range(len(a)-2):
    pair = [a[i],a[i+1],a[i+2]]
    znak4 = [x for x in pair if len(str(abs(x))) == 4]
    if len(znak4) <= 2 and sum(pair) <= max_25:
        ans.append(sum(pair))
print(len(ans), max(ans))
