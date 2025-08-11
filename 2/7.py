print("x y F [1]")
for x in range(2):
    for y in range(2):
        F = 1 - x or y
        print(x, y, int(F))
print("")

print("x y F [2]")
for x in range(2):
    for y in range(2):
        F = 2 - x and y
        print(x, y, int(F))
print("")

print("x y F [3]")
for x in range(2):
    for y in range(2):
        F = 3 - x <= y
        print(x, y, int(F))
print("")

print("x y F [4]")
for x in range(2):
    for y in range(2):
        F = 4 - x == y
        print(x, y, int(F))
print("")

# неверная задача (опечатки?)
# https://education.yandex.ru/ege/task/eea60fac-53a5-42e6-9719-42a48d79e286