k = 0
for n in range(300, 401):
    d = [x for x in str(n)]
    a = [d[0] + d[1], d[0] + d[2], d[1] + d[0], d[1] + d[2], d[2] + d[0], d[2] + d[1]]
    b = [int(x) for x in a if x[0] != '0']
    r = max(b) - min(b)
    if r == 20:
        k += 1
print(k)