a = [int(x) for x in open('17_1993.txt')]
ans = []

for i in range(len(a)-1):
    pair = [a[i], a[i+1]]
    if sum(pair)%3==0 and sum(pair)%6!=0 and abs(pair[0]*pair[1])%10==8:
        ans.append(sum(pair))
print(len(ans), max(ans))