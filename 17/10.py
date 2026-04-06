a = [int(x) for x in open('17-3.txt')]
# тройки
ans = []
for x,y,z in zip(a,a[1:], a[2:]):
    if x*y*z%7==0 and abs(x+y+z)%10 == 0:
        ans.append(x+y+z)
print(len(ans), max(ans))
