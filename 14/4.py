x = 64**30 + 2**300 - 4

a = []
while x > 0:
    a = [x % 8] + a
    x = x // 8
print(a.count(7))
# 59


'''x = 64**30 + 2**300 - 4
print(oct(x)[2:].count('7'))'''