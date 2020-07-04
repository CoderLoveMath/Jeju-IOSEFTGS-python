ch = input('input letter: ')
key = int(input('distance: '))
asci = ord(ch) + key
if asci > 122:
    asci = asci - 122 + 96
print(chr(asci))