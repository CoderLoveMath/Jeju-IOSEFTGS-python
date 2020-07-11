# imp_word = ['is', 'the', 'a', 'an']

cipher = input('Cipher text: ')
key = int(input('Input key: '))
plain = ''

for ch in cipher:
    if 'a' <= ch <= 'z':
        plain += chr(ord('a') + (ord(ch) - ord('a') - key) % 26)
    elif 'A' <= ch <= 'Z':
        plain += chr(ord('A') + (ord(ch) - ord('A') - key) % 26)
    else:
        plain += ch

print(plain)