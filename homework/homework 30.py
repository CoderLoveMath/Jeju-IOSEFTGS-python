import numpy as np

def average_list(ds):
    s = 0
    for i in range(len(ds)):
        s += ds[i]

    return s / len(ds)

li = np.random.randint(1, 101, size=10)
print('Average is {}'.format(average_list(li)))