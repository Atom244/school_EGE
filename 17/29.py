a = [int(x) for x in open('17_2239.txt')]
mx = max([x for x in a if x%19==0])
ans = []

for i in range(len(a)-1):
    pair = [a[i], a[i+1]]
    bolshe = [x for x in pair if x > mx]
    if len(bolshe)>0:
        ans.append(sum(pair))
print(len(ans), min(ans))