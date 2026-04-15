def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i == 0:
            d.append(i)
            x = x // i
        i += 1
    if x > 1: d.append(x)
    return d
for x in range(9_876_543_20, 9_876_000_00, -1):
    d = fact(x)
    if '1' in str(sum(d)) and len(d) == 13:
        print(x, max(d))