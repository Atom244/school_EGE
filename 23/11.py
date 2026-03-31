# Без конкретного результата
d = set()
def f(curr, step):
    if step == 4: d.add(curr)
    else:
        f(curr+1, step+1)
        f(curr+5, step+1)
        f(curr*3, step+1)

f(1,0)
print(len(d))
