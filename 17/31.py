a = [int(x) for x in open('17_2310.txt')]
s = [x for x in a if x%10==4]
sm = min(s)+max(s)
ans = []
for i in range(len(a)-1):
    pair = [a[i], a[i+1]]
    if sum(pair)<sm:
        ans.append(sum(pair))
print(len(ans), max(ans))