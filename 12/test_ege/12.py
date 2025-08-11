# https://education.yandex.ru/ege/task/c8945b8a-2276-4dea-8a6d-a86b6cb1171d
def func(n):
    while "63" in n or "69" in n or "93" in n:
        if "63" in n:
            n = n.replace("63", "36", 1)
        if "69" in n:
            n = n.replace("69", "96", 1)
        if "93" in n:
            n = n.replace("93", "39", 1)
    return n


a = func("3" * 50 + "6" * 50 + "9" * 50)
print(a[41] + a[99] + a[143])
