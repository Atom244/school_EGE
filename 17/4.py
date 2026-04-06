from math import *
a = [int(x) for x in open('17-3.txt')]
ans_prod = []
for i in range(len(a)-1): # -1, чтобы не было list out of range
    pair = [a[i], a[i+1]]
    if prod(pair)>0 and sum(pair)%7==0:
        ans_prod.append(prod(pair))

print(len(ans_prod), min(ans_prod))
