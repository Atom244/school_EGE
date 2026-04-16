for a1 in '2468':
    for a2 in '02468':
        for a3 in '02468':
            for a4 in '02468':
                for n1 in '13579':
                    for n2 in '13579':
                        for n3 in '13579':
                            n = int(f'{a1}{n1}{a2}{a3}{n2}{a4}{n3}77')
                            if n % 7777 == 0:
                                print(n,n//7777)
