"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, надо вывести 6843.
"""


def rec_len(m):
    if m // 10 == 0:
        return 1
    else:
        return 1 + rec_len(m // 10)


def rec_reverse(n):
    if rec_len(n) == 1:
        return str(n)
    else:
        return str(n % 10) + rec_reverse(n // 10)


num = int(input("Введите целое число: "))
print(int(rec_reverse(num)))
