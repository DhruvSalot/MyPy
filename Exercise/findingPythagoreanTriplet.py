def pythaTriplet():
    a = []
    for l in range(1,201):
        for m in range(1,201):
            for n in range(1,201):
                if n**2 + m**2 == l**2:
                    print ([n, m, l])
                    a += [n, m, l]
    print (int(len(a)/6))



pythaTriplet()
