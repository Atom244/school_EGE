k = 0
for x in range(100):
    for y in range(100):
        f = not(((x > 6) and (x +y >= 5)) or (y >= 5))
        if f:
            k += 1
print(k)
