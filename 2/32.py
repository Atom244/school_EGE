for w in 0,1:
    for x  in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (x and z) or ((w <= x) == (z <= y))
                if int(f) == 0:
                    print(x,z,y,w,int(f))
# xzyw