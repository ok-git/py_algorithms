"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def rec_len(num):
    if num // 10 == 0:
        return 1
    else:
        return 1 + rec_len(num // 10)


def rec_even_odd(num, even):
    if rec_len(num) == 1:
        if not num % 2:
            return 1 if even else 0
        else:
            return 1 if not even else 0
    else:
        if not num % 10 % 2:
            return 1 + rec_even_odd(num // 10, even) if even else rec_even_odd(num // 10, even)
        else:
            return 1 + rec_even_odd(num // 10, even) if not even else rec_even_odd(num // 10, even)


num = int(input("Введите целое число: "))
even = rec_even_odd(num, even=True)
odd = rec_even_odd(num, even=False)
print(f"В числе {num} содержится {even} чётных и {odd} нечётных цифр")
