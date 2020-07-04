n1 = int(input('first number: '))
n2 = int(input('second number: '))

gcd = 0
for i in range(1, n1+1):
    if n1 % i == 0 and n2 % i == 0:
        if i > gcd:
            gcd = i
        # print(i, end=' ')

# print()
print('gcd: {}'.format(gcd))