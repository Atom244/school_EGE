def g(s,m):
    if s>=125 or m<0: return m%2==0
    h = [g(s + 2, m - 1), g(s + 4, m - 1), g(s * 2, m - 1)]
    return any(h) if (m-1)%2==0 else all(h)