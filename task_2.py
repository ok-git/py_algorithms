"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


# Адаптация алгоритма простого двухпутевого слияния на псевдокоде с Википедии на Python
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    return result


def merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left, right)
    return result


array = [random.uniform(0, 49) for _ in range(10)]
print(array)

print(merge_sort(array))
