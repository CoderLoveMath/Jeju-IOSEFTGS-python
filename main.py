import numpy as np

rlist = np.random.randint(1, 101, size=10)
print(rlist, type(rlist))

max = rlist[0]

for i in range(1, len(rlist)):
    if rlist[i] > max:
        max = rlist[i]

print('Maximum number:', max)