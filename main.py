import numpy as np

ds = np.random.randint(1, 101, size=100).tolist()
print(ds)
key = 1

if key in ds:
    print("ds[{i}] is {v}".format(i=ds.index(key), v=key))