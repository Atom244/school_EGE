a = [int(x) for x in open('17-407.txt')]
kolvokrat32 = len([x for x in a if x%32 == 0])
ans = []
for i in range(len(a)-1):
    pair = [a[i], a[i+1]]
    if (pair[0]<0 or pair[1]<0) and sum(pair)<kolvokrat32:
        ans.append(sum(pair))

print(len(ans), max(ans))



