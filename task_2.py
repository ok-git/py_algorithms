"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Пример работы программ:
sieve(2)
3
prime(4)
7
"""

import timeit
import cProfile


def sieve(prime_count_target):
    assert prime_count_target < 9593, 'Value not supported'
    n = 100000
    a = [i for i in range(n)]  # создание массива с n количеством элементов
    a[1] = 0  # вторым элементом является единица, которую не считают простым числом
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    prime_number = None  # переменная для искомого простого числа
    prime_count = 0  # счётчик простых чисел

    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            prime_count += 1  # увеличиваем счётчик простого числа
            if prime_count == prime_count_target:  # если достигли заданного номера простого числа, то ...
                prime_number = a[m]  # берём значение простого числа и выходим из цикла
                break
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1
    return prime_number


def prime(prime_count_target):
    assert prime_count_target < 9593, 'Value not supported'
    n = 100000
    a = [i for i in range(2, n)]  # создание массива с n количеством элементов
    prime_number = None  # переменная для искомого простого числа
    prime_count = 0  # счётчик простых чисел
    for num in a:
        for divider in range(2, num):  # для каждого числа из массива ищем хотя бы один делитель, кроме 1 и его самого
            if num % divider == 0:  # если хотя бы один делитель найден, то число составное и тогда выходим из цикла
                break
        else:  # иначе найдено очередное простое число и...
            prime_count += 1  # увеличиваем счётчик простых чисел на 1
        if prime_count == prime_count_target:  # если достигли заданного номера простого числа, то ...
            prime_number = num  # берём значение простого числа и выходим из цикла
            break
    return prime_number


def main():
    sieve(1400)
    prime(1400)

# print(sieve(24))
# print(sieve(1229))
# print(sieve(9592))
#
# print(prime(24))
# print(prime(1229))
# print(prime(9592))


print(timeit.timeit("sieve(200)", number=100, globals=globals()))  # 2.6153535999999997
print(timeit.timeit("sieve(400)", number=100, globals=globals()))  # 2.7296734
print(timeit.timeit("sieve(600)", number=100, globals=globals()))  # 2.7996808
print(timeit.timeit("sieve(800)", number=100, globals=globals()))  # 2.864568799999999
print(timeit.timeit("sieve(1000)", number=100, globals=globals()))  # 2.915178299999999
print(timeit.timeit("sieve(1200)", number=100, globals=globals()))  # 2.9472734999999997
print(timeit.timeit("sieve(1400)", number=100, globals=globals()))  # 2.990636500000001

print(timeit.timeit("prime(200)", number=100, globals=globals()))  # 1.0242764999999991
print(timeit.timeit("prime(400)", number=100, globals=globals()))  # 3.4750795999999973
print(timeit.timeit("prime(600)", number=100, globals=globals()))  # 7.9940949
print(timeit.timeit("prime(800)", number=100, globals=globals()))  # 14.664172299999997
print(timeit.timeit("prime(1000)", number=100, globals=globals()))  # 23.646438600000003
print(timeit.timeit("prime(1200)", number=100, globals=globals()))  # 34.9518269
print(timeit.timeit("prime(1400)", number=100, globals=globals()))  # 48.6583857

cProfile.run("main()")
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.532    0.532 <string>:1(<module>)
        1    0.025    0.025    0.028    0.028 task_2.py:20(sieve)
        1    0.002    0.002    0.002    0.002 task_2.py:23(<listcomp>)
        1    0.500    0.500    0.502    0.502 task_2.py:43(prime)
        1    0.002    0.002    0.002    0.002 task_2.py:46(<listcomp>)
        1    0.001    0.001    0.532    0.532 task_2.py:61(main)
        1    0.000    0.000    0.532    0.532 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

=======
Выводы:
=======

1. Алгоритм "решето  Эратосфена" оказался достаточно эффективен, несмотря на его возраст. Линейная асимптотика, высокое
   быстродействие на всём диапазоне вводимых значений.
2. Мой алгоритм иммеет нелинейную асимптотику. На числах менее 200, он значительно превосходит алгоритм
   "решето Эратосфена", но на более высоких значениях выполняется очень долго, в десятки раз проигрывая ему по времени.

"""
