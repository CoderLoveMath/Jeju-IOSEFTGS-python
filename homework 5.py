import math


a = int(input('integer: '))
b = int(input('integer: '))

# math library
print(str(int(math.fabs(a-b))))

# comparing
if a > b:
    print(str(a - b))
else:
    print(str(b - a))
