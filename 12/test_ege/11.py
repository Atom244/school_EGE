# https://education.yandex.ru/ege/task/a8fd6036-c7b3-42b5-870c-d3f3eb6335bd
def func(n):
    while "23" in n or "12" in n or "32" in n:
        if "12" in n:
            n = n.replace("12", "21", 1)
        if "32" in n:
            n = n.replace("32", "1", 1)
        if "23" in n:
            n = n.replace("23", "2", 1)
    return n

for i in range(1, 10000):
    a = func("1" * 40 + "2" * 40 + "3" * i)
    print(sum(map(int, str(a))))
    if sum(map(int, str(a))) == 100:
        print(i)
