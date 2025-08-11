for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = ((1 == w) == ((not ((w and x) or y)))) <= z
                if int(F) == 1:
                    print(x, z, y, w, int(F))
