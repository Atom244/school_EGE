x = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
a = []
while x > 0:
    a = [x % 12] + a
    x = x // 12
print(a.count(11))
# 51
