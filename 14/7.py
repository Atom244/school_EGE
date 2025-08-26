def convert(x, n):
    a = []
    while x > 0:
        a = [x % n] + a
        x = x // n
    return a

print(sum(convert(51*7**12 - 7**3 - 22, 7)))
# 70