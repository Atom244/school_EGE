a = [int(x) for x in open('17_2016.txt')]
ans = [x for x in a if x%13==7 and x%7!=0 and x%11!=0]
print(max(ans)-min(ans), len(ans))
