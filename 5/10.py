l = set()

for n in range(1, 80):
    b = str(bin(n)[2:])

    b = str(b + str(sum(map(int, b))%2))

    b = str(b + str(sum(map(int, b))%2))

    r = int(b,2)

    if r < 80:
        l.add(r)
        print(n,r)
print(len(l))