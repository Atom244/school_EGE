# DYNAMIC SOLUTION (не проходя через n)

a = [0]*100
a[2] = 1
for i in range(2, 16):
    if i == 4: # !!!
        a[i] = 0
    if i+1 <= 16:
        a[i+1] += a[i]
    if i*2 <= 16:
        a[i*2] += a[i]

print(a[16])