a = [int(x) for x in open('17_2398.txt')]
ans = []
for i in range(len(a)-2):
    troika = [a[i],a[i+1],a[i+2]]
    ok9 = [x for x in troika if abs(x)%10==9 and x > 0]
    if abs(troika[1])%10==9 and troika[1]>0 and len(ok9)==1:
        ans.append(sum(troika))
print(len(ans), max(ans))