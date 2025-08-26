for n in range(2, 100):
    x = 68
    a = []
    while x > 0:
        a = [x % n] + a
        x = x // n
    if a[-1] == 2 and len(a) == 4:
        print(n)
# 3