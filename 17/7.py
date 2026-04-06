a = [int(x) for x in open('17-243.txt')]
mx = max([x for x in a if x%71==0])
ans = []
for x,y in zip(a,a[1:]):
    if x < mx and y < mx and (x%13==0 or y%13==0):
        ans.append(x+y)
print(len(ans), min(ans))