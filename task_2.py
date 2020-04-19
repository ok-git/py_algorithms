"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

hex_a, hex_b = map(list, input('Введите два hex числа через пробел: ').split())
base = deque('123456789abcdef')
base.extend(['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C', '1D', '1E', '1F'])

result = deque()
extra_digit = 0
for digit_a, digit_b in zip(hex_a[::-1], hex_b[::-1]):
    if digit_a != '0' and digit_b != '0':
        idx_a = base.index(digit_a)
        idx_b = base.index(digit_b)
        base.rotate(-idx_b - 1)  # сдвинули для получения результата сложения текущего разряда
        result_digit = base[idx_a][-1]
        base.rotate(idx_b + 1)  # вернули базу в исходное
        result.appendleft(result_digit)
print(result)
