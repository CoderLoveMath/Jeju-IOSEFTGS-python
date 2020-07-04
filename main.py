# ver 1: use list
a = []

# init
for i in range(101):
    a.append(0)

for i in range(2, 101):
    if a[i] == 0:
        for j in range(2 * i, 101, i):
            a[j] = 1

for i in range(2, 101):
    if a[i] == 0:
        print(i, end=' ')

print()

# ver 2: use zeros
import numpy as np

a = np.zeros(101, dtype=int)
for i in range(2, 101):
    if a[i] == 0:
        for j in range(2 * i, 101, i):
            a[j] = 1

for i in range(2, 101):
    if a[i] == 0:
        print(i, end=' ')