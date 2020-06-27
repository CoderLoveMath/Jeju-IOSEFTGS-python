# first triangle
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

print('-----------------')

# second triangle
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

print('-----------------')

# third triangle
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()