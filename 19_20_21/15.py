def f(s,m,p):
    if s >= 20: return m%2 == 0
    if m == 0: return 0
    h = [f(s+2,m-1,p), f(s*2,m-1,p)]
    if p!=1: h += [f(s,m-1,1)]
    return any(h) if m%2 !=0 else all(h)
print(19,[s for s in range(1,20) if f(s,2,0)]) # all->any
print(19,[s for s in range(1,20) if not f(s,1,0) and f(s,3,0)])
print(19,[s for s in range(1,20) for m in range(1,100) if m%2==0 and f(s,m,0)]) # или f(s,20,0) автоматический просмтор побед вани

