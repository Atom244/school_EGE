a = [int(x) for x in open('17-426.txt')]
ans = []

mx = max([x for x in a if len(str(abs(x))) == 5 and abs(x)%100==43])

for i in range(len(a)-2):
    troika = [a[i], a[i+1], a[i+2]]
    znak543 = [x for x in troika if len(str(abs(x))) == 5 and abs(x)%100==43]
    kvadraty = [x**2 for x in troika]
    if len(znak543) > 0 and sum(kvadraty) <= mx**2:
        ans.append(sum(kvadraty))
print(len(ans), min(ans))