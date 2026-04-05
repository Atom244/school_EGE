# по выполненному числу ходов
def g(s, p):
    if s >= 125 or p>2: return p==2
    h = [g(s+2,p+1), g(s+4,p+1), g(s*2,p+1)]
    return any(h) if (p+1)%2==0 else all(h)

print(19, [s for s in range(1,125) if g(s,0)])

def g(s, p):
    if s >= 125 or p>3: return p==3
    h = [g(s+2,p+1), g(s+4,p+1), g(s*2,p+1)]
    return all(h) if (p+1)%2==0 else any(h)

print(20, [s for s in range(1,125) if g(s,0)])

def g(s, p):
    if s >= 125 or p>4: return p==4 or p==2
    h = [g(s+2,p+1), g(s+4,p+1), g(s*2,p+1)]
    return any(h) if (p+1)%2==0 else all(h)

print(21, [s for s in range(1,125) if g(s,0)])