for w in 0,1:
    for x  in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (x <= y) or (not (w <= z))
                if int(f) == 0:
                    print(z,y,w,x,int(f))
# zywx