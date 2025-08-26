for x in range(1, 1000):
    t = 125**200 - 5**x + 74
    a = []
    while t > 0:
        a = [t % 5] + a
        t = t // 5
    if a.count(4) == 100:
        print(x)
# 502