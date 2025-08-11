
def func(n):
    while "52" in n or "1122" in n or "2222" in n:
        if "52" in n:
            n = n.replace("52", "1", 1)
        if "2222" in n:
            n = n.replace("2222", "5", 1)
        if "1122" in n:
            n = n.replace("1122", "25", 1)

    return n


for i in range(4, 10001):
    s = func("5" + "2" * i)
    if s.count("5") * 5 + s.count("2") * 2 + s.count("1") == 88:
        print(i)



