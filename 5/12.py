l = []

for n in range(1, 1000):
    b = str(bin(n)[2:])
    if n%2==0:
        b = '1' + b + '0'
    else:
        b = '11' + b + '11'
    r = int(b, 2)
    if r > 52:
        l.append(r)
print(min(l))