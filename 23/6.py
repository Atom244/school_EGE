# DYNAMIC SOLUTION (проходя через n)

a = [0]*100
a[2] = 1

for i in range(2, 8):
    if i+1 <= 8:
        a[i+1] += a[i]
    if i*2 <= 8:
        a[i*2] += a[i]

for i in range(8, 20):
    if i+1 <= 20:
        a[i+1] += a[i]
    if i*2 <= 20:
        a[i*2] += a[i]

print(a[20])