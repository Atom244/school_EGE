def f(c, e, plus=0, mul=0):
    if c > e:
        return 0
    if c == e:
        return 1

    if plus < 2 and mul < 2:
        return f(c+1, e, plus + 1, 0) + f(c * 2,e,0,mul + 1)

    if plus < 2:
        return f(c + 1, e, plus + 1, 0)

    if mul < 2:
        return f(c * 2, e, 0, mul + 1)

print(f(1, 16))