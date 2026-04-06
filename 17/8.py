a = [int(x) for x in open('17-282.txt')]

m = min([x for x in a if x%17==0])
ans = []
for x,y in zip(a,a[1:]):
    if x%m == 0 or y%m == 0:
        ans.append(x+y)
print(len(ans), max(ans))