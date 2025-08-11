def func(n):
    while "111" in n:
        n = n.replace("111", "2", 1)
        n = n.replace("222", "1", 1)
    return n


print(func("1" * 45 + "2" * 45))
# 12