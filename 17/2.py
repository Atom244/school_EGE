a = [int(x) for x in open('17-4.txt')]
ans = [x for x in a if (x%10 == 5 or x%10 == 7) and x%9!=0 and x%11!=0]
print(len(ans), min(ans) + max(ans))