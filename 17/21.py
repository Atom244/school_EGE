from math import *
a = [int(x) for x in open('17_1994.txt')]
ans = []
for i in range(len(a)-1):
    pair = [a[i],a[i+1]]
    if prod(pair)>0 and sum(pair)%7==0:
        ans.append(prod(pair))
print(len(ans), min(ans))