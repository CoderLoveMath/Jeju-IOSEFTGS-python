def whatisbig(n1, n2):
    if n1>n2:
        return n1
    elif n1<n2:
        return n2
    else:
        return None

a = int(input('integer: '))
b = int(input('integer: '))
print('Big:', whatisbig(a,b))