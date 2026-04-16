from fnmatch import fnmatch

for x in range(0,10**10,1917):
    if fnmatch(str(x),'3?12?14*5'):
        print(x, x//1917)