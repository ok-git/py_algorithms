"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех
уроков.
Определить, какое число в массиве встречается чаще всего.
"""

import random
import timeit
import cProfile


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
    array.sort()  # хотел сравнить по времени встренную функцию sort()
    # print(array)
    max_value = None
    max_counter = 1
    counter = 1
    for i in range(len(array)-1):  # после сортировки, одинаковые числа группируются вместе
        if array[i] == array[i + 1]:  # если идущие подряд числа одинаковые, то...
            counter += 1  # считаем их количество
            if counter > max_counter:  # если нашли новое максимальное количество одинаковых чисел, то...
                max_counter = counter  # обновляем max_counter
                max_value = array[i]
        else:
            counter = 1  # иначе, последовательность одинаковых чисел прервалась, и начинаем считать заново
    return max_value, max_counter


def main():
    array = generator(3500)
    count_v1(array)
    count_v2(array)
    count_v3(array)


# array = generator(500)
# print(count_v1(array))
# print(count_v2(array))
# print(count_v3(array))

array = generator(500)
print(timeit.timeit("count_v1(array)", number=100, globals=globals()))  # 0.1708927
array = generator(1000)
print(timeit.timeit("count_v1(array)", number=100, globals=globals()))  # 0.3414209
array = generator(1500)
print(timeit.timeit("count_v1(array)", number=100, globals=globals()))  # 0.5325064
array = generator(2000)
print(timeit.timeit("count_v1(array)", number=100, globals=globals()))  # 0.6956275000000001
array = generator(2500)
print(timeit.timeit("count_v1(array)", number=100, globals=globals()))  # 0.8936796999999999
array = generator(3000)
print(timeit.timeit("count_v1(array)", number=100, globals=globals()))  # 1.0675035
array = generator(3500)
print(timeit.timeit("count_v1(array)", number=100, globals=globals()))  # 1.2351687999999994


array = generator(500)
print(timeit.timeit("count_v2(array)", number=100, globals=globals()))  # 0.7611140000000001
array = generator(1000)
print(timeit.timeit("count_v2(array)", number=100, globals=globals()))  # 3.0063449999999996
array = generator(1500)
print(timeit.timeit("count_v2(array)", number=100, globals=globals()))  # 6.7401822
array = generator(2000)
print(timeit.timeit("count_v2(array)", number=100, globals=globals()))  # 12.0239628
array = generator(2500)
print(timeit.timeit("count_v2(array)", number=100, globals=globals()))  # 18.7429846
array = generator(3000)
print(timeit.timeit("count_v2(array)", number=100, globals=globals()))  # 27.3788281
array = generator(3500)
print(timeit.timeit("count_v2(array)", number=100, globals=globals()))  # 37.0363588

array = generator(500)
print(timeit.timeit("count_v3(array)", number=100, globals=globals()))  # 0.007706499999997618
array = generator(1000)
print(timeit.timeit("count_v3(array)", number=100, globals=globals()))  # 0.015604199999998514
array = generator(1500)
print(timeit.timeit("count_v3(array)", number=100, globals=globals()))  # 0.02367959999999414
array = generator(2000)
print(timeit.timeit("count_v3(array)", number=100, globals=globals()))  # 0.031481299999995827
array = generator(2500)
print(timeit.timeit("count_v3(array)", number=100, globals=globals()))  # 0.04003939999999773
array = generator(3000)
print(timeit.timeit("count_v3(array)", number=100, globals=globals()))  # 0.04792129999999872
array = generator(3500)
print(timeit.timeit("count_v3(array)", number=100, globals=globals()))  # 0.05641090000000304


cProfile.run("main()")
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.393    0.393 <string>:1(<module>)
     3500    0.002    0.000    0.005    0.000 random.py:174(randrange)
     3500    0.001    0.000    0.006    0.000 random.py:218(randint)
     3500    0.002    0.000    0.003    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.007    0.007 task_1.py:12(generator)
        1    0.001    0.001    0.007    0.007 task_1.py:15(<listcomp>)
        1    0.012    0.012    0.012    0.012 task_1.py:19(count_v1)
        1    0.373    0.373    0.373    0.373 task_1.py:41(count_v2)
        1    0.001    0.001    0.001    0.001 task_1.py:57(count_v3)
        1    0.000    0.000    0.393    0.393 task_1.py:76(main)
        1    0.000    0.000    0.393    0.393 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     3500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     4402    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}

=======
Выводы:
=======

1. Алгоритм 1 показал линейную асимптотику (прирост 17 мс на каждом шаге) и среднее быстродействие из 3-х алгоритмов
2. Алгоритм 2 показал нелинейную асимптотику(прирост 2, 4, 5, 6, 10 сек на каждом шаге) и очень низкое быстродействие.
   сказывается вложенный цикл в цикл
3. Алгоритм 3 показал линейную асимптотику (прирост 7 мс на каждом шаге) и максимальное быстродействие из 3-х алгоритмов
4. Встроенная функция sort() крута, можно спокойно пользоваться, по cProfile она выполнялась менее 1 мс. Эта функция,
   круче, чем мои алгоритмы (надеюсь, пока) :-)
"""
