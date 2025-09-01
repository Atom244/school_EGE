for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            f = (a and (not c)) or ((not b) and (not c))
            if int(f) == 0:
                print(a,b,c,int(f))
# abc