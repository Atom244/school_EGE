def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i==0:
            d.append(i)
            x = x // i
        i += 1
    if x>1: d.append(x)
    return d
def cc(x):
    alph = '0123456789abcdefgh'
    s = ''
    while x>0:
        s = alph[x%18] + s
        x = x // 18
    return s

for x in range(20_581_104+1,21_000_000):
    d = fact(x)
    if 2<=len(d)<=8:
        if all('e' in cc(n) for n in d):
            print(x, sum(d)/len(d))
