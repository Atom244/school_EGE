def func(n):
    while "4444" in n or "844" in n or "84" in n:
        if "4444" in n:
            n = n.replace("4444", "884", 1)
        if "844" in n:
            n = n.replace("844", "488", 1)
        if "84" in n:
            n = n.replace("84", "3343", 1)
    return n

counter = 0
for N in range(4, 40):
    generated_word = func("8" + "4" * N)
    print(N, len(generated_word))

