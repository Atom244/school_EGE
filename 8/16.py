# https://vkvideo.ru/video-205865487_456239692?t=1h25m10s

from itertools import *

k = 0
for x in product(sorted('АКРУ'), repeat=5):
    s = ''.join(x)
    k += 1
    if k == 150:
        print(k, s)

# АРККК