n = int(input('please input the number: '))
isPrime = True

for i in range(2, n):
    if n % i == 0:
        isPrime = False
        break

if isPrime:
    print('this is prime')
else:
    print('this is composite number')
