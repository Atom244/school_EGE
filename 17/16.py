a = [int(x) for x in open('17_2013.txt')]
ans = [x for x in a if (x%10 == 2 or x%10 == 7) and x%3==0 and x%11==0]

print(len(ans), min(ans))