for x in range(21, 30):
    a = []
    t = x
    while x > 0:
        a = [x % 3] + a
        x = x // 3
    if a[-2] == 1 and a[-1] == 1:
        print(t, a)
# 22