def s(a):
    if a == 1:
        return 1
    else:
        return a + s(a-1)

print(s(100))