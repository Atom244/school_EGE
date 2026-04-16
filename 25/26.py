for a1 in '0123456789':
    for a2 in '0123456789':
        for a3 in '0123456789':
            n = f'12{a1}345{a2}67089{a3}'
            if int(n)%206==0:
                print(n,int(n)//206)