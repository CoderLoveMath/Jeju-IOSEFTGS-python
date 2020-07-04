str = input('string: ')
isPal = True

for i in range(1, len(str)):
    if str[i] != str[len(str) - 1 - i]:
        isPal = False
        break

if isPal:
    print('Palindrome')
else:
    print('not Palindrome')