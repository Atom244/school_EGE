def func(n):
    while "1111" in n:
        n = n.replace("1111", "22", 1)
        n = n.replace("222", "1", 1)
    return n

print(func("1" * 98))
