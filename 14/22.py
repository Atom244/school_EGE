def convert(x, cc):
    a = []
    while x > 0:
        a = [x % cc] + a
        x = x // cc
    return a
k = 0
for n in range(1, 1000):
    if len(convert(n, 5)) <= 4 and len(convert(n, 2)) >= 5 and n%16 == 13:
        k += 1
print(k)
# 38