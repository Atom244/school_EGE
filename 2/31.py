for w in 0,1:
    for x  in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = ((z <= x) and (x <= w)) or (y == (z or x))
                if int(f) == 0:
                    print(y,x,w,z,int(f))
# yxwz