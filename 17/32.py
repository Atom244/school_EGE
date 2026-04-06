a = [int(x) for x in open('17_2403.txt')]
def cc(x):
    x = abs(x)
    s = ''
    while x>0:
        s = str(x%8)+s
        x = x // 8
    return s

ans = []

for i in range(len(a)-1):
    pair = [a[i], a[i+1]]
    del9 = [x for x in pair if x%9==0] # len 1
    ok3nedel = [x for x in pair if x%9!=0 and cc(x)[-1]=='3']
    if len(del9) == 1 and len(ok3nedel) == 1:
        ans.append(max(pair))

print(len(ans), max(ans))