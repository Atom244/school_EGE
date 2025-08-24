def func(n):
    while "333" in n or "999" in n:
        if "333" in n:
            n = n.replace("333", "9", 1)
        else:
            n = n.replace("999", "3", 1)

    return n

print(func("9" * 127))