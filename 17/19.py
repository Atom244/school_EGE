a = [int(x) for x in open('17_2017.txt')]
def cc(x):
    s = ''
    alph = '0123456789abcdefgh'
    while x>0:
        s = alph[x%16] + s
        x = x // 16
    return s
ans = [x for x in a if cc(x)[-1] == 'b' and x%7==0 and x%6!=0 and x%13!=0 and x%19!=0]
print(sum(ans), len(ans))