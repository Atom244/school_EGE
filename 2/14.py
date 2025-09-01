for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (x or (not y)) and (not(y == z)) and w
                if int(f) == 1:
                    print(x,w,z,y,int(f))
# xwzy