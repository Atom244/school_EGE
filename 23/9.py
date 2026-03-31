# с подсчётом шагов
def f(curr, end, step):
    if curr > end: return 0

    if curr == end and step == 6: return 1
    if curr == end and step != 6: return 0

    if curr < end: return f(curr+1, end, step+1) + f(curr+2, end, step+1) + f(curr*2, end, step+1)

print(f(1,20, 0))