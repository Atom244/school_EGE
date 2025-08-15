from math import *

lst = []

for dop in range(1, 1000):
    alph = 10 + 999
    char = ceil(log2(alph))
    idd = ceil(char*745/8)

    if (idd + dop)*312 <= 311 * 2**10:
        lst+=[dop]

print(max(lst) * 312) #!!!!!!!!!!!!!!! ВНИМАТЕЛЬНО НА ПЕРЕФОРМУЛИРОВКЕ ЗАДАЧИ!!!!!!!!!!!
# ДОП ИНФА !ВСЕХ! ПОЛЬЗОВАТЕЛЕЙ
# 27456