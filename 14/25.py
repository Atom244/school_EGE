for x in range(0, 11):
    a = 3*11**4 + 3*11**3 + 6*11**2 + 4*11 + x
    b = x*12**4 + 7*12**3 + 9*12**2 + 4*12 + 6
    c = 5*14**4 + 5*14**3 + x*14**2 + 8*14 + 7
    if a + b == c:
        print(x, c)

for x in "0123456789a":
    try:
        a = int(f"3364{x}", 11)
        b = int(f"{x}7946", 12)
        c = int(f"55{x}87", 14)
        if a + b == c:
            print(x, c)
    except:
        pass