x = 3 * 16**8 - 4**5 + 3

a = []
while x > 0:
    a = [x % 4] + a
    x = x // 4
print(a.count(3))
# 12