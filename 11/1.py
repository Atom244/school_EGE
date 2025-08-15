from math import *

kod = 9
char = ceil(log2(kod)) # ceil - округлние в большую сторону
pas = ceil((15*char) / 8)
total = pas * 25
print(total)
