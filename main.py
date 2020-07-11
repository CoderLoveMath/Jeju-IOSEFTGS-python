def print_n(str, n):
    if n == 0:
        return
    print(str)
    print_n(str, n-1)

print_n('Hello!', 3)