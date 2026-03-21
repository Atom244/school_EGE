def g(s):
    if s >= 82:
        return "WIN"
    if g(s*3) == "WIN" or g(s+4) == "WIN" or g(s+1) == "WIN" :
        return "p1"
    if g(s*3) == "p1" and g(s+4) == "p1" and g(s+1) == "p1":
        return "v1"
    if g(s*3) == "v1" or g(s+4) == "v1" or g(s+1) == "v1":
        return "p2"
for s in range(9,83):
    print(s, g(s))
