ch = input('input letter: ')
key = int(input('distance: '))

print(chr(ord('a') + (ord(ch) - ord('a') - key) % 26))