import numpy as np

ds = np.random.randint(1, 5, size=5).tolist()
key = 3

for a in range(len(ds) - 1):
    for b in range(len(ds) - a - 1):
        if ds[b] > ds[b+1]:
            ds[b], ds[b+1] = ds[b+1], ds[b]

print(ds)

low = 0
high = len(ds) - 1

while low <= high:
    mid = (low + high) // 2
    if key == ds[mid]:
        print('ds[{i}] is {v}, high={h} and low={l}'.format(i=mid, v=ds[mid], h=high, l=low))
        break
    elif key < ds[mid]:
        high = mid - 1
    else:
        low = mid + 1