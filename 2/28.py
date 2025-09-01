for a in 0,1:
    for b  in 0,1:
        for c in 0,1:
            for d in 0,1:
                f = ((a and b) == (not c)) and (b <= d)
                if int(f) == 1:
                    print(c,a,d,b,int(f))
# cadb