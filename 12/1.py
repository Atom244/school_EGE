def func(n):
    while "11111" in n or "888" in n:
        if "11111" in n:
            n = n.replace("11111", "88")
        else:
            n = n.replace("888", "8")
    return n


print(func("1" * 81))
