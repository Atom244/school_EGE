x = 5 * 216**1156 - 4*36**1147 + 6**1153 - 875
a = []
while x > 0:
    a = [x % 6] + a
    x = x // 6
print(a.count(5) - a.count(0))
# 1182