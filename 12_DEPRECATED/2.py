def func(n):
    while "44" in n or "9299" in n or "49" in n:
        if "49" in n:
            n = n.replace("49", "944")
        if "44" in n:
            n = n.replace("44", "2")
        if "9299" in n:
            n = n.replace("9299", "4")
    return n

tup = []

for i in range(3, 1001):

    tup.append(func(f"4{'9'*i}"))
print(len(set(tup)))