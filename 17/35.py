a = [int(i) for i in open('17 (1).txt')]
k = 0
for i in range(len(a)-1):
    pair = [a[i],a[i+1]]
    if (pair[0]>0 and pair[1]>0) or (pair[0]<0 and pair[1]<0):
        k += 1
print(k)