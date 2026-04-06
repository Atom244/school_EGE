a = [int(x) for x in open('17_1999.txt')]
ans = []
for i in range(len(a)-2):
    troika = [a[i], a[i+1], a[i+2]]
    kret12 = [x for x in troika if x%12==0] # len>0
    del3 = [x for x in troika if x%3==0] # len 3
    if len(kret12)>0 and len(del3) == 3:
        ans.append(sum(troika)/len(troika))

print(len(ans), min(ans))