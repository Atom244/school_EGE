def func(n):
    while ">1" in n or ">2" in n or ">3" in n:
        if ">1" in n:
            n = n.replace(">1", "22>", 1)
        if ">2" in n:
            n = n.replace(">2", "2>", 1)
        if ">3" in n:
            n = n.replace(">3", "1>", 1)

    return n

print(func(">" + "1" * 11 + "2" * 12 + "3" * 30))

a = "2222222222222222222222222222222222111111111111111111111111111111"
lst = []
for j in a:
    lst.append(int(j))

print(sum(lst))