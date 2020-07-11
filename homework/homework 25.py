capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = capital.lower()

cipher = input('Plain Text: ')
key = int(input('Input Key: '))
plain = ''

for ch in cipher:
    if ch in small:
        plain += small[(small.index(ch) - key) % 26]
    elif ch in capital:
        plain += capital[(capital.index(ch) - key) % 26]
    else:
        plain += ch

print('plain text: {}'.format(plain))