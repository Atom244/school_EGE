a = [int(x) for x in open('17_2401.txt')]
ans = []
k = 0
for i in range(len(a)-1):
    pair = [a[i], a[i+1]]
    abspair = [abs(x) for x in pair]
    if 50<=sum(abspair)<=200:
        k += 1
        ans.append(pair[0])
        ans.append(pair[1])
print(k, min(ans))