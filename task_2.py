"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


# Адаптация для Python алгоритма простого двухпутевого слияния на псевдокоде с Википедии
def rec_merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    left = rec_merge_sort(left)
    right = rec_merge_sort(right)
    result = merge(left, right)
    return result


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
    for chunk in range(1, len(array) // 2):
        result = []
        for i in range(0, len(array), chunk):
            left = array[i:chunk]
            right = array[i + chunk:i + chunk + chunk]
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
        array = result
    return array


array = [random.uniform(0, 49) for _ in range(10)]
print(array)
print(rec_merge_sort(array))
array = [random.uniform(0, 49) for _ in range(6)]
print(array)
print(merge_sort(array))
