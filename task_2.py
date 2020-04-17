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


def sieve(prime_count_target):
    assert prime_count_target < 9593
    n = 100000
    a = [i for i in range(n)]  # создание массива с n количеством элементов

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    prime_number = 2
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
    assert prime_count_target < 9593
    n = 100000
    a = [i for i in range(2, n)]  # создание массива с n количеством элементов
    prime_number = 2
    prime_count = 0  # счётчик простых чисел
    for num in a:
        k = 0
        for divider in range(2, num):
            if k > 1:
                break
            if num % divider == 0:
                k += 1
        prime_count += 1
        if prime_count == prime_count_target:  # если достигли заданного номера простого числа, то ...
            prime_number = num  # берём значение простого числа и выходим из цикла
            break
    return prime_number


print(sieve(24))
print(sieve(1229))
print(sieve(9592))

print(prime(24))
print(prime(1229))
print(prime(9592))
