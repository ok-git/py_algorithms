"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def rec_len(m):
    if m // 10 == 0:
        return 1
    else:
        return 1 + rec_len(m // 10)


def rec_even_odd(n, even):
    if rec_len(n) == 1:
        if not n % 2:
            return 1 if even else 0
        else:
            return 1 if not even else 0
    else:
        if not n % 10 % 2:
            return 1 + rec_even_odd(n // 10, even) if even else rec_even_odd(n // 10, even)
        else:
            return 1 + rec_even_odd(n // 10, even) if not even else rec_even_odd(n // 10, even)


num = int(input("Введите целое число: "))
even = rec_even_odd(num, even=True)
odd = rec_even_odd(num, even=False)
print(f"В числе {num} содержится {even} чётных и {odd} нечётных цифр")
