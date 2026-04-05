def f(a,b,m):
    if a >= 78 or b >= 78: return m%2==0
    if m == 0: return 0
    if a < b: h = [f(a,b+1,m-1), f(a,b+2,m-1), f(a,b+3,m-1), f(a*2,b,m-1)]
    if a > b: h = [f(a+1,b,m-1), f(a+2,b,m-1),f(a+3,b,m-1),f(a,b*2,m-1)]
    if a == b: h = [f(a+1,b,m-1), f(a+2,b,m-1),f(a+3,b,m-1)]
    return any(h) if m%2 != 0 else all(h)
print(19, min([a+b for a in range(1,78) for b in range(1,78) if f(a,b,1)]))
print(20, [s for s in range(1,78) if not f(25,s,1) and f(25,s,3)])
print(21, [s for s in range(1,78) if not f(69,s,2) and f(69,s,4)])
