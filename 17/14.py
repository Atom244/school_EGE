a = [int(x) for x in open('17-433.txt')]
ans = []
m = min([x for x in a if abs(x)%100==15 and len(str(abs(x))) == 3])
for i in range(len(a)-2):
    troika = [a[i],a[i+1],a[i+2]]
    plus = [x for x in troika if x > 0]
    minus = [x for x in troika if x < 0]
    if (len(plus) == 3 or len(minus) == 3) and min(troika)*max(troika) > m**2:
        ans.append(min(troika)*max(troika))
print(len(ans), min(ans))