for y in range(0, 17):
    for x in range(0, 15):
        a = 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
        b = 6 * 17 ** 3 + 7 * 17 ** 2 + y * 17 + 9
        if (a + b) % 131 == 0:
            print(x, y, (a + b) // 131)

for y in "0123456789abcde":
    for x in "0123456789abcdefg":
        try:
            a = int(f"123{x}5", 15)
            b = int(f"67{y}9", 17)
            if (a + b) % 131 == 0:
                print(x, y, (a + b) // 131)
        except:
            pass

#686
