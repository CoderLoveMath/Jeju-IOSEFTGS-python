plain = input('Plain Text: ')
key = 3
cipher = ''

for ch in plain:
    if 'a' <= ch <= 'z':
        cipher += chr(ord('a') + (ord(ch) - ord('a') + key) % 26)
    elif 'A' <= ch <= 'Z':
        cipher += chr(ord('A') + (ord(ch) - ord('A') + key) % 26)
    else:
        cipher += ch

print('Cipher Text:', cipher)