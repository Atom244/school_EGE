def f(c,e,umn):
    if c > e or umn > 1: return 0
    if c == e and umn == 1: return 1
    if umn == 1:
        return f(c+1,e,umn) + f(c+2,e,umn)
    return f(c+1,e,umn) + f(c+2,e,umn) + f(c*2,e,umn+1)

print(f(2,12, 0))