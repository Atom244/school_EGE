for x in range(1, 100):
    t = 36 ** 17 - 6 ** x + 71
    a = []
    while t > 0:
        a = [t % 6] + a
        t = t // 6
    if sum(a) == 61:
        print(x)
# 24