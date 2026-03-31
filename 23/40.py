def f(c,e,chet):
    if c > e: return 0
    if c == e: return chet == 6
    return f(c+1,e,chet + 1 if (c+1)%2==0 else chet) + f(c+3,e,chet + 1 if (c+3)%2==0 else chet) + f(c+5,e,chet + 1 if (c+5)%2==0 else chet)

print(f(3,25,0))