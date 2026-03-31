def f(c,e,a,m):
    if c > e: return 0
    if c == e: return m>a
    if c < e:
        return f(c+1,e,a+1,m) + f(c*2,e,a,m+1) + f(c*3, e, a, m+1)

print(f(1,157,0,0))