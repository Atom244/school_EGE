for x in range(1, 100):
    t = 81**20 - 9**x + 50
    a = []
    while t > 0:
        a = [t % 9] + a
        t = t // 9

    if sum(a) == 138:
        print(x)
# 24