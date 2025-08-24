from itertools import *

k = 0
for x in permutations('КОЛУН'):
    s = ''.join(x)
    s = s.replace('Л', 'К').replace('Н', "К").replace("У", "О")
    if 'КК' not in s and 'ОО' not in s:
        k += 1
        print(s)
print(k)

# 12
# https://vkvideo.ru/video-205865487_456239692?t=49m43s