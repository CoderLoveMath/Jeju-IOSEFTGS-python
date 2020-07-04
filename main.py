s = int(input('first number(small): '))
b = int(input('second number(big): '))

while True:
    r = b % s
    if r == 0:
        print(s)
        break
    else:
        b = s
        s = r