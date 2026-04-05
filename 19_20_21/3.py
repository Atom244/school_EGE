from functools import lru_cache

@lru_cache(None)
def f(s,x,yach,m):
    if yach > 25 or m < 0: return 0
    if s == x: return m%2==0
    steps = [f(s+1,x,yach+1,m-1), f(s+2,x,yach+1,m-1), f(s+3,x,yach+1,m-1), f(s+4,x,yach+1,m-1)]
    if m%2 != 0:
        return any(steps)
    if m%2 == 0:
        return all(steps)


exp_x = set()
for expected_x in range(5,25+1):
    for step in range(1,26,2):
        if f(0,expected_x,0,step):
            exp_x.add(expected_x)

print(len(exp_x))

exp_x = []
for expected_x in range(5,25+1):
    if not(f(0,expected_x,0,1)) and f(0,expected_x,0,4):
        exp_x.append(expected_x)

print(exp_x)

exp_x = []
for expected_x in range(5,25+1):
    if not(f(0,expected_x,0,2) or f(0,expected_x,0,4)) and f(0,expected_x,0,6):
        exp_x.append(expected_x)

print(exp_x)