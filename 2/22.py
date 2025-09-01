for w in 0,1:
    for x  in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (y<= (x or z)) and (z <= y)
                if int(f) == 0:
                    print(z,w,y,x,int(f))
# zwyx