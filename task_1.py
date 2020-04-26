"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random
import timeit


def sort_bubble_lesson(array):  # алгоритм с урока, для сравнения
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


def sort_bubble(array):  # алгоритм доработанный
    n = 1
    while n < len(array):
        sorted_ = True  # предполагаем, что каждый раз последний, и сейчас мы достигнем сортировки
        for i in range(len(array) - n):  # не проходим по тем позициям, которые уже отсортированы
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted_ = False  # если меняли местами элементы, значит ещё не достигли сортировки
        n += 1
        if sorted_:  # достигли сортировки, выходим из цикла
            break
    return array


a_1 = [random.randint(-100, 99) for _ in range(100)]
a_2 = a_1.copy()

print(a_1)

# print(timeit.timeit("sort_bubble_lesson(a_1)", number=100, globals=globals()))  # 0.10688 (100 эл.) 10.9536 (1000 эл.)
# print(timeit.timeit("sort_bubble(a_2)", number=100, globals=globals()))         # 0.00207 (100 эл.) 0.11373 (1000 эл.)
# Разница в скорости впечатляет. Делал запуски на разаных данных - аналогичная разница между алгоритмами сохраняется

print(sort_bubble_lesson(a_1))
print(sort_bubble(a_2))
