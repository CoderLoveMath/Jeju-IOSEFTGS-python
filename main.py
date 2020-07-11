capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = capital.lower()

plain = input('Plain Text: ')
key = 3
cipher = ''

for ch in plain:
    if ch in small:
        cipher += small[(small.index(ch) + 3) % 26]
    elif ch in capital:
        cipher += capital[(capital.index(ch) + 3) % 26]
    else:
        cipher += ch

print('Cipher Text:', cipher)