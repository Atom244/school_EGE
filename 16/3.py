# https://education.yandex.ru/ege/task/d638827d-c02a-4b33-b88d-9fc318527d1c SIMPLE THAN EGE
def F(n):
    if n < 3:
        return 1
    elif n >= 3 and n % 2 == 0:
        return F(n // 2) + 1
    elif n >= 3 and n % 2 != 0:
        return F(n - 3) + F(n - 1)

print(F(18))