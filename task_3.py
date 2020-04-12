"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
result = []
print(array)

min_val, min_idx = 0, 0
max_val, max_idx = 0, 0

for el in enumerate(array):
    pass

