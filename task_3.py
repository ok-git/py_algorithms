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

min_val, min_idx = array[0], 0
max_val, max_idx = array[0], 0

for idx, el in enumerate(array):
    if el < min_val:
        min_val = el
        min_idx = idx
    if el > max_val:
        max_val = el
        max_idx = idx
array[min_idx], array[max_idx] = array[max_idx], array[min_idx]
print(array)