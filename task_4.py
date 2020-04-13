"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

# Формируем массив-результат
result = [[0, 0]]  # Массив содержит счётчик для каждого числа исходного массива - [number, counter]
for number in array:
    for idx, val in enumerate(result):
        if number == val[0]:
            result[idx][1] += 1  # если число в массиве-результате уже есть, то увеличиваем счётчик числа на 1
            break
    else:
        result += [[number, 1]]  # если число в массиве-результате не находится, то добавляем его со счётчиком = 1
print(f'\nМассив со счётчиками чисел исходного массива: {result}')

# Ищем все максимальные результаты и помещаем их в max_results
max_results = []
max_counter = 2
for idx, el in enumerate(result):
    if el[1] < max_counter:  # если счётчик меньше максимального, тогда новая итерация
        continue
    if el[1] > max_counter:  # если найден новый максимальный счётчик, тогда
        max_counter = el[1]  # обновляем максимум
        max_results = []  # и начинаем формировать новый массив значений [number, counter]
    max_results += [el]  # добавляем очередное значение [number, counter] в массив

# Выводим все результаты
print('\nЧисла, которые встречаются чаще всего:', *[n[0] for n in max_results], 'в количестве', max_results[0][1], 'шт')
