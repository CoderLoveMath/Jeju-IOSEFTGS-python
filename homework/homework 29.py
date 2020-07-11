import numpy as np

def max_list(ds):
    m = ds[0]
    for i in range(1, len(ds)):
        if m < ds[i]:
            m = ds[i]
    return m

li = np.random.randint(0, 101, size=10)
print("Max is {}".format(max_list(li)))