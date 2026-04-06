a = [int(x) for x in open('17_2003.txt')]
ans = []
for x in a:
    if x%3==0 and x%7!=0 and x%17!=0 and x%19!=0 and x%27!=0:
        ans.append(x)
print(len(ans), max(ans))