def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(799000, 800000):
    d = div(x)
    if d:
        m = min(d) + max(d)
    else:
        m = 0
    if m%10==2:
        print(x, m)