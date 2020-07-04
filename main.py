n1 = int(input('first number: '))
n2 = int(input('second number: '))

for i in range(1, n1+1):
    if n1 % i == 0 and n2 % i == 0:
        print(i, end=' ')