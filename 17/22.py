from math import *

a = [int(x) for x in open('17_1998.txt')]
ans = []

for i in range(len(a)-2):
    troika = [a[i], a[i+1], a[i+2]]
    if prod(troika)%7==0 and abs(sum(troika))%10==5:
        ans.append(sum(troika))
print(len(ans), max(ans))