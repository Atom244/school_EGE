import string
import random

g = 'AEIOU'
s = 'BCDFGHJKLMNPQRSTVWXZ'
# 0.19 g
# 0.81 s

def randomaiser(n):
    if random.randint(0, n) <= n:
        return True
    return False

choices = ['s', 'g']

comblength = 50



def msg_gen(n):
    msg = ''
    for c in range(n):
        if random.choice(choices) == 's':
            if randomaiser(66):
                msg += random.choice(s)
            elif randomaiser(15):
                msg += random.choice(g)
        elif random.choice(choices) == 'g':
            if randomaiser(15):
                msg += random.choice(g)
            elif randomaiser(66):
                msg += random.choice(s)
        else:
            msg += ' '
    return msg

def msg_gen_improved(msg, n):
    for c in range(n):
        if msg.upper()[-1] in s:
            if randomaiser(66):
                msg += random.choice(s)
            elif randomaiser(15):
                msg += random.choice(g)
        elif msg.upper()[-1] in g:
            if randomaiser(15):
                msg += random.choice(g)
            elif randomaiser(66):
                msg += random.choice(s)
        else:
            msg += ' '
    return msg


for i in range(100):
    print(msg_gen(100))
