def f(c,e,k):
    if c > e or k > 2: return 0
    if c == e and k <= 2: return 1
    if c < e: return f(c+1,e,k)+f(c*2,e,k+1)+f(c*3,e,k+1)

print(f(1,100,0))