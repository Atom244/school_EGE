for w in 0,1:
    for x  in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (x == (not z)) <= ((x or w) == y)
                if int(f) == 0:
                    print(x,w,y,z,int(f))
# xwyz