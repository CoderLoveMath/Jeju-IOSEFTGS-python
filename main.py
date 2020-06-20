mode = input('C or F (temp standard): ')
temp = int(input('temp: '))

if mode == 'C':
    print(temp * 9 / 5 + 32)
else:
    print((temp - 32) * 5 / 9)