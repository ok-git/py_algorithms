import sys

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
● не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.

В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def count_mem(*args):
    return sum(map(sys.getsizeof, [*args]))


# Variant 1. Original
# ===================
MIN_ITEM = 2
MAX_ITEM = 100
array = [i for i in range(MIN_ITEM, MAX_ITEM)]
result = [0] * 10

for el in array:
    for denominator in range(2, 10):
        if el % denominator == 0:
            result[denominator] += 1

print("Количество кратных чисел, из исходного массива:")
for i in range(2, 10):
    print(f"{i} - {result[i]}")

print(f'Память занятая переменными {count_mem(MIN_ITEM, MAX_ITEM, array, result, el, denominator, i)} байт\n')
# Память занятая переменными 606 байт


# Variant 2. With recursive function
# ==================================
def rec_div(denominator, counter=0, i=2, max_i=99):
    if i == max_i:
        if i % denominator == 0:
            counter += 1
        global spam
        spam = count_mem(denominator, counter, i, max_i)
        return counter
    if i % denominator == 0:
        counter += 1
    i += 1
    return rec_div(denominator, counter, i)


print("Количество чисел из массива от 2 до 99, кратных от 2 до 9")
for num in range(2, 10):
    print(f"{num} - {rec_div(num)}")

print(f'Память занятая переменными {count_mem(num) + spam} байт')
print(f'Память занятая рекурсивной функцией {count_mem(rec_div)} байт\n')
# Память занятая переменными 70 байт
# Память занятая рекурсивной функцией 72 байт


# Variant 3. With generator
# =========================
def divider(n, m):
    for denominator in range(2, n + 1):
        counter = 0
        for i in range(2, m + 1):
            if i % denominator == 0:
                counter += 1
        global eggs
        eggs = count_mem(n, m, denominator, counter, i)
        yield denominator, counter


print("Количество чисел из массива от 2 до 99, кратных от 2 до 9:")
for denominator, counter in divider(9, 99):
    print(f"{denominator} - {counter}")

print(f'Память занятая переменными {count_mem(denominator, counter) + eggs} байт')
print(f'Память занятая функцией {count_mem(divider)} байт\n')
# Память занятая переменными 98 байт
# Память занятая функцией 72 байт


# Variant 4. With dict
# ====================
result = {a: 0 for a in range(2, 10)}

for el in range(2, 100):
    for denominator in result.keys():
        if el % denominator == 0:
            result[denominator] += 1

print("Количество кратных чисел, из исходного массива:")
for key, value in result.items():
    print(f"{key} - {value}")

print(f'Память занятая переменными {count_mem(result, el, denominator, key, value, result.items, result.keys)} байт\n')
# Память занятая переменными 340 байт

"""
ВЫВОДЫ

Версия Python - Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Версия ОС - Win10 64 bit

Вариант 1 - Память занятая переменными 606 байт (использованы списки)
Вариант 2 - Память занятая переменными 70 байт + память занятая рекурсивной функцией 72 байт = 142 байта
Вариант 3 - Память занятая переменными 98 байт + память занятая функцией-генератором 72 байт = 170 байт. 
Вариант 4 - Память занятая переменными 340 байт (использован словарь)

Ну уверен, правильно ли я подсчитал память занимаемую переменными и нужно ли в общий подсчёт прибавлять память,
занимаемую функциями (в вариантах 2 и 3), т.к. я уже учёл память занимаемую переменными этих функций. Думаю, если
функция это объект, то учитывать, наверное надо. Прошу подсказать этот момент. 

Самый эффективный вариант по памяти - 2, т.к. не используются списки, словари, мимнимум переменных

А глобальный вывод такой, что, чем меньше используется "продвинутых" структур данных (списков, словарей, множеств, т.д.)
и переменных вообще, тем меньше памяти расходуется.
"""
