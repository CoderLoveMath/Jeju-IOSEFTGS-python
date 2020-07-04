for n in range(1, 20 + 1):
    print(n, end=': ')
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')
    print()