for n in range(0,100,5):
    for x in range(1, n):
        if n % x == 0 and x >= 2:
            print(n, 'La multiplicación para', x, '*', n//x)
            break
        if n == 5 and x == 1:
            print(n, 'La multiplicación dede 5 * 1')
    if n == 0:
        print(n, 'La multiplicación de 5 * 0')