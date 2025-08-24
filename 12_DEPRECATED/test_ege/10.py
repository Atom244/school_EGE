# https://education.yandex.ru/ege/task/b00a1ede-851c-48c8-841e-510e7bf2fb4b
def func(n):
    while "47" in n or "49" in n or "97" in n:
        if "47" in n:
            n = n.replace("47", "74", 1)
        if "49" in n:
            n = n.replace("49", "94", 1)
        if "97" in n:
            n = n.replace("97", "79", 1)
    return n


a = func("4" * 40 + "7" * 40 + "9" * 40)
print(a[24] + a[72] + a[104])
