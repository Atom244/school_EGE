from itertools import *

k = 0
for x in product('01234567', repeat = 4):
    s = ''.join(x)
    if s[0] in '246' and s[0]>=s[1]>=s[2]>=s[3]:
        k += 1

print(k)
# 129
# https://vkvideo.ru/video-205865487_456239692?t=1h22m37s