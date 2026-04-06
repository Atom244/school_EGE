a = [int(x) for x in open('17_2002.txt')]
# 4>3>2>1
ans = []
for i in range(len(a)-3):
    x,y,z,w = a[i],a[i+1],a[i+2],a[i+3]
    if x>y>z>w and max([x,y,z,w])-min([x,y,z,w]) > 1000:
        ans.append(sum([x,y,z,w]))
print(len(ans), min(ans))