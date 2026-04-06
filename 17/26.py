from math import *

a = [int(x) for x in open('17_2400.txt')]
ans = []

for i in range(len(a)-1):
    pair = [a[i],a[i+1]]
    negative = [x for x in pair if x < 0]
    if len(negative)>0 and sum(pair)>=100:
        ans.append(prod(pair))

print(len(ans), max(ans))