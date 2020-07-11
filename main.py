def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a

n1 = int(input('First number: '))
n2 = int(input('Second number: '))
print('diff: {}'.format(diff(n1, n2)))