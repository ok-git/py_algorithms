"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
● не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

# Variant 1. Original
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

print()


# Variant 2. With recursive function
def rec_div(denominator, counter=0, i=2, max_i=99):
    if i == max_i:
        if i % denominator == 0:
            counter += 1
        return counter
    if i % denominator == 0:
        counter += 1
    i += 1
    return rec_div(denominator, counter, i)


print("Количество чисел из массива от 2 до 99, кратных от 2 до 9")
for num in range(2, 10):
    print(f"{num} - {rec_div(num)}")

print()


# Variant 3. With generator
def divider(n, m):
    for denominator in range(2, n + 1):
        counter = 0
        for i in range(2, m + 1):
            if i % denominator == 0:
                counter += 1
        yield denominator, counter


print("Количество кратных чисел, из исходного массива:")
for denominator, counter in divider(9, 99):
    print(f"{denominator} - {counter}")
