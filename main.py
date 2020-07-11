import numpy as np

ds = np.random.randint(1, 101, size=100)
print(ds)
key = 1
found = False

for a in range(len(ds)):
    if key == ds[a]:
        found = True
        print("ds[{a}] is {va}".format(a=a, va=ds[a]))
        break