for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = not(x == (y <= z))

            print(y,x,z,int(f))
# ywxz