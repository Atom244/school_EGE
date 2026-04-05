def f(s,m,p1,p2):
    if s >= 121: return m%2==0
    if m == 0: return 0
    h = []
    if p2 != '+2': h += [f(s+2,m-1,'+2', p1)]
    if p2 != '+5': h += [f(s+5, m-1, '+5', p1)]
    if p2 != '+12': h += [f(s+12,m-1,'+12', p1)]
    if p2 != '*2': h += [f(s*2,m-1,'*2', p1)]
    return any(h) if m%2!=0 else all(h)

print(19, [s for s in range(1,121) if f(s,2,'','')]) # all->any
print(20, [s for s in range(1,121) if not f(s,1,'','') and f(s,3,'','')])
print(19, [s for s in range(1,121) if not f(s,4,'','') and f(s,6,'','')])
