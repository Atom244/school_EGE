def find_2s(x):
    lst = []
    k = 0
    for i in range(1, len(str(x))):
        num = str(n)[k] + str(n)[i]
        lst.append(int(num))
        k += 1
    return lst


for n in range(10, 3000):
    l = find_2s(n)
    r = max(l) - min(l)
    if r == 44:
        print(n)
