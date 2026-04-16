from fnmatch import fnmatch

for x in range(0,10**10,7993):
    if fnmatch(str(x),'4*4736*1'):
        print(x, x//7993)