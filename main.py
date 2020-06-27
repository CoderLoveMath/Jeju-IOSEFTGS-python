import numpy as np
food = ['짜장면', '짬뽕', '볶음밥']
print(np.random.choice(food))
print(np.random.choice(food, 2))
print(np.random.choice(food, 2, replace=False))