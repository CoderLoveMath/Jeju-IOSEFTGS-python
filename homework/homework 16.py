n = int(input('number: '))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1
        print(i, end=' ')

print()
print('count:', count)