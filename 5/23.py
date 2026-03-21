for n in range(2, 3000):
    sumkrat = sum([int(x) for x in str(n) if int(x)%2==0])
    sum2 = 0
    for i in range(len(str(n))):
        if (i + 1)%2==0:
            sum2 += int(str(n)[i])
    r = abs(sumkrat - sum2)
    if r == 9:
        print(n)