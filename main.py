str1 = input('string: ')
str2 = ""

for i in range(len(str1) - 1, -1, -1):
    str2 = str2 + str1[i]

if str1 == str2:
    print('Palindrome')
else:
    print('not Palindrome')