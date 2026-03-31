def f(c,e,umn):
    if c > e: return 0
    if c == e: return umn <= 3
    if c < e and umn <= 3:
        return f(c+2,e,umn) + f(c*3,e,umn+1) + f(c*5,e,umn+1)
    if c < e and umn > 3:
        return f(c+2,e,umn)

print(f(2,200,0))