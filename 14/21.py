def convert(x, cc):
    a = []
    while x > 0:
        a = [x % cc] + a
        x = x // cc
    return a

for n in range(1, 100):
    if len(convert(n, 6)) == 2 and len(convert(n, 5)) == 3 and convert(n, 11)[-1] == 1:
        print(n)
# 34