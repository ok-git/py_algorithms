"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех
уроков.
Определить, какое число в массиве встречается чаще всего.
"""

import random


def generator(size):
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


def count_v1(array):
    # array = [0, 0, 1, 2, 3, 5, 5, 5, 7, 7, 8, 8, 8, 9, 7, 9, 5]
    # print(array)
    # Формируем массив-результат
    result = [[0, 0]]  # Массив содержит счётчик для каждого числа исходного массива - [number, counter]
    for number in array:
        for idx, val in enumerate(result):
            if number == val[0]:
                result[idx][1] += 1  # если число в массиве-результате уже есть, то увеличиваем счётчик числа на 1
                break
        else:
            result += [[number, 1]]  # если число в массиве-результате не находится, то добавляем его со счётчиком = 1
    # Ищем максимальный результат
    max_value = None
    max_counter = 1
    for el in result:  # ищем максимальный счётчик в массиве-результате
        if el[1] > max_counter:
            max_counter = el[1]
            max_value = el[0]
    return max_value, max_counter  # возвращаем [number, counter] для первого попавшегося максимального счётчика


def count_v2(array):
    # array = [0, 0, 1, 2, 3, 5, 5, 5, 7, 7, 8, 8, 8, 9, 7, 9, 5]
    # print(array)
    max_value = None
    max_counter = 1
    for number in array:  # сравниваем каждое число массива с каждым числом
        counter = 0
        for num in array:
            if number == num:
                counter += 1
        if counter > max_counter:
            max_counter = counter
            max_value = number
    return max_value, max_counter


def count_v3(array):
    # array = [0, 0, 1, 2, 3, 5, 5, 5, 7, 7, 8, 8, 8, 9, 7, 9, 5]
    # print(array)
    array.sort()
    # print(array)
    max_value = None
    max_counter = 1
    counter = 1
    for i in range(len(array)-1):
        if array[i] == array[i + 1]:
            counter += 1
            if counter > max_counter:
                max_counter = counter
                max_value = array[i]
        else:
            counter = 1
    return max_value, max_counter


array = generator(3000)
print(count_v1(array))
print(count_v2(array))
print(count_v3(array))
