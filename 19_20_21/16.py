def f(a,b,m):
    if a == 0 or b == 0: return m%2 == 0
    h = []
    if a>=3 and b>=3: h += [f(a-3,b-3,m-1)]
    if a%2==0: h+=[f(a//2,a//2,m-1)]
    if b%2==0: h+=[f(b//2,b//2,m-1)]
    if len(h) == 0: return m%2==0
    if m == 0: return 0
    return any(h) if m%2!=0 else all(h)

print(19,[k for k in range(1,100) if f(32,k,2)]) # all->any
print(20, [k for k in range(1,100) if not f(32,k,1) and f(32,k,3)])
print(21, [k for k in range(1,100) if not f(20,k,2) and f(20,k,4)])