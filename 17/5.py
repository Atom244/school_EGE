a = [int(x) for x in open('17-5.txt')]
# 2 способ zip
ans = []
for x,y in zip(a,a[1:]):
    if abs(x)%10==5 and abs(y)%10 == 5:
        ans.append(x+y)

print(len(ans), max(ans))