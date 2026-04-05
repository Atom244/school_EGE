def moves(s):
    return s+2, s+4, s*2

def w(s):
    return s >= 125

def p1(s):
    return not w(s) and any(w(i) for i in moves(s))

def v1(s):
    return not p1(s) and all(p1(i) for i in moves(s))

def p2(s):
    return any(v1(i) for i in moves(s))

def v2(s):
    return not v1(s) and not p1(s) and all(p1(i) or p2(i) for i in moves(s))

print('p1',[s for s in range(1,125) if p1(s)])
print('v1',[s for s in range(1,125) if v1(s)])
print('p2',[s for s in range(1,125) if p2(s)])
print('v2',[s for s in range(1,125) if v2(s)])
