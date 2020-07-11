import numpy as np
ds = np.random.randint(1, 101, size=5)
print(ds)

for a in range(0, len(ds) - 1):
    for b in range(0, len(ds) - a - 1):
        if ds[b + 1] < ds[b]:
            ds[b], ds[b+1] = ds[b+1], ds[b]

print(ds)
