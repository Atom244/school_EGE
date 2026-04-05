def f(s,m, hod):
    if s >= 140: return m%2 == 0
    if m == 0: return 0
    if hod == '+1':
        h = [f(s + 2, m-1, '+2'), f(s * 3, m-1, '*3')]
    elif hod == '+2':
        h = [f(s + 1, m-1, '+1'), f(s * 3, m-1, '*3')]
    elif hod == '*3':
        h = [f(s + 2, m-1, '+2'), f(s + 1, m-1, '+1')]
    else:
        h = [f(s + 2, m-1, '+2'), f(s * 3, m-1, '*3'), f(s + 1, m-1, '+1')]
    return any(h) if (m-1)%2==0 else all(h)

print(19,[s for s in range(1,140) if not f(s,1,'') and f(s,2,'')])
print(20,[s for s in range(1,140) if not f(s,1,'') and f(s,3,'')])
print(21,[s for s in range(1,140) if (f(s,2,'') or f(s,4,'')) and not f(s,2,'')])
