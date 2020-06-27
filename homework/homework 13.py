import numpy as np

amo = int(input('Input count of students: '))
lucky_amo = int(input('Input count of lucky: '))

array = np.array(range(1, amo + 1))
np.random.shuffle(array)

lucky = array[:lucky_amo]
print(lucky)
