k = 0
def f(n):
    global k
    # print('*')
    k += 1
    if n >=1:
        # print('*')
        k += 1
        f(n-1)
        f(n-3)
        # print('*')
        k += 1

f(40)
print(k)