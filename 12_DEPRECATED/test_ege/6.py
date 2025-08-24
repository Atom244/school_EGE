def func(n):
    while "00" not in n:
        n = n.replace("011", "20", 1)
        n = n.replace("022", "10", 1)
        n = n.replace("01", "220", 1)
        n = n.replace("02", "110", 1)

    return n


for two in range(1, 10000):
    stroke = func("0" + "1"*two + "2"*two +"0")
    if stroke.count("1") == 47 and stroke.count("2") < 70:
        print(two)

# NO