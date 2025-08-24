from itertools import *

k = 0
for x in set(permutations("АССАСИН")):
    s = ''.join(x)
    print(s)
    k += 1
print(k)
# 420
# https://vkvideo.ru/video-205865487_456239692?t=1h5m22s