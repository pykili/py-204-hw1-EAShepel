for n in range(101):
    sum = 0
    for i in range(1, 2*n, 2):
        sum = sum + i
    if sum == n*n:
        print(n, '-', True)
    else:
        print(n, '-', False)
