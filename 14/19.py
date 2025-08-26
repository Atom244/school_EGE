for x in range(1, 40):
    a = []
    t = x
    while x > 0:
        a = [x % 2] + a
        x = x // 2
    if len(a) >=4 and a[-4:] == [1,0,1,1]:
        print(t)
# 27

'''for x in range(1, 40):
    t = bin(x)[2:]
    if t[-4:] == "1011":
        print(x)'''
