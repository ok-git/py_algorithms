"""
 Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры
"""


def rec_sum_row(start, n):
    if n == 1:
        return start
    else:
        summand = start / 2
        summand = -summand
        n -= 1
        return start + rec_sum_row(summand, n)


num = int(input("Введите количество элементов ряда: "))
print(rec_sum_row(1, num))
