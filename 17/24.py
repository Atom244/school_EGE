a = [int(x) for x in open('17_2402.txt')]
def cc(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x = x // 3
    return s
ans = []

for i in range(len(a)-2):
    troika = [a[i],a[i+1],a[i+2]]
    ok2 = [x for x in troika if int(cc(x))%10==2]
    if len(ok2)>0:
        ans.append(min(troika))

print(len(ans), sum(ans))