def g(s,p,end):
    if s>=125 or p>end: return p%2==end%2
    h = [g(s + 2, p + 1, end), g(s + 4, p + 1, end), g(s * 2, p + 1, end)]
    return any(h) if (p+1)%2 == end%2 else all(h)

print(19,[s for s in range(1,125) if g(s,0,2)])
print(20,[s for s in range(1,125) if g(s,0,3)])
print(21,[s for s in range(1,125) if g(s,0,4)])