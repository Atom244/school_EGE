for x in range(0, 17):
    a = 9 * 17**4 + 7 * 17 **3 + 5* 17**2 + 9*17 + x
    b = 3 * 17 **4 + x * 17 **3 + 17**2 + 8
    if (a + b) % 11 == 0:
        print(x, (a+b)//11)
# 95306

for x in "01234567890abcdefgh":
    try:
        a = int(f"9759{x}", 17)
        b = int(f"3{x}108", 17)
        if (a + b) % 11 == 0:
            print(x, (a+b)//11)
    except:
        pass