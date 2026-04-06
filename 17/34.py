a = [int(x) for x in open('17_2399.txt')]
ans = []
def cc(x):
    s = ''
    alph = '0123456789abcdefgh'
    while x > 0:
        s = alph[x%16] + s
        x = x // 16
    return s
sm = sum(int(d) for x in a if x % 35 == 0 for d in str(x))

for i in range(len(a)-1):
    pair = [a[i],a[i+1]]
    bolshesm = [x for x in pair if x > sm]
    if len(bolshesm) == 1 and ((pair[0]>sm and cc(pair[1])[-2:]=='ef') or (pair[1]>sm and cc(pair[0])[-2:]=='ef')):
        ans.append(sum(pair))
print(len(ans), min(ans))