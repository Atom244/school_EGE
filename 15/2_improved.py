for a in range(1, 100):
    for x in range(1, 100000):
        f =((x%34 == 0) and (x%51 != 0)) <= ((x%a != 0) or (x%51 == 0))
        if int(f) == 0:
            break
    else:
        print(a)
# 3