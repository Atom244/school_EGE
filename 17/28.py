a = [int(x) for x in open('17_2238.txt')]
avg = sum(a)/len(a)
ans = []
for i in range(len(a)-2):
    troika = [a[i],a[i+1],a[i+2]]
    bolsheavg = [x for x in troika if x>avg]
    if len(bolsheavg)>=2:
        ans.append(sum(troika))
print(len(ans), max(ans))