a = [int(x) for x in open('17-4.txt')]
avg = sum(a)/len(a)
ans = []
for x,y in zip(a,a[1:]):
    if x < avg and y < avg and (x+y)%100 == 19:
        ans.append(x+y)

print(len(ans), min(ans))