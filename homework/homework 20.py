count = 0

for n in range(2, 50 + 1):
    isPrime = True

    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break

    if isPrime:
        count += 1
        print(n, end=' ')

print()
print('count: {}'.format(count))