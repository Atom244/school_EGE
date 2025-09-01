for w in 0,1:
    for x  in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (y <= x) or (not((x <= z) and (z <= x))) and (not w)
                if int(f) == 0:
                    print(w,z,x,y,int(f))
# wzxy