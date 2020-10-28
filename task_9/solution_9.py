for n in range(101):
    summ = 0
    for i in range(1, 2*n, 2):
        summ = summ + i
    if summ == n*n:
        print(n, '-', True)
    else:
        print(n, '-', False)
