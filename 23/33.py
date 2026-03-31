def f(c,e,k):
    if c > e or k > 7: return 0
    if c == e: return k == 7
    return f(c+1,e,k+1) + f(c+4,e,k+1) + f(c*2,e,k+1)

print(f(3,27,0))