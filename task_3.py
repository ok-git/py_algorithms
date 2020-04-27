"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках
"""
import random

m = 5
array = [random.randint(0, 99) for _ in range(2 * m + 1)]
print(array)

array = [45, 32, 53, 45, 62, 64, 56, 58, 74, 30, 13]
print(array)
print([13, 30, 32, 45, 45, 53, 56, 58, 62, 64, 74])

median = None
median_counter = len(array) // 2
for i in array:
    el_less_counter = 0
    el_more_counter = 0
    for j in array:
        if i < j:
            el_less_counter += 1
        if i > j:
            el_more_counter += 1
    if el_more_counter == median_counter and el_less_counter == median_counter:
        median = i
print(median)
