def convert(x, n):
    a = []
    while x > 0:
        a = [x % n] + a
        x = x // n
    return a

print(convert(2*27**7 + 3**10 - 9, 3).count(0))
# 13