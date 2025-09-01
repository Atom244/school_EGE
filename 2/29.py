for w in 0,1:
    for x  in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (not (z and (not w)) or ((z <= w) == (x <= y)))
                if int(f) == 0:
                    print(z,x,w,y,int(f))
# zxwy