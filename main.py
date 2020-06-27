for i in range(5):
    print(i, end=" ")

print()

# using for statement
ran = int(input("range: "))
s = 0
for i in range(1, ran + 1):
    s += i
print('sum is', s)

# using math
getsum = lambda r: (r + 1) * r / 2
print('also sum is,', getsum(ran))