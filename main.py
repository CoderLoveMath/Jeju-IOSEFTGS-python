def whatisbig(n1, n2, n3):
    if n1>n2:
        if n1>n3:
            return n1
        elif n1<n3:
            return n3
    elif n1<n2:
        if n2 > n3:
            return n2
        elif n2 < n3:
            return n3
    return None

a = int(input('integer: '))
b = int(input('integer: '))
c = int(input('integer: '))
print('Big:', whatisbig(a,b,c))